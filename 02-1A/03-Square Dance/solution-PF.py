#!/usr/bin/env python3
class Competitor:
    def __init__(self, skill):
        self.skill = skill
        self.north = self.south = self.west = self.east = None

    def get_neighbors(self, row, col, max_row, max_col, board):
        if row > 0:
            self.north = board[row - 1][col]
        if row < max_row:
            self.south = board[row + 1][col]
        if col > 0:
            self.west = board[row][col - 1]
        if col < max_col:
            self.east = board[row][col + 1]

    def is_eliminated(self):
        skills = [comp.skill for comp in (
            self.north, self.south, self.west, self.east) if comp is not None]
        if len(skills) == 0:
            return False
        else:
            return self.skill < (sum(skills) / len(skills))

    def remove(self):
        if self.north is not None:
            self.north.south = self.south
        if self.south is not None:
            self.south.north = self.north
        if self.west is not None:
            self.west.east = self.east
        if self.east is not None:
            self.east.west = self.west


def run_round(board):
    skill_sum = 0
    for row in board:
        for cell in row:
            if cell is None:
                continue
            skill_sum += cell.skill
    eliminated = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell is None:
                continue
            if cell.is_eliminated():
                eliminated.append((r, c))
    for r, c in eliminated:
        board[r][c].remove()
        board[r][c] = None
    return skill_sum, len(eliminated)


def square_dance(skill_board):
    board = [[Competitor(skill) for skill in row] for row in skill_board]
    max_row = len(board) - 1
    max_col = len(board[0]) - 1
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell is None:
                continue
            cell.get_neighbors(r, c, max_row, max_col, board)
    interest_level = 0
    while True:
        skill_sum, num_eliminated = run_round(board)
        interest_level += skill_sum
        if num_eliminated == 0:
            break
    return interest_level


def main():
    t = int(input())
    for case in range(1, t + 1):
        r = int(input().split()[0])
        skill_board = [[int(x) for x in input().split()] for _ in range(r)]
        interest_level = square_dance(skill_board)
        print("Case #{0}: {1}".format(case, interest_level))


if __name__ == "__main__":
    main()
