from puzzles.util import replace_bit
from util import *


class ALU:
    def __init__(self):
        self.variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.input_counter = 0
        self.inputs = []

    def parse(self, line, op):
        target, operand = line.split(f'{op} ')[-1].split(' ')
        if operand in self.variables.keys():
            operand = self.variables[operand]
        return target, int(operand)

    def run(self, lines, inputs=None):
        if input is None:
            inputs = []
        self.inputs = inputs
        self.variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.input_counter = 0
        for line in lines:
            if line.startswith('inp'):
                var_name = line.split('inp ')[-1]
                value = self.input()
                self.variables[var_name] = value
                # exec(f'self.{var_name} = {value}')
            elif line.startswith('add'):
                target, operand = self.parse(line, 'add')
                self.variables[target] += operand
            elif line.startswith('mul'):
                target, operand = self.parse(line, 'mul')
                self.variables[target] *= operand
            elif line.startswith('div'):
                target, operand = self.parse(line, 'div')
                self.variables[target] //= operand
            elif line.startswith('mod'):
                target, operand = self.parse(line, 'mod')
                self.variables[target] %= operand
            elif line.startswith('eql'):
                target, operand = self.parse(line, 'eql')
                self.variables[target] = int(self.variables[target] == operand)
        return self.variables

    def input(self):
        res = self.inputs[self.input_counter]
        self.input_counter += 1
        return res


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


def follow_suggestions(n):
    res, suggestions = simulate_alu(n)
    while len(suggestions) > 0:
        # Change most significant digit first
        key = min(suggestions.keys())
        n = n[:key] + str(suggestions[key]) + n[key + 1:]
        res, suggestions = simulate_alu(n)
    return res, n


def sweep(bits, start_n, find_max=False):
    n = start_n
    best_res, _ = simulate_alu(n)
    best_n = n
    replace = bits
    for i in range(1, 10):
        n_ = replace_bit(n, replace[0], i)
        for j in range(1, 10):
            n_ = replace_bit(n_, replace[1], j)
            for k in range(1, 10):
                n_ = replace_bit(n_, replace[2], k)
                for l in range(1, 10):
                    n_ = replace_bit(n_, replace[3], l)
                    for m in range(1, 10):
                        n_ = replace_bit(n_, replace[4], m)
                        res, new_n = follow_suggestions(n_)
                        if best_res is None or (best_res != 0 and res < best_res):
                            best_res = res
                            best_n = str(new_n)
                        elif best_res == 0 and res == 0:
                            if find_max and int(new_n) > int(best_n):
                                best_res = res
                                best_n = str(new_n)
                            elif (not find_max) and int(new_n) < int(best_n):
                                best_res = res
                                best_n = str(new_n)
    return best_n




def part1():
    lines = read_input_as_lines()
    # res = check_model_number(lines, 2510000370204)
    # print(res)
    n = '9' * 14
    ranges = ((0, 1, 2, 3, 4), (3, 4, 5, 6, 7), (6, 7, 8, 9, 10), (9, 10, 11, 12, 13))
    for bit_range in ranges:
        n = sweep(bit_range, n, find_max=True)
    for bit_range in ranges:
        n = sweep(bit_range, n, find_max=True)
    assert check_model_number_with_alu(read_input_as_lines(), n)
    return int(n)


def part2():
    n = '9' * 14
    ranges = ((0, 1, 2, 3, 4), (3, 4, 5, 6, 7), (6, 7, 8, 9, 10), (9, 10, 11, 12, 13))
    for bit_range in ranges:
        n = sweep(bit_range, n)
    for bit_range in ranges:
        n = sweep(bit_range, n)
    assert check_model_number_with_alu(read_input_as_lines(), n)
    return int(n)


if __name__ == '__main__':
    print(part1())
    print(part2())
