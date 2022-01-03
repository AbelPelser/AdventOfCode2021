import operator

from puzzles.Day24.alu import ALU
from puzzles.Day24.z3_solver import Z3ConstraintGenerator
from util import *


def check_model_number_with_alu(lines, number):
    helper = ALU()
    padded_number = str(number).zfill(14)
    helper.run(lines, list(map(int, padded_number)))
    return helper.variables['z'] == 0


@cache
def simulate_alu(inp):
    secret_x = [13, 12, 12, 10, -11, -13, 15, 10, -2, -6, 14, 0, -15, -4]
    secret_y = [8, 13, 8, 10, 12, 1, 13, 5, 10, 3, 2, 2, 12, 7]
    z = 0
    suggestions = {}
    input_digits = string_to_digits(inp)
    for i, w in enumerate(input_digits):
        x = (z % 26) + secret_x[i]
        if i in (4, 5, 8, 9, 11, 12, 13):
            z //= 26
        if x != w:
            # Within this range, we could amend our input to make this check pass
            if 0 < x < 10:
                suggestions[i] = x
            z = (26 * z) + w + secret_y[i]
    return z, suggestions


def check_model_number_with_simulated_alu(number):
    z, _ = simulate_alu(number)
    return z == 0


@cache
def follow_suggestions(number_str):
    res, suggestions = simulate_alu(number_str)
    while len(suggestions) > 0:
        # Most significant digit first
        key = min(suggestions.keys())
        number_str = number_str[:key] + str(suggestions[key]) + number_str[key + 1:]
        res, suggestions = simulate_alu(number_str)
    return res, number_str


def bruteforce_digits(digit_indices, number_str, monad_comparator):
    best_z, _ = simulate_alu(number_str)
    best_number_str = number_str
    best_number_int = int(number_str)
    for i in range(1, 10):
        number_str = replace_item_in_list(number_str, digit_indices[0], i)
        for j in range(1, 10):
            number_str = replace_item_in_list(number_str, digit_indices[1], j)
            z, changed_number_str = follow_suggestions(number_str)
            changed_number_int = int(changed_number_str)

            if (best_z is None) or \
                    (best_z > 0 and z < best_z) or \
                    (best_z == 0 and z == 0 and monad_comparator(changed_number_int, best_number_int)):
                best_z = z
                best_number_str = changed_number_str
                best_number_int = int(best_number_str)
    return best_number_str


# monad_comparator: accepts two monads, keep the first if result is True, and the second otherwise
def bruteforce_optimal_nomad(monad_comparator):
    number = '9' * 14
    consecutive_digit_indices = [(i - 1, i) for i in range(1, 14)]
    loop = True
    while loop:
        # Sometimes multiple runs are needed
        prev_number = number
        for digit_indices in consecutive_digit_indices:
            number = bruteforce_digits(digit_indices, number, monad_comparator)
        loop = prev_number != number
    assert check_model_number_with_alu(read_input_as_lines(), number)
    return int(number)


def part1():
    return bruteforce_optimal_nomad(operator.gt)


def part1_z3():
    generator = Z3ConstraintGenerator()
    generator.add_monad_constraints(read_input_as_lines())
    return generator.find_max_monad()


def part2():
    return bruteforce_optimal_nomad(operator.lt)


def part2_z3():
    generator = Z3ConstraintGenerator()
    generator.add_monad_constraints(read_input_as_lines())
    return generator.find_min_monad()


if __name__ == '__main__':
    print(time_call(part1))
    print(time_call(part2))
    # print(time_call(part1_z3))
    print(time_call(part2_z3))
