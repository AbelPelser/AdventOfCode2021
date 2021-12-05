import re

from util import read_input_as_lines


def parse_command(command):
    command, amount = re.match('([a-z]+) ([0-9]+)', command).groups()
    return command, int(amount)


def part1():
    lines = read_input_as_lines()
    depth = pos = 0
    for line in lines:
        action, amount = parse_command(line)
        if action == 'forward':
            pos += amount
        elif action == 'down':
            depth += amount
        elif action == 'up':
            depth -= amount
    return pos * depth


def part2():
    lines = read_input_as_lines()
    aim = pos = depth = 0
    for line in lines:
        action, amount = parse_command(line)
        if action == 'forward':
            pos += amount
            depth += aim * amount
        elif action == 'down':
            aim += amount
        elif action == 'up':
            aim -= amount
    return pos * depth


if __name__ == '__main__':
    print(part1())
    print(part2())
