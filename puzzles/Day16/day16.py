from util import *


def evaluate_packet(bit_str):
    type_id = int(bit_str[3:6], 2)
    i = 6
    if type_id == 4:
        groups = []
        while i < len(bit_str):
            stop_bit = bit_str[i]
            groups.append(bit_str[i + 1:i + 5])
            i += 5
            if stop_bit == '0':
                v = int(''.join(groups), 2)
                return v, i
    else:
        length_type_id = bit_str[6]
        sub_values = []
        if length_type_id == '0':
            n_bits_for_subpackets = int(bit_str[7:22], 2)
            i = 22
            while i < n_bits_for_subpackets + 22:
                sub_value, sub_i = evaluate_packet(bit_str[i:])
                sub_values.append(sub_value)
                i += sub_i
        else:
            n_subpackets_contained = int(bit_str[7:18], 2)
            i = 18
            for _ in range(n_subpackets_contained):
                sub_value, sub_i = evaluate_packet(bit_str[i:])
                sub_values.append(sub_value)
                i += sub_i
        if type_id == 0:
            return sum(sub_values), i
        elif type_id == 1:
            return mult(sub_values), i
        elif type_id == 2:
            return min(sub_values), i
        elif type_id == 3:
            return max(sub_values), i
        elif type_id == 5:
            if sub_values[0] > sub_values[1]:
                return 1, i
            else:
                return 0, i
        elif type_id == 6:
            if sub_values[0] < sub_values[1]:
                return 1, i
            else:
                return 0, i
        elif type_id == 7:
            if sub_values[0] == sub_values[1]:
                return 1, i
            else:
                return 0, i


def decode_version_sum(bit_str):
    version = int(bit_str[:3], 2)
    type_id = int(bit_str[3:6], 2)
    i = 6
    if type_id == 4:
        groups = []
        while i < len(bit_str):
            stop_bit = bit_str[i]
            groups.append(int(bit_str[i + 1:i + 5], 2))
            i += 5
            if stop_bit == '0':
                break
        return version, i
    else:
        sum_of_versions = version
        length_type_id = bit_str[6]
        if length_type_id == '0':
            n_bits_for_subpackets = int(bit_str[7:22], 2)
            i = 22
            while i < n_bits_for_subpackets + 22:
                subsum, sub_i = decode_version_sum(bit_str[i:])
                sum_of_versions += subsum
                i += sub_i
            return sum_of_versions, i
        else:
            n_subpackets_contained = int(bit_str[7:18], 2)
            i = 18
            for _ in range(n_subpackets_contained):
                subsum, sub_i = decode_version_sum(bit_str[i:])
                sum_of_versions += subsum
                i += sub_i
            return sum_of_versions, i


def part1():
    lines = read_input_as_lines()
    line = lines[0]
    bit_str = turn_into_bit_str(line)
    return decode_version_sum(bit_str)[0]


def turn_into_bit_str(line):
    bit_data = []
    for c in list(line):
        value = int(c, 16)
        bits = bin(value)[2:].rjust(4, '0')
        bit_data.append(bits)
    return ''.join(bit_data)


def part2():
    lines = read_input_as_lines()
    line = lines[0]
    bit_str = turn_into_bit_str(line)
    return evaluate_packet(bit_str)[0]


if __name__ == '__main__':
    print(part1())
    print(part2())
