from util import *

PAIRS = {
    '<': '>', '[': ']', '{': '}', '(': ')'
}

illegal_c_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part1():
    lines = read_input_as_lines()
    score = 0
    for line in lines:
        allowed_closes = list()
        corrupt = False
        for c in list(line):
            if c in ('<', '[', '{', '('):
                allowed_closes.append(PAIRS[c])
            else:
                if c != allowed_closes[-1]:
                    score += illegal_c_map[c]
                    corrupt = True
                    break
                allowed_closes = allowed_closes[:-1]
        if corrupt:
            continue
    return score


def part2():
    lines = read_input_as_lines()
    all_scores = []
    for line in lines:
        allowed_closes = list()
        corrupt = False
        for c in list(line):
            if c in ('<', '[', '{', '('):
                allowed_closes.append(PAIRS[c])
            else:
                if c != allowed_closes[-1]:
                    corrupt = True
                    break
                allowed_closes = allowed_closes[:-1]
        if corrupt:
            continue
        score = 0
        for c in allowed_closes[::-1]:
            score *= 5
            score += {')': 1, ']': 2, '}': 3, '>': 4}[c]
        all_scores.append(score)
    return sorted(all_scores)[len(all_scores) // 2]


if __name__ == '__main__':
    print(part1())
    print(part2())
