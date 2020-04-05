#!/usr/bin/env python3
def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        raw_activities = [[int(x) for x in input().split()] for _ in range(n)]
        activities = sorted(enumerate(raw_activities), key=lambda act: act[1])
        c_end = j_end = 0
        schecule = [''] * len(raw_activities)
        for num_act in activities:
            num, act = num_act
            if act[0] >= c_end:
                schecule[num] = 'C'
                c_end = act[1]
            elif act[0] >= j_end:
                schecule[num] = 'J'
                j_end = act[1]
            else:
                schecule = ['IMPOSSIBLE']
                break
        print('Case #{0}: {1}'.format(i, ''.join(schecule)))


if __name__ == '__main__':
    result = main()
