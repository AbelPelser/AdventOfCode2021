from util import *


def parse_input():
    lines = read_input_as_lines()
    return list(map(int, lines[0].split(',')))


def find_minimum_cost(crab_positions, cost_function):
    best_cost = None
    for possible_alignment in range(min(crab_positions), max(crab_positions) + 1):
        cost = sum(cost_function(possible_alignment, n) for n in crab_positions)
        if best_cost is None or cost < best_cost:
            best_cost = cost
    return best_cost


def part1():
    return find_minimum_cost(parse_input(), lambda a, b: abs(a - b))


def cost_part2(a, b):
    abs_diff = abs(a - b)
    return (abs_diff * (abs_diff + 1)) // 2


def part2():
    return find_minimum_cost(parse_input(), cost_part2)


if __name__ == '__main__':
    print(part1())
    print(part2())
