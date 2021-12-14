from collections import defaultdict

from util import *


def parse_input():
    text = read_input()
    polymer_template, pair_insertion_rules_str = safe_split(text, '\n\n')
    pair_insertion_rules = {}
    for line in safe_split(pair_insertion_rules_str):
        pair, to_insert = line.split(' -> ')
        pair_insertion_rules[pair] = to_insert
    return polymer_template, pair_insertion_rules


def run_pair_insertion_step(current_pair_counts, element_quantities, pair_insertion_rules):
    next_pair_counts = defaultdict(int)
    for pair, to_insert in pair_insertion_rules.items():
        pair_count = current_pair_counts[pair]
        if pair_count > 0:
            left, right = list(pair)
            next_pair_counts[left + to_insert] += pair_count
            next_pair_counts[to_insert + right] += pair_count
            element_quantities[to_insert] += pair_count
    return next_pair_counts


def run_pair_insertion(n_steps):
    polymer_template, pair_insertion_rules = parse_input()

    current_pair_counts = defaultdict(int)
    for i in range(1, len(polymer_template)):
        pair = polymer_template[i - 1:i + 1]
        current_pair_counts[pair] += 1

    element_quantities = defaultdict(int)
    for c in list(polymer_template):
        element_quantities[c] += 1

    for _ in range(n_steps):
        current_pair_counts = run_pair_insertion_step(current_pair_counts, element_quantities, pair_insertion_rules)
    all_quantities = element_quantities.values()
    return max(all_quantities) - min(all_quantities)


def part1():
    return run_pair_insertion(10)


def part2():
    return run_pair_insertion(40)


if __name__ == '__main__':
    print(part1())
    print(part2())
