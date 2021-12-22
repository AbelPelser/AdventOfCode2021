import re
from collections import defaultdict

from util import *


def test(start_x, start_y, x_from, x_to, y_from, y_to):
    x = 0
    y = 0
    v_x = start_x
    v_y = start_y
    in_target = False
    max_height = None
    point_list = []
    while True:
        x += v_x
        y += v_y
        point_list.append((v_x, v_y))
        if max_height is None or y > max_height:
            max_height = y
        if v_x < 0:
            v_x += 1
        elif v_x > 0:
            v_x -= 1
        v_y -= 1
        if x_from <= x <= x_to and y_from <= y <= y_to:
            in_target = True
        if v_y < 0 and y < y_from and y < y_to:
            return in_target, max_height, point_list[:-1]


def get_possible_vx(x_from, x_to):
    v_x_that_work = set()
    for v_x in range(x_to + 1):
        for target_x in range(min((x_to, x_from)), max((x_to, x_from)) + 1):
            if start_v_x_reaches_target(v_x, target_x):
                v_x_that_work.add(v_x)
                break
    return v_x_that_work


def part1():
    x_from, x_to, y_from, y_to = parse_input(read_input_as_lines()[0])

    max_y = None
    for v_x in get_possible_vx(x_from, x_to):
        for v_y in range(min(y_from, y_to), abs(min(y_from, y_to))):
            in_target, max_height, _ = test(v_x, v_y, x_from, x_to, y_from, y_to)
            if in_target:
                if max_y is None or max_height > max_y:
                    max_y = max_height
    return max_y


def parse_input(line):
    boundaries_as_strings = re.match('target area: x=(-?\\d+)..(-?\\d+), y=(-?\\d+)..(-?\\d+)', line).groups()
    return tuple(map(int, boundaries_as_strings))


def start_v_x_reaches_target(v_x, target_x):
    x = 0
    if v_x <= 0 < target_x or target_x < 0 <= v_x:
        return False
    while v_x != 0 and not (x < target_x < 0 or 0 < target_x < x):
        x += v_x
        if v_x < 0:
            v_x += 1
        elif v_x > 0:
            v_x -= 1
        if x == target_x:
            return True
    return False


def start_v_y_reaches_target_from_above(v_y, y_from, y_to):
    y = 0
    while True:
        y += v_y
        v_y -= 1
        if y_from <= y <= y_to:
            return True
        if v_y < 0 and y < y_from and y < y_to:
            return False


def part2():
    x_from, x_to, y_from, y_to = parse_input(read_input_as_lines()[0])

    works = []
    for v_x in get_possible_vx(x_from, x_to):
        for v_y in range(min(y_from, y_to), abs(min(y_from, y_to))):
            in_target, _, point_list = test(v_x, v_y, x_from, x_to, y_from, y_to)
            if in_target:
                works.append((v_x, v_y, point_list))
    print(sorted(works))
    return len(works)


if __name__ == '__main__':
    print(part1())
    print(part2())
