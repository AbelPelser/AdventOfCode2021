from util import *



def part1():
    lines = read_input_as_lines()
    count = 0
    for line in lines:
        a = line.split('|')[1]
        b = remove_empty(a.split(' '))
        for c in b:
            if len(c) in (2, 4, 3, 7):
                count += 1
    return count


positions = {

}


def part2():
    lines = read_input_as_lines()
    count = 0
    for line in lines:
        patterns, output_value = line.split('|')
        patterns_split = [''.join(sorted(x)) for x in remove_empty(patterns.split(' '))]
        output_value_split = [''.join(sorted(x)) for x in remove_empty(output_value.split(' '))]
        patterns_to_digits = {}
        digits_to_patterns = {}
        for pattern in patterns_split:
            if len(pattern) == 2:
                patterns_to_digits[pattern] = 1
                digits_to_patterns[1] = pattern
            elif len(pattern) == 3:
                patterns_to_digits[pattern] = 7
                digits_to_patterns[7] = pattern
            elif len(pattern) == 4:
                patterns_to_digits[pattern] = 4
                digits_to_patterns[4] = pattern
            elif len(pattern) == 7:
                patterns_to_digits[pattern] = 8
                digits_to_patterns[8] = pattern
        for pattern in patterns_split:
            if len(pattern) == 5 and all([x in pattern for x in digits_to_patterns[7]]):
                patterns_to_digits[pattern] = 3
                digits_to_patterns[3] = pattern
        for pattern in patterns_split:
            if len(pattern) == 6 and all([x in pattern for x in digits_to_patterns[3]]):
                patterns_to_digits[pattern] = 9
                digits_to_patterns[9] = pattern
        letter_only_missing_in_2 = None
        for letter in list('abcdefg'):
            if len([r for r in patterns_split if letter in r]) == 9:
                letter_only_missing_in_2 = letter
        for pattern in patterns_split:
            if len(pattern) == 5 and letter_only_missing_in_2 not in pattern:
                patterns_to_digits[pattern] = 2
                digits_to_patterns[2] = pattern
        for pattern in patterns_split:
            if len(pattern) == 5 and pattern not in patterns_to_digits.keys():
                patterns_to_digits[pattern] = 5
                digits_to_patterns[5] = pattern
        for pattern in patterns_split:
            if len(pattern) == 6 and all([x in pattern for x in digits_to_patterns[7]]) and pattern not in patterns_to_digits.keys():
                patterns_to_digits[pattern] = 0
                digits_to_patterns[0] = pattern
        for pattern in patterns_split:
            if len(pattern) == 6 and pattern not in patterns_to_digits.keys():
                patterns_to_digits[pattern] = 6
                digits_to_patterns[6] = pattern
        number = ''
        for output in output_value_split:
            digit = str(patterns_to_digits[output])
            number += digit
        count += int(number)
    return count


if __name__ == '__main__':
    print(part1())
    print(part2())
