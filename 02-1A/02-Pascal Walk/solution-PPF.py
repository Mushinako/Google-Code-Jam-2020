#!/usr/bin/env python3
import math


def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)


def find_path(n):
    k = math.ceil(math.log2(n + 1))
    results = []
    for i in range(1, k, 2):
        for j in range(1, i + 1):
            results.append((i, j))
        for j in range(i + 1, 0, -1):
            results.append((i + 1, j))
    k_odd = k % 2
    if k_odd:
        for j in range(1, k + 1):
            results.append((k, j))
    diff = 2 ** k - 1 - n
    cur_row = k
    cur_col = 1 if k_odd else cur_row
    while diff > 1:
        # Remove
        if cur_col < 1 or cur_col > cur_row:
            cur_row -= 2
            cur_col = 1 if k_odd else cur_row
            continue
        bottom_to_remove_val = nCr(cur_row - 1, cur_col - 1)
        if diff < bottom_to_remove_val:
            cur_row -= 2
            cur_col = 1 if k_odd else cur_row
            continue
        diff -= bottom_to_remove_val
        results.remove((cur_row, cur_col))
        if k_odd:
            if cur_col >= cur_row - 1:
                cur_row -= 2
                cur_col = 1 if k_odd else cur_row
                continue
        else:
            if cur_col <= 2:
                cur_row -= 2
                cur_col = 1 if k_odd else cur_row
                continue
        tmp_row = cur_row - 1
        tmp_col = cur_col if k_odd else cur_col - 1
        top_to_remove_val = nCr(tmp_row - 1, tmp_col - 1)
        if diff < top_to_remove_val:
            cur_row -= 2
            cur_col = 1 if k_odd else cur_row
            continue
        diff -= top_to_remove_val
        results.remove((tmp_row, tmp_col))
        cur_col = cur_col + (1 if k_odd else - 1)
    if diff == 1:
        results.remove((k, k if k_odd else 1))
    return results


def main():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        result = find_path(n)
        print('Case #{}:'.format(case))
        for step in result:
            print(*step)


if __name__ == "__main__":
    exit_code = main()
