from util import *


def increase_neighbours(lines_nr, x, y):
    if x > 0:
        lines_nr[y][x-1] += 1
        if y > 0:
            lines_nr[y-1][x-1] += 1
        if y < len(lines_nr) - 1:
            lines_nr[y+1][x-1] += 1
    if x < len(lines_nr[0]) - 1:
        lines_nr[y][x+1] += 1
        if y > 0:
            lines_nr[y-1][x+1] += 1
        if y < len(lines_nr) - 1:
            lines_nr[y+1][x+1] += 1
    if y > 0:
        lines_nr[y-1][x] += 1
    if y < len(lines_nr) - 1:
        lines_nr[y+1][x] += 1


def part1():
    lines = read_input_as_lines()
    lines_nr = []
    for l in lines:
        lines_nr.append([])
        for c in list(l):
            lines_nr[-1].append(int(c))

    n_flashes = 0
    for i in range(100):
        print(i)
        for y in range(len(lines_nr)):
            for x in range(len(lines_nr)):
                lines_nr[y][x] += 1
        flashed = False
        flashed_in_step = list()
        for y in range(len(lines_nr)):
            for x in range(len(lines_nr)):
                if lines_nr[y][x] > 9 and (x, y) not in flashed_in_step:
                    flashed_in_step.append((x, y))
                    increase_neighbours(lines_nr, x, y)
                    flashed = True
        while flashed:
            flashed = False
            for y in range(len(lines_nr)):
                for x in range(len(lines_nr)):
                    if lines_nr[y][x] > 9 and (x, y) not in flashed_in_step:
                        flashed_in_step.append((x, y))
                        increase_neighbours(lines_nr, x, y)
                        flashed = True
        n_flashes += len(flashed_in_step)
        for x, y in flashed_in_step:
            lines_nr[y][x] = 0
    return n_flashes


def part2():
    lines = read_input_as_lines()
    lines_nr = []
    for l in lines:
        lines_nr.append([])
        for c in list(l):
            lines_nr[-1].append(int(c))
    i = 0
    while True:
        for y in range(len(lines_nr)):
            for x in range(len(lines_nr)):
                lines_nr[y][x] += 1
        flashed = False
        flashed_in_step = list()
        for y in range(len(lines_nr)):
            for x in range(len(lines_nr)):
                if lines_nr[y][x] > 9 and (x, y) not in flashed_in_step:
                    flashed_in_step.append((x, y))
                    increase_neighbours(lines_nr, x, y)
                    flashed = True
        while flashed:
            flashed = False
            for y in range(len(lines_nr)):
                for x in range(len(lines_nr)):
                    if lines_nr[y][x] > 9 and (x, y) not in flashed_in_step:
                        flashed_in_step.append((x, y))
                        increase_neighbours(lines_nr, x, y)
                        flashed = True
        for x, y in flashed_in_step:
            lines_nr[y][x] = 0
        if len(flashed_in_step) == 100:
            return i + 1
        i += 1


if __name__ == '__main__':
    print(part1())
    print(part2())
