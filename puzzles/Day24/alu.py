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