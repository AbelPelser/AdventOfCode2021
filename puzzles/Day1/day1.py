from util import read_input_as_numbers


def part1():
    numbers = read_input_as_numbers()
    prev = None
    c = 0
    for n in numbers:
        if prev is not None and n > prev:
            c += 1
        prev = n
    return c


def part2():
    numbers = read_input_as_numbers()
    prev = None
    prevb = None
    c = 0
    last_s = None
    for n in numbers:
        if prev is not None and prevb is not None and last_s is not None and sum((n, prev, prevb)) > last_s:
            c += 1
        if prev is not None and prevb is not None:
            last_s = sum((n, prev, prevb))
        prevb = prev
        prev = n
    return c


if __name__ == '__main__':
    print(part1())
    print(part2())
