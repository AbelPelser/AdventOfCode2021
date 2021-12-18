import math

from util import *

from copy import deepcopy


def split_number(number):
    return [math.floor(number / 2), math.ceil(number / 2)]


def add_numbers(a, b):
    return [a, b]


def explode_leftmost_suitable_pair(number, nest_level = 4, numbers_seen = 0):
    # 1) explodes the pair by replacing it by 0
    # 2) Returns the pair that exploded, followed by the index of said zero
    # returns None, numbers_seen if no explosion happened
    if isinstance(number, list):
        if nest_level <= 1:
            tmp_seen = numbers_seen
            for i in range(len(number)):
                if isinstance(number[i], list):
                    if isinstance(number[i][0], int) and isinstance(number[i][1], int):
                        result = number[i]
                        number[i] = 0
                        return result, tmp_seen
                else:
                    tmp_seen += 1
        for i in range(len(number)):
            if isinstance(number[i], list):
                result, numbers_seen = explode_leftmost_suitable_pair(number[i], nest_level=nest_level - 1, numbers_seen=numbers_seen)
                if result is not None:
                    return result, numbers_seen
            else:
                numbers_seen += 1
    return None, numbers_seen


def find_leftmost_10_or_greater(number):
    sub_numbers_in_number = eval(str(number).replace('[', '').replace(']', ''))
    for sub_number in sub_numbers_in_number:
        if sub_number >= 10:
            return sub_number


def add_digit_helper(number, to_add, index, numbers_seen=0):
    if isinstance(number, list):
        for i in range(len(number)):
            if isinstance(number[i], list):
                item, sub_numbers_seen, done = add_digit_helper(number[i], to_add, index, numbers_seen=numbers_seen)
                numbers_seen = sub_numbers_seen
                number[i] = item
                if done is True:
                    return number, numbers_seen, done
            else:
                if index == numbers_seen:
                    number[i] += to_add
                    return number, numbers_seen, True
                numbers_seen += 1
        return number, numbers_seen, False
    print(f'Not a list: {number}')
    return number, 0, False


def reduce_number(number):
    change = True
    while change:
        change = False
        number_str = str(number)
        number_flat = eval(number_str.replace('[', '').replace(']', ''))

        exploded_pair, i = explode_leftmost_suitable_pair(number)
        if exploded_pair is not None:
            add_digit_helper(number, exploded_pair[0], i - 1)
            add_digit_helper(number, exploded_pair[1], i + 1)
            change = True
            continue
        # split >=10
        split = False
        for sub_number in number_flat:
            if sub_number is None:
                raise ValueError(number_str + ' <> ' + str(number_flat))
            if sub_number >= 10:
                number_str = number_str.replace(str(sub_number), str(split_number(sub_number)), 1)
                number = eval(number_str)
                split = True
                change = True
                break
        if split:
            continue
    return number


def magnitude_of_pair(pair):
    if isinstance(pair[0], int):
        magnitude0 = 3 * pair[0]
    else:
        magnitude0 = 3 * magnitude_of_pair(pair[0])
    if isinstance(pair[1], int):
        magnitude1 = 2 * pair[1]
    else:
        magnitude1 = 2 * magnitude_of_pair(pair[1])

    return magnitude0 + magnitude1


def part1():
    lines = read_input_as_lines()
    snailfish_lines = []
    for line in lines:
        snailfish_lines.append(eval(line))
    while len(snailfish_lines) > 1:
        n = add_numbers(snailfish_lines[0], snailfish_lines[1])
        n = reduce_number(n)
        snailfish_lines = [n] + snailfish_lines[2:]
    return magnitude_of_pair(snailfish_lines[0])


def part2():
    lines = read_input_as_lines()
    snailfish_lines = []
    for line in lines:
        snailfish_lines.append(eval(line))
    best_magnitude = None
    for i in range(len(snailfish_lines)):
        for j in range(len(snailfish_lines)):
            if i == j:
                continue
            a = deepcopy(snailfish_lines[i])
            b = deepcopy(snailfish_lines[j])
            r = reduce_number(add_numbers(a, b))
            magnitude = magnitude_of_pair(r)
            if best_magnitude is None or magnitude > best_magnitude:
                best_magnitude = magnitude
    return best_magnitude


if __name__ == '__main__':
    print(part1())
    print(part2())
