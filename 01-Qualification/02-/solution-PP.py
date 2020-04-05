#!/usr/bin/env python3
def main():
    t = int(input())
    for i in range(1, t+1):
        s = input()
        for j in range(1, 10):
            s = s.replace(str(j), '(' * j + str(j) + ')' * j)
        while True:
            s_next = s.replace(')(', '')
            if s_next == s:
                break
            s = s_next
        print('Case #{0}: {1}'.format(i, s))


if __name__ == '__main__':
    result = main()
