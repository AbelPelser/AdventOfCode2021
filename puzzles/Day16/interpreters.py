from util import mult


class InterpreterWithIndex:
    def __init__(self, command_bit_string):
        self.bit_string = command_bit_string
        self.i = 0
        self.version = int(self.read_n_bits(3), 2)
        self.type_id = int(self.read_n_bits(3), 2)

    def read_n_bits(self, n_bits):
        result = self.bit_string[self.i:self.i + n_bits]
        self.i += n_bits
        return result

    def evaluate_literal(self):
        groups = []
        stop = False
        while not stop:
            stop = self.read_n_bits(1) == '0'
            groups.append(self.read_n_bits(4))
        return int(''.join(groups), 2)

    def evaluate_subpacket(self):
        sub_interpreter = InterpreterWithIndex(self.bit_string[self.i:])
        value = sub_interpreter.evaluate()
        self.i += sub_interpreter.i
        return value

    def evaluate_subpackets(self):
        length_type_id = self.read_n_bits(1)
        contained_values = []
        if length_type_id == '0':
            n_bits_for_subpackets = int(self.read_n_bits(15), 2)
            start_i = self.i
            while self.i < start_i + n_bits_for_subpackets:
                contained_values.append(self.evaluate_subpacket())
        else:
            n_subpackets_contained = int(self.read_n_bits(11), 2)
            for _ in range(n_subpackets_contained):
                contained_values.append(self.evaluate_subpacket())
        return contained_values

    def operate_on_values(self, values):
        if self.type_id in (5, 6, 7):
            assert len(values) == 2
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return mult(values)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 5:
            return int(values[0] > values[1])
        elif self.type_id == 6:
            return int(values[0] < values[1])
        elif self.type_id == 7:
            return int(values[0] == values[1])
        assert False, self.type_id

    def evaluate(self):
        if self.type_id == 4:
            return self.evaluate_literal()
        contained_values = self.evaluate_subpackets()
        return self.operate_on_values(contained_values)


class InterpreterWithStringConsumption:
    def __init__(self, command_bit_string):
        self.bit_string = command_bit_string
        self.version = int(self.read_n_bits(3), 2)
        self.type_id = int(self.read_n_bits(3), 2)

    def read_n_bits(self, n_bits):
        result = self.bit_string[:n_bits]
        self.bit_string = self.bit_string[n_bits:]
        return result

    def evaluate_literal(self):
        groups = []
        stop = False
        while not stop:
            stop = self.read_n_bits(1) == '0'
            groups.append(self.read_n_bits(4))
        return int(''.join(groups), 2)

    def evaluate_subpacket(self):
        sub_interpreter = InterpreterWithStringConsumption(self.bit_string)
        value = sub_interpreter.evaluate()
        self.bit_string = sub_interpreter.bit_string
        return value

    def evaluate_subpackets(self):
        length_type_id = self.read_n_bits(1)
        contained_values = []
        if length_type_id == '0':
            n_bits_for_subpackets = int(self.read_n_bits(15), 2)
            current_length = len(self.bit_string)
            while current_length - len(self.bit_string) < n_bits_for_subpackets:
                contained_values.append(self.evaluate_subpacket())
        else:
            n_subpackets_contained = int(self.read_n_bits(11), 2)
            for _ in range(n_subpackets_contained):
                contained_values.append(self.evaluate_subpacket())
        return contained_values

    def operate_on_values(self, values):
        if self.type_id in (5, 6, 7):
            assert len(values) == 2
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return mult(values)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 5:
            return int(values[0] > values[1])
        elif self.type_id == 6:
            return int(values[0] < values[1])
        elif self.type_id == 7:
            return int(values[0] == values[1])
        assert False, self.type_id

    def evaluate(self):
        if self.type_id == 4:
            return self.evaluate_literal()
        contained_values = self.evaluate_subpackets()
        return self.operate_on_values(contained_values)
