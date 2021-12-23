from puzzles.Day23.burrow import Burrow
from util import *


class Solver:
    def __init__(self):
        self.minimal_cost = None
        self.best_costs_per_state = {}

    def solve(self, burrow, current_cost=0):
        state = burrow.dump()
        if self.minimal_cost is not None and current_cost >= self.minimal_cost:
            return
        if state in self.best_costs_per_state.keys():
            if self.best_costs_per_state[state] <= current_cost:
                return
        self.best_costs_per_state[state] = current_cost
        possible_moves = burrow.get_all_possible_moves()
        for move_cost, (from_coord, to_coord) in burrow.prioritize_moves(possible_moves):
            new_cost = current_cost + move_cost
            burrow_copy = burrow.copy()
            burrow_copy.move(from_coord, to_coord)
            if burrow_copy.is_finished():
                if self.minimal_cost is None or new_cost < self.minimal_cost:
                    self.minimal_cost = new_cost
                    print(new_cost)
            else:
                self.solve(burrow_copy, new_cost)
        return self.minimal_cost


def part1():
    burrow = Burrow()
    burrow.setup_from_input(read_input_as_lines(filename='input_part1'))
    return Solver().solve(burrow)


def part2():
    burrow = Burrow()
    burrow.setup_from_input(read_input_as_lines(filename='input_part2'))
    return Solver().solve(burrow)


if __name__ == '__main__':
    print(time_call(part1))
    print(time_call(part2))
