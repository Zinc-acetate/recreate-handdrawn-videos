#!/usr/bin/env python3
"""Check declared half-open frame intervals, never visual correctness. Python 3 stdlib."""
import argparse
import json
import sys


def integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f'{name} must be an integer')
    return value


def spans(value, duration, name):
    if not isinstance(value, list):
        raise ValueError(f'{name} must be a list')
    result = []
    for i, pair in enumerate(value):
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError(f'{name}[{i}] must be [start, end]')
        a, b = [integer(x, name) for x in pair]
        if not 0 <= a < b <= duration:
            raise ValueError(f'{name}[{i}] must satisfy 0 <= start < end <= duration_frames')
        result.append((a, b))
    return result


def union(intervals):
    result = []
    for a, b in sorted(intervals):
        if result and a <= result[-1][1]:
            result[-1] = (result[-1][0], max(b, result[-1][1]))
        else:
            result.append((a, b))
    return result


def subtract(required, covered):
    missing = []
    for a, b in union(required):
        cursor = a
        for c, d in union(covered):
            if d <= cursor or c >= b:
                continue
            if c > cursor:
                missing.append((cursor, min(c, b)))
            cursor = max(cursor, d)
            if cursor >= b:
                break
        if cursor < b:
            missing.append((cursor, b))
    return missing


def check(data):
    if not isinstance(data, dict):
        raise ValueError('manifest must be an object')
    duration = integer(data['duration_frames'], 'duration_frames')
    if duration <= 0:
        raise ValueError('duration_frames must be positive')
    shots = spans(data['shots'], duration, 'shots')
    allowed = spans(data.get('allowed_overlaps', []), duration, 'allowed_overlaps')
    overlap = []
    for i, (a, b) in enumerate(shots):
        for c, d in shots[i + 1:]:
            if max(a, c) < min(b, d):
                overlap.append((max(a, c), min(b, d)))
    errors = []
    for label, missing in [('shot_gaps', subtract([(0, duration)], shots)),
                           ('undeclared_shot_overlaps', subtract(overlap, allowed))]:
        if missing:
            errors.append({'kind': label, 'frames': missing})
    replacements = data.get('replacements', [])
    if not isinstance(replacements, list):
        raise ValueError('replacements must be a list')
    ids = set()
    for entry in replacements:
        if not isinstance(entry, dict) or not isinstance(entry.get('id'), str) or not entry['id'].strip():
            raise ValueError('each replacement needs a nonempty string id')
        label = entry['id']
        if label in ids:
            raise ValueError(f'duplicate replacement id: {label}')
        ids.add(label)
        visible = spans(entry['visible'], duration, f'{label}.visible')
        if not visible:
            raise ValueError(f'{label}.visible must not be empty; omit nonvisible replacements')
        covered = spans(entry['covered'], duration, f'{label}.covered')
        before = integer(entry.get('guard_before', 0), 'guard_before')
        after = integer(entry.get('guard_after', 0), 'guard_after')
        if min(before, after) < 0:
            raise ValueError('guards must be nonnegative')
        required = [(max(0, a - before), min(duration, b + after)) for a, b in visible]
        missing = subtract(required, covered)
        if missing:
            errors.append({'kind': 'replacement_coverage_gap', 'id': label, 'frames': missing})
    return {'ok': not errors, 'duration_frames': duration, 'errors': errors,
            'scope': 'Declared intervals only; inspect source and rendered frames independently.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', help='JSON manifest; schema in references/timing-and-coverage.md')
    args = parser.parse_args()
    try:
        with open(args.manifest, encoding='utf-8') as f:
            report = check(json.load(f))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'ok': False, 'input_error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
