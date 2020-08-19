#!/usr/bin/env python3
from sys import exit


QUARTER_BOARD = int(5e8)
HALF_BOARD = int(1e9)
SPECIAL_POINTS = [
    (0, 0),
    (-QUARTER_BOARD, -QUARTER_BOARD),
    (-QUARTER_BOARD, QUARTER_BOARD),
    (QUARTER_BOARD, -QUARTER_BOARD),
    (QUARTER_BOARD, QUARTER_BOARD),
]

CENTER_RESPONSE = "CENTER"
HIT_RESPONSE = "HIT"
MISS_RESPONSE = "MISS"


def query(x, y):
    print(x, y, flush=True)
    response = input()
    return response == CENTER_RESPONSE, response


def left_binary_search(xmax, y):
    xmin = -HALF_BOARD
    done, response = query(xmin, y)
    if done:
        return True, None
    if response == HIT_RESPONSE:
        return False, xmin
    while True:
        if xmax - xmin == 1:
            return False, xmax
        xavg = (xmin + xmax) // 2
        done, response = query(xavg, y)
        if done:
            return True, None
        if response == HIT_RESPONSE:
            xmax = xavg
        else:
            xmin = xavg


def right_binary_search(xmin, y):
    xmax = HALF_BOARD
    done, response = query(xmax, y)
    if done:
        return True, None
    if response == HIT_RESPONSE:
        return False, xmax
    while True:
        if xmax - xmin == 1:
            return False, xmin
        xavg = (xmin + xmax) // 2
        done, response = query(xavg, y)
        if done:
            return True, None
        if response == HIT_RESPONSE:
            xmin = xavg
        else:
            xmax = xavg


def down_binary_search(x, ymax):
    ymin = -HALF_BOARD
    done, response = query(x, ymin)
    if done:
        return True, None
    if response == HIT_RESPONSE:
        return False, ymin
    while True:
        if ymax - ymin == 1:
            return False, ymax
        yavg = (ymin + ymax) // 2
        done, response = query(x, yavg)
        if done:
            return True, None
        if response == HIT_RESPONSE:
            ymax = yavg
        else:
            ymin = yavg


def up_binary_search(x, ymin):
    ymax = HALF_BOARD
    done, response = query(x, ymax)
    if done:
        return True, None
    if response == HIT_RESPONSE:
        return False, ymax
    while True:
        if ymax - ymin == 1:
            return False, ymin
        yavg = (ymin + ymax) // 2
        done, response = query(x, yavg)
        if done:
            return True, None
        if response == HIT_RESPONSE:
            ymin = yavg
        else:
            ymax = yavg


def blindfold_bullseye(a, b):
    start_x = start_y = 0
    for pt in SPECIAL_POINTS:
        done, response = query(*pt)
        if done:
            return
        if response == HIT_RESPONSE:
            start_x, start_y = pt
            break
    # Keep going left
    done, xmin = left_binary_search(start_x, start_y)
    if done:
        return
    # Keep going right
    done, xmax = right_binary_search(start_x, start_y)
    if done:
        return
    # Keep going down
    done, ymin = down_binary_search(start_x, start_y)
    if done:
        return
    # Keep going up
    done, ymax = up_binary_search(start_x, start_y)
    if done:
        return
    # Got 4 points, find center
    xavg = (xmin + xmax) // 2
    yavg = (ymin + ymax) // 2
    done, response = query(xavg, yavg)
    if done:
        return
    exit(-1)


def main():
    t, a, b = [int(x) for x in input().split()]
    for case in range(1, t+1):
        blindfold_bullseye(a, b)


if __name__ == "__main__":
    main()
