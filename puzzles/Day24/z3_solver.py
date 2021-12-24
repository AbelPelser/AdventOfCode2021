import z3


class Z3ConstraintGenerator:
    def __init__(self):
        self.solver = z3.Solver()
        # New variable for every assignment
        self.variables = {
            'w': [],
            'x': [z3.Int('x0')],
            'y': [z3.Int('y0')],
            'z': [z3.Int('z0')]
        }
        for var_name in ('x', 'y', 'z'):
            # x, y, z start at 0
            self.solver.add(self.variables[var_name][0] == 0)

    def create_target(self, var_name):
        var_list = self.variables[var_name]
        new_var = z3.Int(f'{var_name}{len(var_list)}')
        var_list.append(new_var)
        return new_var

    def parse_operand(self, operand):
        return self.variables[operand][-1] if operand in self.variables.keys() else int(operand)

    def parse_line(self, line):
        op = line[:3]
        target, *operands = line[4:].split(' ')
        if op == 'inp':
            # Only operation without any operands
            return op, self.create_target(target), None
        parsed_operands = [self.variables[target][-1]]
        for operand in operands:
            parsed_operands.append(self.parse_operand(operand))
        return op, self.create_target(target), parsed_operands

    def add_monad_constraints(self, lines):
        for line in lines:
            op, target, operands = self.parse_line(line)
            if op == 'inp':
                self.solver.add(target < 10)
                self.solver.add(target > 0)
            elif op == 'add':
                self.solver.add(target == (operands[0] + operands[1]))
            elif op == 'mul':
                self.solver.add(target == (operands[0] * operands[1]))
            elif op == 'div':
                self.solver.add(target == (operands[0] / operands[1]))
            elif op == 'mod':
                self.solver.add(target == (operands[0] % operands[1]))
            elif op == 'eql':
                self.solver.add(z3.If(operands[0] == operands[1], target == 1, target == 0))
        # The last z is the final z, and needs to be 0
        self.solver.add(self.variables['z'][-1] == 0)

    def find_min_monad(self):
        min_monad = None
        while self.solver.check() == z3.sat:
            model = self.solver.model()
            monad_string = ''.join((str(model[w]) for w in self.variables['w']))
            min_monad = int(monad_string)
            self.solver.add(z3.Or([w < model[w] for w in self.variables['w']]))
        return min_monad

    def find_max_monad(self):
        max_monad = None
        while self.solver.check() == z3.sat:
            model = self.solver.model()
            monad_string = ''.join((str(model[w]) for w in self.variables['w']))
            max_monad = int(monad_string)
            self.solver.add(z3.Or([w > model[w] for w in self.variables['w']]))
        return max_monad
