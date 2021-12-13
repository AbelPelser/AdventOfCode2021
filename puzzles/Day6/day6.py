from util import *


def parse_input():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))
    fish_per_timer_value = [0] * 9
    for n in numbers:
        fish_per_timer_value[n] += 1
    return fish_per_timer_value


def simulate_lanternfish(fish_per_timer_value, n_steps):
    for _ in range(n_steps):
        new_fish_per_timer_value = [0] * 9
        for timer in range(9):
            new_fish_per_timer_value[timer] = fish_per_timer_value[(timer + 1) % 9]
        new_fish_per_timer_value[6] += fish_per_timer_value[0]
        fish_per_timer_value = new_fish_per_timer_value
    return sum(fish_per_timer_value)


def part1():
    return simulate_lanternfish(parse_input(), 80)


def part2():
    return simulate_lanternfish(parse_input(), 256)


if __name__ == '__main__':
    print(part1())
    print(part2())
