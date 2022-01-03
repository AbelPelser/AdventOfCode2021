import re
from collections import defaultdict, namedtuple

from util import read_input_as_lines, time_call


def parse_input():
    start_positions = []
    for line in read_input_as_lines():
        position = re.match('Player \\d+ starting position: (\\d+)', line).groups()[0]
        start_positions.append(int(position) - 1)
    return start_positions


class DiracRunner:
    def __init__(self, starting_positions):
        self.positions = starting_positions
        self.die_roll_value = 1
        self.n_die_rolls = 0
        self.scores = [0, 0]
        self.player_turn = 0

    def roll(self):
        result = self.die_roll_value
        self.die_roll_value = (self.die_roll_value % 100) + 1
        self.n_die_rolls += 1
        return result

    def run(self):
        while max(self.scores) < 1000:
            self.positions[self.player_turn] += sum((self.roll() for _ in range(3)))
            self.positions[self.player_turn] %= 10
            self.scores[self.player_turn] += self.positions[self.player_turn] + 1
            self.player_turn = 1 - self.player_turn
        return min(self.scores) * self.n_die_rolls


def part1():
    return DiracRunner(parse_input()).run()


def part2():
    return DiracUniverseSimulator(parse_input()).run()


GameState = namedtuple('GameState', ('scores', 'positions'))
POSSIBLE_THROWS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


class DiracUniverseSimulator:
    def __init__(self, start_positions):
        self.n_universes_won = [0, 0]
        self.n_universes_with_game = defaultdict(int)
        self.n_universes_with_game_after_turn = None
        self.n_universes_with_game[GameState((0, 0), tuple(start_positions))] = 1
        self.player_turn = 0

    def play_turn_for_game_state(self, game_state, n_universes):
        for throw_value, n_possible_ways_to_throw_in_turn in POSSIBLE_THROWS.items():
            n_universes_with_throw = n_universes * n_possible_ways_to_throw_in_turn
            pos_after_throw = (game_state.positions[self.player_turn] + throw_value) % 10
            score_after_throw = game_state.CORRUPT_SCORES[self.player_turn] + pos_after_throw + 1
            if score_after_throw >= 21:
                self.n_universes_won[self.player_turn] += n_universes_with_throw
            else:
                if self.player_turn == 0:
                    new_state = GameState((score_after_throw, game_state.CORRUPT_SCORES[1]),
                                          (pos_after_throw, game_state.positions[1]))
                else:
                    new_state = GameState((game_state.CORRUPT_SCORES[0], score_after_throw),
                                          (game_state.positions[0], pos_after_throw))
                self.n_universes_with_game_after_turn[new_state] += n_universes_with_throw

    def run(self):
        while len(self.n_universes_with_game) > 0:
            self.n_universes_with_game_after_turn = defaultdict(int)
            for game_state, n_universes in self.n_universes_with_game.items():
                self.play_turn_for_game_state(game_state, n_universes)
            self.n_universes_with_game = self.n_universes_with_game_after_turn
            self.player_turn = 1 - self.player_turn
        return max(self.n_universes_won)


if __name__ == '__main__':
    print(time_call(part1))
    print(time_call(part2))
