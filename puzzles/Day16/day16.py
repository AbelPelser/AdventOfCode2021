from puzzles.Day16.interpreters import InterpreterWithIndex, InterpreterWithStringConsumption
from util import *
from util import convert_hex_into_bit_string


class VersionSumInterpreter(InterpreterWithIndex):
    def __init__(self, command_bit_string):
        super(VersionSumInterpreter, self).__init__(command_bit_string)
        self.version_sum = self.version

    def evaluate_subpacket(self):
        sub_interpreter = VersionSumInterpreter(self.bit_string[self.i:])
        value = sub_interpreter.evaluate()
        self.i += sub_interpreter.i
        self.version_sum += sub_interpreter.version_sum
        return value


def part1():
    line = read_input_as_lines()[0]
    bit_str = convert_hex_into_bit_string(line)
    interpreter = VersionSumInterpreter(bit_str)
    interpreter.evaluate()
    return interpreter.version_sum


def part2():
    line = read_input_as_lines()[0]
    bit_str = convert_hex_into_bit_string(line)
    return InterpreterWithStringConsumption(bit_str).evaluate()


if __name__ == '__main__':
    print(part1())
    print(part2())
