#!/usr/bin/env python3
from collections import Counter


def oversized_pancake_choppers(d, a_old):
    if sum(a_old) / d < min(a_old):
        return d - 1
    a = Counter(a_old)
    num, count = a.most_common(1)[0]
    del a[num]
    if count >= d:
        return 0
    left = d - count
    cut = 0
    for i in range(2, 51):
        new_num = i * num
        if new_num not in a:
            continue
        capacity = a[new_num] * i
        if capacity <= left:
            left -= capacity
            cut += a[new_num] * (i - 1)
            del a[new_num]
            if not left:
                return cut
            continue
        whole = left // i
        residue = left % i
        cut += whole * (i - 1) + residue
        return cut
    # Residue
    return cut + left


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, d = [int(num) for num in input().split()]
        a = sorted([int(num) for num in input().split()])
        result = oversized_pancake_choppers(d, a)
        print('Case #{0}: {1}'.format(case, result))


if __name__ == "__main__":
    exit_code = main()
