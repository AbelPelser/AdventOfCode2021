from util import *


def part1():
    lines = read_input_as_lines()
    for y in range(len(lines)):
        lines[y] = list(lines[y])

    n_steps = 0
    loop = True
    while loop:
        loop = False

        new_lines = [['.' for x in range(len(lines[y]))] for y in range(len(lines))]
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '>':
                    new_x = (x + 1) % len(lines[y])
                    if lines[y][new_x] in ('v', '>'):
                        new_lines[y][x] = lines[y][x]
                    else:
                        loop = True
                        new_lines[y][new_x] = lines[y][x]
                elif lines[y][x] == 'v':
                    new_lines[y][x] = lines[y][x]
        lines = new_lines
        new_lines = [['.' for x in range(len(lines[y]))] for y in range(len(lines))]
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == 'v':
                    new_y = (y + 1) % len(lines)
                    if lines[new_y][x] in ('v', '>'):
                        new_lines[y][x] = lines[y][x]
                    else:
                        loop = True
                        new_lines[new_y][x] = lines[y][x]
                elif lines[y][x] == '>':
                    new_lines[y][x] = lines[y][x]
        lines = new_lines
        n_steps += 1
    return n_steps


def part2():
    return 0


if __name__ == '__main__':
    print(part1())
    print(part2())
