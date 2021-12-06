from util import *


def part1():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))
    # numbers = list(map(int, '3,4,3,1,2'.split(',')))
    for d in range(80):
        print(d)
        for i in range(len(numbers)):
            if numbers[i] > 0:
                numbers[i] -= 1
            elif numbers[i] == 0:
                numbers[i] = 6
                numbers.append(8)
    return len(numbers)


def part2():
    lines = read_input_as_lines()
    numbers = list(map(int, lines[0].split(',')))
    amounts_per_numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for n in numbers:
        amounts_per_numbers[n] += 1
    for d in range(256):
        new_amounts_per_numbers = {}
        new_amounts_per_numbers[0] = amounts_per_numbers[1]
        new_amounts_per_numbers[1] = amounts_per_numbers[2]
        new_amounts_per_numbers[2] = amounts_per_numbers[3]
        new_amounts_per_numbers[3] = amounts_per_numbers[4]
        new_amounts_per_numbers[4] = amounts_per_numbers[5]
        new_amounts_per_numbers[5] = amounts_per_numbers[6]
        new_amounts_per_numbers[6] = amounts_per_numbers[7] + amounts_per_numbers[0]
        new_amounts_per_numbers[7] = amounts_per_numbers[8]
        new_amounts_per_numbers[8] = amounts_per_numbers[0]
        amounts_per_numbers = new_amounts_per_numbers
    print(amounts_per_numbers)
    return sum(amounts_per_numbers.values())


if __name__ == '__main__':
    print(part1())
    print(part2())
