from util import *


class Board:
    def __init__(self, lines):
        self.numbers = []
        self.drawn = []
        for line in remove_empty(lines):
            number_strings = remove_empty(line.split(' '))
            self.numbers.append(list(map(int, number_strings)))
            self.drawn.append([False] * len(self.numbers[-1]))

    def draw(self, number):
        won = False
        for y, row in enumerate(self.numbers):
            if number in row:
                x = row.index(number)
                self.drawn[y][x] = True
                won = all(self.drawn[y]) or all([row[x] for row in self.drawn])
        if won:
            return self.calculate_score(number)
        return None

    def calculate_score(self, last_drawn):
        return last_drawn * sum([
            self.numbers[y][x]
            for y in range(len(self.numbers))
            for x in range(len(self.numbers[y]))
            if not self.drawn[y][x]
        ])


def parse_input():
    to_draw_str, text = read_input().split('\n', 1)
    to_draw = list(map(int, to_draw_str.split(',')))
    boards = []
    for board_str in text.split('\n\n'):
        boards.append(Board(board_str.split('\n')))
    return to_draw, boards


def part1():
    to_draw, boards = parse_input()
    for number in to_draw:
        for board in boards:
            result = board.draw(number)
            if result is not None:
                return result


def part2():
    to_draw, boards = parse_input()
    boards_won = set()
    for number in to_draw:
        for board in boards:
            if board in boards_won:
                continue
            result = board.draw(number)
            if result is not None:
                boards_won.add(board)
                if len(boards_won) == len(boards):
                    return result


if __name__ == '__main__':
    print(part1())
    print(part2())
