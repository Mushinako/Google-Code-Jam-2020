#!/usr/bin/env python3
def pattern_matching(patterns):
    first_arr = sorted(p[0] for p in patterns)
    first = ''
    for f in first_arr:
        if len(first) < len(f) and (first == f[: len(first)] or not first):
            first = f
            continue
        if len(first) >= len(f) and (first[: len(f)] == f or not f):
            continue
        return '*'
    last_arr = sorted(p[-1] for p in patterns)
    last = ''
    for l in last_arr:
        if len(last) < len(l) and (last == l[-len(last):] or not last):
            last = l
            continue
        if len(last) >= len(l) and (last[-len(l):] == l or not l):
            continue
        return '*'
    middle = ''.join(''.join(p[1:-1]) for p in patterns)
    return first + middle + last


def main():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        patterns = [input().split('*') for _ in range(n)]
        result = pattern_matching(patterns)
        print('Case #{0}: {1}'.format(case, result))


if __name__ == "__main__":
    exit_code = main()
