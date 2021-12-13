from util import *


def parse_input():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))
    n_fish_per_timer_value = [0] * 9
    for n in numbers:
        n_fish_per_timer_value[n] += 1
    return n_fish_per_timer_value


def simulate_lanternfish(n_fish_per_timer_value, n_steps):
    for _ in range(n_steps):
        next_n_fish_per_timer_value = [0] * 9
        for timer in range(9):
            next_n_fish_per_timer_value[timer] = n_fish_per_timer_value[(timer + 1) % 9]
        next_n_fish_per_timer_value[6] += n_fish_per_timer_value[0]
        n_fish_per_timer_value = next_n_fish_per_timer_value
    return sum(n_fish_per_timer_value)


def part1():
    return simulate_lanternfish(parse_input(), 80)


def part2():
    return simulate_lanternfish(parse_input(), 256)


if __name__ == '__main__':
    print(part1())
    print(part2())
