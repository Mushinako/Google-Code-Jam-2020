#!/usr/bin/env python3
import sys


def query(data):
    print(data, flush=True)
    judge_response = input()
    # debug_print(' *quer: {}'.format(data))
    # debug_print(' *judg: {}'.format(judge_response))
    if judge_response == 'N':
        sys.exit(-1)
    if judge_response == 'Y':
        return True
    return int(judge_response)


def quantum_check(data, same_pointer, opposite_pointer, b):
    if same_pointer == -1:
        # If no same existed yet, bit filps and reversing have the same effect
        # Check opposite, as it must exist
        datum_opposite = query(opposite_pointer + 1)
        if datum_opposite != data[opposite_pointer]:
            data.reverse()
        # Waste 1 query as I want to keep query_count even
        query(1)
    else:
        # If same changes, bits must have flipped
        datum_same = query(same_pointer + 1)
        if datum_same != data[same_pointer]:
            for i in range(b):
                if data[i] != -1:
                    data[i] ^= 1
        # If no opposite existed yet, reversing have no effect
        if opposite_pointer == -1:
            # Waste 1 query as I want to keep query_count even
            query(1)
        else:
            # If opposite still don't match, the data must have been reversed
            datum_opposite = query(opposite_pointer + 1)
            if datum_opposite != data[opposite_pointer]:
                data.reverse()
    return data


# def debug_print(*args):
#     print(*args, file=sys.stderr)


def main():
    t, b = [int(x) for x in input().split()]
    for i in range(1, t+1):
        data = [-1] * b
        same_pointer = opposite_pointer = -1
        new_data_pointer = 0
        query_count = 0
        while -1 in data:
            # debug_print(' -data: {}'.format(data))
            # debug_print(' -same: {}'.format(same_pointer))
            # debug_print(' -oppo: {}'.format(opposite_pointer))
            # debug_print(' -qcnt: {}'.format(query_count))
            if query_count % 10 or not query_count:
                # Not quantum fluctuation round
                datum_1 = query(new_data_pointer + 1)
                data[new_data_pointer] = datum_1
                tmp_data_pointer = b - new_data_pointer - 1
                datum_2 = query(tmp_data_pointer + 1)
                data[tmp_data_pointer] = datum_2
                if datum_1 == datum_2:
                    if same_pointer == -1:
                        same_pointer = new_data_pointer
                else:
                    if opposite_pointer == -1:
                        opposite_pointer = new_data_pointer
                new_data_pointer += 1
                query_count += 2
            else:
                # Quantum fluctuation!
                data = quantum_check(data, same_pointer, opposite_pointer, b)
                query_count += 2
        final = query(''.join((str(x) for x in data)))
        # debug_print('\n')
        if final:
            continue


if __name__ == '__main__':
    result = main()
