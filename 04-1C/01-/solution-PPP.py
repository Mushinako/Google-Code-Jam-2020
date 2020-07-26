#!/usr/bin/env python3
def overexcited_fan(x, y, path):
    if x == y == 0:
        return 0
    for i, move in enumerate(path):
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        else:
            x -= 1
        if abs(x) + abs(y) <= i + 1:
            return i + 1
    return 'IMPOSSIBLE'


def main():
    t = int(input())
    for case in range(1, t + 1):
        x_str, y_str, path = input().split()
        x = int(x_str)
        y = int(y_str)
        result = overexcited_fan(x, y, path)
        print('Case #{0}: {1}'.format(case, result))


if __name__ == "__main__":
    exit_code = main()
