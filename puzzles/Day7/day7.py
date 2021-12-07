from util import *


def cost_part2(a, b):
    c = 0
    for i in range(1, abs(a - b) + 1):
        c += i
    return c


def part1():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))

    best_cost = None
    for n in range(min(numbers), max(numbers)):
        cost = 0
        for number in numbers:
            cost += abs(n - number)
        if best_cost is None or cost < best_cost:
            best_cost = cost
    return best_cost


def part2():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))

    best_cost = None
    for n in range(min(numbers), max(numbers)):
        cost = 0
        for number in numbers:
            cost += cost_part2(n, number)
        if best_cost is None or cost < best_cost:
            best_cost = cost
    return best_cost


if __name__ == '__main__':
    print(part1())
    print(part2())
