from util import read_input_as_lines, read_input_as_numbers

import re

def part1():
    lines = read_input_as_lines()
    depth = 0
    pos = 0
    for l in lines:

        if l.startswith('forward '):
            pos += int(l[8:])
        elif l.startswith('down '):
            depth += int(l[5:])
        elif l.startswith('up '):
            depth -= int(l[3:])
    return pos * depth


def part2():
    lines = read_input_as_lines()
    aim = 0
    pos = 0
    depth = 0
    for l in lines:
        if l.startswith('forward '):
            val = int(l[8:])
            pos += val
            depth += aim * val
        elif l.startswith('down '):
            aim += int(l[5:])
        elif l.startswith('up '):
            aim -= int(l[3:])
    return pos * depth


if __name__ == '__main__':
    print(part1())
    print(part2())
