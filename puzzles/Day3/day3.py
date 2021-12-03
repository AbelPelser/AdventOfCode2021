from collections import defaultdict

from util import *


def part1():
    lines = read_input_as_lines()
    counter = defaultdict(lambda: defaultdict(int))
    for line in lines:
        for i in range(len(line)):
            counter[i][line[i]] += 1
    gamma = ''
    epsilon = ''
    for i in range(12):
        if counter[i]['0'] > counter[i]['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print(gamma, epsilon)
    return int(gamma, 2) * int(epsilon, 2)


def count(lines):
    counter = defaultdict(lambda: defaultdict(int))
    for line in lines:
        for i in range(len(line)):
            counter[i][line[i]] += 1
    return counter


def part2():
    lines = read_input_as_lines()
    counter = count(lines)
    for line in lines:
        for i in range(len(line)):
            counter[i][line[i]] += 1

    possible_oxygen = lines[:]
    bit_i = 0
    while len(possible_oxygen) > 1:
        common_bit = '0' if counter[bit_i]['0'] > counter[bit_i]['1'] else '1'
        possible_oxygen = [p for p in possible_oxygen if p[bit_i] == common_bit]
        bit_i += 1
        counter = count(possible_oxygen)
    oxygen = int(possible_oxygen[0], 2)

    possible_co2 = lines[:]
    bit_i = 0
    while len(possible_co2) > 1:
        common_bit = '1' if counter[bit_i]['0'] > counter[bit_i]['1'] else '0'
        possible_co2 = [p for p in possible_co2 if p[bit_i] == common_bit]
        bit_i += 1
        counter = count(possible_co2)
    co2_scrubber = int(possible_co2[0], 2)
    return co2_scrubber * oxygen




if __name__ == '__main__':
    print(part1())
    print(part2())