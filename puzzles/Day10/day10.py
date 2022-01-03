from util import *

BRACKET_PAIRINGS = {
    '<': '>', '[': ']', '{': '}', '(': ')'
}

CORRUPT_SCORES = {
    ')': 3,
    ']': 3 * 19,
    '}': 3 * 3 * 7 * 19,
    '>': 3 * 3 * 3 * 7 * 7 * 19
}

UNCLOSED_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


class NavigationSyntaxChecker:
    def __init__(self, lines):
        self.lines = lines
        self.corrupt_score = 0
        self.incompleteness_scores = []

    def check_line(self, line):
        bracket_stack = []
        corrupt = False
        for char in list(line):
            if char in '<[{(':
                bracket_stack.append(BRACKET_PAIRINGS[char])
            elif char != bracket_stack.pop():
                self.corrupt_score += CORRUPT_SCORES[char]
                corrupt = True
                break
        return corrupt, bracket_stack

    def check_file(self):
        for line in self.lines:
            corrupt, bracket_stack = self.check_line(line)
            if corrupt:
                continue
            score = 0
            for unclosed_bracket in bracket_stack[::-1]:
                score *= 5
                score += UNCLOSED_SCORES[unclosed_bracket]
            self.incompleteness_scores.append(score)

    def get_middle_incompleteness_score(self):
        scores = self.incompleteness_scores
        return sorted(scores)[len(scores) // 2]


def part1():
    checker = NavigationSyntaxChecker(read_input_as_lines())
    checker.check_file()
    return checker.corrupt_score


def part2():
    checker = NavigationSyntaxChecker(read_input_as_lines())
    checker.check_file()
    return checker.get_middle_incompleteness_score()


if __name__ == '__main__':
    print(part1())
    print(part2())
