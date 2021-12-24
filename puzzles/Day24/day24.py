from puzzles.Day24.alu import ALU
from puzzles.Day24.z3_solver import Z3ConstraintGenerator
from puzzles.util import replace_bit

from util import *


def check_model_number_with_alu(lines, number):
    helper = ALU()
    padded_number = str(number).zfill(14)
    helper.run(lines, list(map(int, padded_number)))
    return helper.variables['z'] == 0


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


def follow_suggestions(n):
    res, suggestions = simulate_alu(n)
    while len(suggestions) > 0:
        # Most significant digit first
        key = min(suggestions.keys())
        n = n[:key] + str(suggestions[key]) + n[key + 1:]
        res, suggestions = simulate_alu(n)
    return res, n


def bruteforce_digits_in_range(bits, start_n, find_max=False):
    n = start_n
    best_res, _ = simulate_alu(n)
    best_n = n
    replace = bits
    for i in range(1, 10):
        n_ = replace_bit(n, replace[0], i)
        for j in range(1, 10):
            n_ = replace_bit(n_, replace[1], j)
            res, new_n = follow_suggestions(n_)
            if best_res is None or (best_res != 0 and res < best_res):
                best_res = res
                best_n = str(new_n)
            elif best_res == 0 and res == 0:
                if find_max and int(new_n) > int(best_n):
                    best_res = res
                    best_n = str(new_n)
                elif not find_max and int(new_n) < int(best_n):
                    best_res = res
                    best_n = str(new_n)
    return best_n


def part1():
    n = '9' * 14
    ranges = [(i - 1, i) for i in range(1, 14)]
    loop = True
    while loop:
        prev_n = n
        for digit_range in ranges:
            n = bruteforce_digits_in_range(digit_range, n, find_max=True)
        loop = prev_n != n
    assert check_model_number_with_alu(read_input_as_lines(), n)
    return int(n)


def part1_z3():
    generator = Z3ConstraintGenerator()
    generator.add_monad_constraints(read_input_as_lines())
    return generator.find_max_monad()


def part2():
    n = '9' * 14
    ranges = [(i - 1, i) for i in range(1, 14)]
    loop = True
    while loop:
        prev_n = n
        for digit_range in ranges:
            n = bruteforce_digits_in_range(digit_range, n)
        loop = prev_n != n
    assert check_model_number_with_alu(read_input_as_lines(), n)
    return int(n)


def part2_z3():
    generator = Z3ConstraintGenerator()
    generator.add_monad_constraints(read_input_as_lines())
    return generator.find_min_monad()


if __name__ == '__main__':
    print(time_call(part1))
    print(time_call(part2))
    print(time_call(part1_z3))
    print(time_call(part2_z3))
