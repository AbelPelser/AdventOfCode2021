from collections import defaultdict

from util import *


def parse_input():
    lines = read_input_as_lines()
    for line in lines:
        coord_a, coord_b = line.split(' -> ')
        a_x, a_y = coord_a.split(',')
        b_x, b_y = coord_b.split(',')
        yield (int(a_x), int(a_y)), (int(b_x), int(b_y))


def get_step_delta(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    return -1


def get_steps_inclusive(a_x, a_y, b_x, b_y):
    d_x = get_step_delta(a_x, b_x)
    d_y = get_step_delta(a_y, b_y)
    b_x += d_x
    b_y += d_y
    while not (a_x == b_x and a_y == b_y):
        yield a_x, a_y
        a_x += d_x
        a_y += d_y


def get_n_doubly_covered_points(include_diagonals=False):
    covered = defaultdict(int)
    for (a_x, a_y), (b_x, b_y) in parse_input():
        if a_x == b_x or a_y == b_y or include_diagonals:
            for x, y in get_steps_inclusive(a_x, a_y, b_x, b_y):
                covered[(x, y)] += 1
    return len({s for s in covered.keys() if covered[s] > 1})


def part1():
    return get_n_doubly_covered_points()


def part2():
    return get_n_doubly_covered_points(include_diagonals=True)


if __name__ == '__main__':
    print(part1())
    print(part2())
