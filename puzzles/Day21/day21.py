from collections import defaultdict

p1_start = 3
p2_start = 10


def part1():
    die_roll_value = 1
    n_die_rolls = 0
    p1_pos = p1_start - 1
    p2_pos = p2_start - 1
    p1_score = 0
    p2_score = 0
    while True:
        def roll():
            nonlocal die_roll_value, n_die_rolls

            result = die_roll_value
            die_roll_value += 1
            if die_roll_value > 100:
                die_roll_value = 1
            n_die_rolls += 1
            return result

        p1_move = roll() + roll() + roll()
        p1_pos = (p1_pos + p1_move) % 10
        p1_score += p1_pos + 1
        if p1_score >= 1000:
            return p2_score * n_die_rolls
        p2_move = roll() + roll() + roll()
        p2_pos = (p2_pos + p2_move) % 10
        p2_score += p2_pos + 1
        if p2_score >= 1000:
            return p1_score * n_die_rolls


def part2():
    # total_value: number of ways to reach this value in one triple throw
    possible_throws = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    n_universes_won_p1 = 0
    n_universes_won_p2 = 0
    n_universes_with_game = defaultdict(int)
    # p1_score, p2_score, p1_pos, p2_pos
    n_universes_with_game[(0, 0, p1_start - 1, p2_start - 1)] = 1
    while len(n_universes_with_game) > 0:
        p1_score = p2_score = p1_pos = p2_pos = n_universes = None
        for (p1_score, p2_score, p1_pos, p2_pos), n_universes in n_universes_with_game.items():
            break
        del n_universes_with_game[(p1_score, p2_score, p1_pos, p2_pos)]
        # player 1
        games_after_first_turn = defaultdict(int)
        for throw_value, n_possible_ways_to_throw_in_turn in possible_throws.items():
            n_universes_with_throw = n_universes * n_possible_ways_to_throw_in_turn
            p1_pos_after_throw = (p1_pos + throw_value) % 10
            p1_score_after_throw = p1_score + p1_pos_after_throw + 1
            if p1_score_after_throw >= 21:
                n_universes_won_p1 += n_universes_with_throw
            else:
                games_after_first_turn[
                    (p1_score_after_throw, p2_score, p1_pos_after_throw, p2_pos)] += n_universes_with_throw
        # player 2
        for (p1_score_after_throw, p2_score, p1_pos_after_throw,
             p2_pos), n_universes_after_first_turn in games_after_first_turn.items():
            for throw_value, n_possible_ways_to_throw_in_turn in possible_throws.items():
                n_universes_with_throw = n_universes_after_first_turn * n_possible_ways_to_throw_in_turn
                p2_pos_after_throw = (p2_pos + throw_value) % 10
                p2_score_after_throw = p2_score + p2_pos_after_throw + 1
                if p2_score_after_throw >= 21:
                    n_universes_won_p2 += n_universes_with_throw
                else:
                    n_universes_with_game[(p1_score_after_throw, p2_score_after_throw, p1_pos_after_throw,
                                           p2_pos_after_throw)] += n_universes_with_throw
    return max(n_universes_won_p1, n_universes_won_p2)


if __name__ == '__main__':
    print(part1())
    print(part2())
