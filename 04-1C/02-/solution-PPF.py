#!/usr/bin/env python3
from collections import Counter


def overrandomized(u, responses):
    pool = set(''.join(responses))
    heads = sorted([s[0] for s in responses])
    non_zeros = set(''.join(heads))
    zero = tuple(pool - non_zeros)[0]
    count = Counter(heads)
    digits = sorted(non_zeros, key=lambda x: count[x], reverse=True)
    return zero + ''.join(digits)


def main():
    t = int(input())
    for case in range(1, t + 1):
        u = int(input())
        responses = list([input().split()[1] for _ in range(10 ** 4)])
        responses.sort()
        responses.sort(key=len)
        result = overrandomized(u, responses)
        print('Case #{0}: {1}'.format(case, result))


if __name__ == "__main__":
    exit_code = main()
