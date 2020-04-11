#!/usr/bin/env python3
def square_dance(s, r, c):
    score = 0
    new_s = s
    s = []
    while s != new_s:
        s = new_s
        new_s = [row[:] for row in s]
        score += sum(sum(row) for row in s)
        for i in range(r):
            for j in range(c):
                if not s[i][j]:
                    continue
                neighbors = []
                # Left neighbor
                for k in range(j - 1, -1, -1):
                    if s[i][k]:
                        neighbors.append(s[i][k])
                # Right neighbor
                for k in range(j + 1, c):
                    if s[i][k]:
                        neighbors.append(s[i][k])
                # Top neighbor
                for k in range(i - 1, -1, -1):
                    if s[k][j]:
                        neighbors.append(s[k][j])
                # Botton neighbor
                for k in range(i + 1, r):
                    if s[k][j]:
                        neighbors.append(s[k][j])
                if not neighbors:
                    continue
                avg = sum(neighbors) / len(neighbors)
                if s[i][j] < avg:
                    new_s[i][j] = 0
    return score


def main():
    t = int(input())
    for case in range(1, t + 1):
        r, c = map(int, input().split())
        s = [[int(x) for x in input().split()] for _ in range(r)]
        result = square_dance(s, r, c)
        print('Case #{0}: {1}'.format(case, result))


if __name__ == "__main__":
    exit_code = main()
