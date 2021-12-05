from util import *


def count_bits_for_position(lines, position):
    counter = {0: 0, 1: 0}
    for line in lines:
        counter[int(line[position])] += 1
    return counter


def count_bits_for_all_positions(lines):
    return [count_bits_for_position(lines, pos) for pos in range(len(lines[0]))]


def part1():
    counts = count_bits_for_all_positions(read_input_as_lines())
    gamma = 0
    epsilon = 0
    for counts_for_position in counts:
        gamma <<= 1
        epsilon <<= 1
        if counts_for_position[0] > counts_for_position[1]:
            epsilon += 1
        else:
            gamma += 1
    return gamma * epsilon


def extract_value_by_bit_criterium(values, invert=False):
    bit_index = 0
    while len(values) > 1:
        counter = count_bits_for_position(values, bit_index)
        target_bit = 0 if counter[0] > counter[1] else 1
        if invert:
            target_bit = 1 - target_bit
        values = [p for p in values if int(p[bit_index]) == target_bit]
        bit_index += 1
    return int(values[0], 2)


def part2():
    lines = read_input_as_lines()
    oxygen = extract_value_by_bit_criterium(lines[:])
    co2_scrubber = extract_value_by_bit_criterium(lines[:], invert=True)
    return co2_scrubber * oxygen


if __name__ == '__main__':
    print(part1())
    print(part2())
