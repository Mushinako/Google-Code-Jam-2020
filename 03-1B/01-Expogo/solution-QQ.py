#!/usr/bin/env python3
def expogo(x, y):
    x_neg = x < 0
    y_neg = y < 0
    x = abs(x)
    y = abs(y)
    if (x + y) % 2 == 0:
        return "IMPOSSIBLE"
    steps = []
    opposite = {"W": "E", "E": "W", "N": "S", "S": "N"}
    x_bin = bin(x)[2:][::-1]
    y_bin = bin(y)[2:][::-1]
    shorter_len = min(len(x_bin), len(y_bin))
    for d in range(shorter_len):
        if x_bin[d] == y_bin[d]:
            if x_bin[d] == "1":
                return "IMPOSSIBLE"
            else:
                last_step = steps.pop()
                steps.append(opposite[last_step])
                steps.append(last_step)
        else:
            if x_bin[d] == "1":
                steps.append("E")
            else:
                steps.append("N")
    if len(x_bin) > len(y_bin):
        for d in range(shorter_len, len(x_bin)):
            if x_bin[d] == "1":
                steps.append("E")
            else:
                last_step = steps.pop()
                steps.append(opposite[last_step])
                steps.append(last_step)
    else:
        for d in range(shorter_len, len(y_bin)):
            if y_bin[d] == 1:
                steps.append("N")
            else:
                last_step = steps.pop()
                steps.append(opposite[last_step])
                steps.append(last_step)
    if x_neg:
        steps = [opposite[s] if s in "WE" else s for s in steps]
    if y_neg:
        steps = [opposite[s] if s in "NS" else s for s in steps]
    return "".join(steps)


def main():
    t = int(input())
    for case in range(1, t+1):
        x, y = [int(coord) for coord in input().split()]
        result = expogo(x, y)
        print("Case #{0}: {1}".format(case, result))


if __name__ == "__main__":
    main()
