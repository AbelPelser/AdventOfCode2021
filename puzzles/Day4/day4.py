from util import *


def calculate_score(board_numbers, board_drawn, last_n):
    print(board_drawn)
    print(board_numbers)
    print(last_n)
    sum = 0
    for y, row in enumerate(board_numbers):
        for x, number in enumerate(row):
            if not board_drawn[y][x]:
                sum += number
    print(sum)
    return sum * last_n


def check_col(board_drawn, x):
    for row in board_drawn:
        if row[x] is False:
            return False
    return True


def part1():
    lines = read_input().split('\n')
    to_draw = [int(i) for i in lines[0].split(',')]
    boards_drawn = []
    boards_numbers = []
    for line in lines[1:]:
        if line.strip() == '' or len(boards_drawn) == 0:
            boards_drawn.append([])
            boards_numbers.append([])
        else:
            boards_numbers[-1].append([int(n.strip()) for n in line.split(' ') if n.strip() != ''])
            boards_drawn[-1].append([False, False, False, False, False])
    print(boards_numbers)
    for n in to_draw:
        for i, board_numbers in enumerate(boards_numbers):
            for y, row in enumerate(board_numbers):
                for x, number in enumerate(row):
                    if number == n:
                        boards_drawn[i][y][x] = True
                        if all(boards_drawn[i][y]):
                            return calculate_score(boards_numbers[i], boards_drawn[i], n)
                        if check_col(boards_drawn[i], x):
                            return calculate_score(boards_numbers[i], boards_drawn[i], n)



def part2():
    lines = read_input().split('\n')
    to_draw = [int(i) for i in lines[0].split(',')]
    boards_drawn = []
    boards_numbers = []
    boards_won = []
    for line in lines[1:]:
        if line.strip() == '' or len(boards_drawn) == 0:
            boards_drawn.append([])
            boards_numbers.append([])
        else:
            boards_numbers[-1].append([int(n.strip()) for n in line.split(' ') if n.strip() != ''])
            boards_drawn[-1].append([False, False, False, False, False])
    print(boards_numbers)
    for n in to_draw:
        for i, board_numbers in enumerate(boards_numbers):
            if board_numbers in boards_won:
                continue
            for y, row in enumerate(board_numbers):
                for x, number in enumerate(row):
                    if number == n:
                        boards_drawn[i][y][x] = True
                        win = all(boards_drawn[i][y]) or check_col(boards_drawn[i], x)
                        if win:
                            boards_won.append(boards_numbers[i])
                            if len(boards_won) == len(boards_numbers) - 1:
                                return calculate_score(boards_numbers[i], boards_drawn[i], n)
    print(len(boards_won), len(boards_numbers))


if __name__ == '__main__':
    print(part1())
    print(part2())
