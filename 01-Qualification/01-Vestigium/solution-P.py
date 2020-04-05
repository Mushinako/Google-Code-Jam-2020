#!/usr/bin/env python3
def unique(li):
    return len(set(li)) == len(li)


def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        m = [[int(x) for x in input().split()] for _ in range(n)]
        # Trace
        k = 0
        for j, row in enumerate(m):
            k += row[j]
        # Row duplicates
        r = len([0 for row in m if not unique(row)])
        # Col duplicates
        c = len([0 for col in zip(*m) if not unique(col)])
        print('Case #{0}: {1} {2} {3}'.format(i, k, r, c))


if __name__ == '__main__':
    result = main()
