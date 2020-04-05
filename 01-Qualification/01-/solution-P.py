#!/usr/bin/env python3
def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        m = [[int(x) for x in input().split()] for _ in range(n)]
        k = 0
        for j, row in enumerate(m):
            k += row[j]
        r = len([0 for row in m if not unique(row)])
        c = len([0 for col in zip(*m) if not unique(col)])
        print('Case #{0}: {1} {2} {3}'.format(i, k, r, c))


def unique(li):
    return len(set(li)) == len(li)


if __name__ == '__main__':
    result = main()
