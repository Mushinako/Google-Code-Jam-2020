#!/usr/bin/env python3
import itertools
import random


def print_possible(i, sq):
    print('Case #{}: POSSIBLE'.format(i))
    for row in sq:
        print(' '.join((str(x) for x in row)))


def print_impossible(i):
    print('Case #{}: IMPOSSIBLE'.format(i))


def diag_mat(n, d):
    row = [(x + d - 1) % n + 1 for x in range(n)]
    mat = [row]
    for _ in range(n - 1):
        row = row[-1:] + row[:-1]
        mat.append(row)
    return mat


def find_0(n, sq):
    for i in range(n):
        for j in range(n):
            if not sq[i][j]:
                return (True, i, j)
    return (False, 0, 0)


def fill_square(n, sq):
    filled = []
    counter = 0
    while True:
        # Find 0
        found_0, i, j = find_0(n, sq)
        if not found_0:
            return (True, sq)
        # Fill at i,j
        cand = set(range(1, n + 1))
        for k in range(n):
            cand.discard(sq[i][k])
        for k in range(n):
            cand.discard(sq[k][j])
        if not cand:
            for row in sq:
                print(row)
            print()
            if counter > n:
                return (False, [])
            i, j = filled.pop()
            sq[i][j] = 0
            counter += 1
            continue
            # return (False, [])
        sq[i][j] = random.choice(tuple(cand))
        filled.append((i, j))
        counter = 0


def latin_square(n, diag):
    diag.sort()
    diag.sort(key=lambda x: diag.count(x))
    first_fillers = [x for i, x in enumerate(diag) if diag.index(x) == i]
    sq = [[0] * n for _ in range(n)]
    for i in range(n):
        sq[i][i] = diag[i]

    while True:
        tmp_sq = [row[:] for row in sq]
        result, tmp_sq = fill_square(n, tmp_sq)
        if result:
            return tmp_sq


def main():
    t = int(input())
    for i in range(1, t+1):
        n, k = [int(x) for x in input().split()]

        if n == 2:
            if k == 2:
                print_possible(i, ((1, 2), (2, 1)))
            elif k == 4:
                print_possible(i, ((2, 1), (1, 2)))
            else:
                print_impossible(i)
            continue

        if n == 3:
            if k == 3:
                print_possible(i, diag_mat(3, 1))
            elif k == 6:
                print_possible(i, diag_mat(3, 2))
            elif k == 9:
                print_possible(i, diag_mat(3, 3))
            else:
                print_impossible(i)
            continue

        if k in (n + 1, n * n - 1):
            print_impossible(i)
            continue

        if not k % n:
            print_possible(i, diag_mat(n, k // n))
            continue

        if k % n == 1:
            diag = [k // n] * n
            diag[-1] += 1
            diag[-2] += 1
            diag[-3] -= 1
        elif k % n == n - 1:
            diag = [k // n + 1] * n
            diag[-1] -= 1
            diag[-2] -= 1
            diag[-3] += 1
        else:
            diag = [k // n] * n
            diag_res = k % n
            for j in range(1, diag_res + 1):
                diag[-j] += 1

        square = latin_square(n, diag)
        print_possible(i, square)


if __name__ == '__main__':
    result = main()
