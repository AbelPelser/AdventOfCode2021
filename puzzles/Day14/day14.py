from collections import defaultdict

from util import *


def part1():
    text = read_input()
    start, pairs_str = safe_split(text, '\n\n')
    pairs = {}
    for line in safe_split(pairs_str):
        f, t = line.split(' -> ')
        pairs[f] = t
    string = start
    for _ in range(10):
        new_string = string[0]
        for i in range(1, len(string)):
            if string[i - 1:i + 1] in pairs.keys():
                new_string += pairs[string[i - 1:i + 1]] + string[i]
            else:
                new_string += string[i]
        string = new_string

    quantities = defaultdict(int)
    for c in string:
        quantities[c] += 1
    return max(quantities.values()) - min([v for v in quantities.values() if v != 0])


def part2():
    text = read_input()
    start, pairs_str = safe_split(text, '\n\n')
    pairs = {}
    for line in safe_split(pairs_str):
        f, t = line.split(' -> ')
        pairs[f] = t

    pairs_present = defaultdict(int)
    for i in range(1, len(start)):
        pairs_present[start[i-1:i+1]] += 1
    quantities = defaultdict(int)
    for c in list(start):
        quantities[c] += 1

    for _ in range(40):
        new_pairs_present = defaultdict(int)
        for f, t in pairs.items():
            if pairs_present[f] > 0:
                new_pairs_present[f[0] + t] += pairs_present[f]
                new_pairs_present[t + f[1]] += pairs_present[f]
                quantities[t] += pairs_present[f]
        pairs_present = new_pairs_present
    return max(quantities.values()) - min([v for v in quantities.values() if v != 0])


if __name__ == '__main__':
    print(part1())
    print(part2())
