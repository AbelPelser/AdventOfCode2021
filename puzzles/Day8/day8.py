from str_util import extract_letter_frequencies, sorted_str
from util import *
from util import read_input_as_lines


def parse_line(line):
    patterns, output_value = line.split('|')
    patterns_split = [sorted_str(x) for x in remove_empty(patterns.split())]
    output_value = [sorted_str(x) for x in remove_empty(output_value.split())]
    return patterns_split, output_value


def part1():
    lines = read_input_as_lines()
    count = 0
    for line in lines:
        _, output_value = parse_line(line)
        count += len([o for o in output_value if len(o) in (2, 3, 4, 7)])
    return count


def part2():
    # Can be determined by hand, or not
    sorted_frequencies_to_digits = {
        (4, 6, 7, 8, 8, 9): 0,
        (8, 9): 1,
        (4, 7, 7, 8, 8): 2,
        (7, 7, 8, 8, 9): 3,
        (6, 7, 8, 9): 4,
        (6, 7, 7, 8, 9): 5,
        (4, 6, 7, 7, 8, 9): 6,
        (8, 8, 9): 7,
        (4, 6, 7, 7, 8, 8, 9): 8,
        (6, 7, 7, 8, 8, 9): 9
    }

    lines = read_input_as_lines()
    count = 0
    for line in lines:
        patterns_split, output_value_split = parse_line(line)
        patterns_to_digits = {}
        letters_to_frequencies = extract_letter_frequencies(''.join(patterns_split))

        for pattern in patterns_split:
            sorted_frequencies = tuple(sorted([letters_to_frequencies[c] for c in pattern]))
            patterns_to_digits[pattern] = sorted_frequencies_to_digits[sorted_frequencies]
        digits_as_str = (str(patterns_to_digits[o]) for o in output_value_split)
        count += int(''.join(digits_as_str))
    return count


if __name__ == '__main__':
    print(part1())
    print(part2())
