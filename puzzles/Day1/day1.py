from util import read_input_as_numbers


def find_n_positive_deltas(items, window_size):
    return len([b - a for a, b in zip(items[:-window_size], items[window_size:]) if b > a])


def part1():
    return find_n_positive_deltas(read_input_as_numbers(), 1)


def part2():
    return find_n_positive_deltas(read_input_as_numbers(), 3)


if __name__ == '__main__':
    print(part1())
    print(part2())
