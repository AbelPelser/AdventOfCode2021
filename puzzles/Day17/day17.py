from collections import defaultdict

from util import *


def test(start_x, start_y, x_from, x_to, y_from, y_to):
    x = 0
    y = 0
    v_x = start_x
    v_y = start_y
    in_target = False
    max_height = None
    while True:
        x += v_x
        y += v_y
        if max_height is None or y > max_height:
            max_height = y
        if v_x < 0:
            v_x += 1
        elif v_x > 0:
            v_x -= 1
        v_y -= 1
        if x_from <= x <= x_to and y_from <= y <= y_to:
            in_target = True
        if (v_y < 0 and y < y_from and y < y_to):
            return in_target, max_height


def sweep_x(start_x, start_y, x_from, x_to, y_from, y_to):
    has_been_in_target = False
    max_y = None

    for i in range(100):
        in_target, max_height = test(start_x + i, start_y, x_from, x_to, y_from, y_to)
        if in_target:
            has_been_in_target = True
            if max_y is None or max_height > max_y:
                max_y = max_height
        if (not in_target) and has_been_in_target:
            return max_y, start_x + i
        in_target, max_height = test(start_x - i, start_y, x_from, x_to, y_from, y_to)
        if in_target:
            has_been_in_target = True
            if max_y is None or max_height > max_y:
                max_y = max_height
        if (not in_target) and has_been_in_target:
            return max_y, start_x - i
    return max_y, start_x + 1


def sweep_y(start_x, start_y, x_from, x_to, y_from, y_to):
    has_been_in_target = False
    max_y = None

    for i in range(100):
        in_target, max_height = test(start_x, start_y + i, x_from, x_to, y_from, y_to)
        if in_target:
            has_been_in_target = True
            if max_y is None or max_height > max_y:
                max_y = max_height
        if (not in_target) and has_been_in_target:
            return max_y, start_y + i
        in_target, max_height = test(start_x, start_y - i, x_from, x_to, y_from, y_to)
        if in_target:
            has_been_in_target = True
            if max_y is None or max_height > max_y:
                max_y = max_height
        if (not in_target) and has_been_in_target:
            return max_y, start_y - i
    return max_y, start_x + 1


def part1():
    line = read_input_as_lines()[0]
    # line = 'target area: x=20..30, y=-10..-5'
    target_x_from = int(line.split('target area: x=')[1].split('..')[0])
    target_x_to = int(line.split('target area: x=')[1].split('..')[1].split(', ')[0])
    target_y_from = int(line.split('y=')[1].split('..')[0])
    target_y_to = int(line.split('y=')[1].split('..')[1])

    max_y = None
    # start_x = 1
    # start_y = 1
    #
    # change = True
    # while change or max_y is None:
    #     change = False
    #     max_height, start_x = sweep_x(start_x, start_y, target_x_from, target_x_to, target_y_from, target_y_to)
    #     if max_height is not None and (max_y is None or max_height > max_y):
    #         max_y = max_height
    #         change = True
    #     max_height, start_y = sweep_y(start_x, start_y, target_x_from, target_x_to, target_y_from, target_y_to)
    #     if max_height is not None and (max_y is None or max_height > max_y):
    #         max_y = max_height
    #         change = True
    best = None
    for v_x in range(200):
        for v_y in range(-150, 500):
            in_target, max_height = test(v_x, v_y, target_x_from, target_x_to, target_y_from, target_y_to)
            if in_target:
                if max_y is None or max_height > max_y:
                    max_y = max_height
                    best = (v_x, v_y)
    print(best)
    return max_y


def reverse_from_target_point(start_x, start_y):
    x = start_x
    y = start_y
    v_x = 0
    v_y = 0
    while True:
        if x == 0 and y == 0:
            return -v_x, -v_y
        v_y += 1
        if x < 0:
            v_x -= 1
        elif x > 0:
            v_x += 1
        y += v_y
        x += v_x
        if (start_x > 0 and x < 0) or (start_x < 0 and x > 0) or \
                (start_y > 0 and y < 0) or (start_y < 0 and y > 0):
            return None, None


def startx_works_for_target(start_x, x_from, x_to):
    x = 0
    v_x = start_x
    if start_x == 0 and not (x_from < 0 < x_to):
        return False, -1
    if x_from > 0 and x_to > 0 and start_x < 0:
        return False, -1
    if x_from < 0 and x_to < 0 and start_x > 0:
        return False, -1
    n_steps = 0
    while True:
        n_steps += 1
        x += v_x
        if v_x < 0:
            v_x += 1
        elif v_x > 0:
            v_x -= 1
        if x_from <= x <= x_to:
            return True, n_steps
        elif v_x == 0:
            return False, -1
        if (0 > x_from > x and 0 > x_to > x) or \
                (0 < x_from < x and 0 < x_to < x):
            return False, -1


def get_y_for_start_y_and_steps(start_y, n_steps):
    y = 0
    v_y = start_y
    for _ in range(n_steps):
        y += v_y
        v_y -= 1
    return y


def part2():
    line = read_input_as_lines()[0]
    # line = 'target area: x=20..30, y=-10..-5'
    # target_x_from = int(line.split('target area: x=')[1].split('..')[0])
    # target_x_to = int(line.split('target area: x=')[1].split('..')[1].split(', ')[0])
    # target_y_from = int(line.split('y=')[1].split('..')[0])
    # target_y_to = int(line.split('y=')[1].split('..')[1])
    target_x_from = 56
    target_x_to = 76
    target_y_from = -162
    target_y_to = -134

    # for point_x in range(target_x_from, target_x_to + 1):
    #     for point_y in range(target_y_from, target_y_to + 1):
    #         print(reverse_from_target_point(point_x, point_y))
    steps_per_v_x_that_work = defaultdict(list)
    for v_x in range(77):
        for target_x in range(min((target_x_to, target_x_from)), max((target_x_to, target_x_from)) + 1):
            works, steps = startx_works_for_target(v_x, target_x, target_x)
            if works:
                steps_per_v_x_that_work[v_x].append(steps)
    print(steps_per_v_x_that_work)

    works = []
    for v_x in steps_per_v_x_that_work.keys():
        for v_y in range(-165, 1000):
            if v_y % 100 == 0:
                print(v_y)
            in_target, max_height = test(v_x, v_y, target_x_from, target_x_to, target_y_from, target_y_to)
            if in_target:
                works.append((v_x, v_y))
    print(sorted(works))
    return len(works)


if __name__ == '__main__':
    # print(part1())
    print(part2())
