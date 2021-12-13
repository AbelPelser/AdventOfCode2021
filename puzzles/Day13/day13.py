from util import *


def part1():
    text = read_input()
    dots_text, folds_text = text.split('\n\n')
    dots = []
    for line in safe_split(dots_text):
        a, b = line.split(',')
        dots.append((int(a), int(b)))
    folds = []
    for line in safe_split(folds_text):
        folds.append((line[11:12], int(line[13:])))

    axis, amount = folds[0]
    new_dots = []
    if axis == 'x':
        for x, y in dots:
            if x < amount:
                if (x, y) not in new_dots:
                    new_dots.append((x, y))
            else:
                if (amount - (x - amount), y) not in new_dots:
                    new_dots.append((amount - (x - amount), y))
    elif axis == 'y':
        for x, y in dots:
            if y < amount:
                if (x, y) not in new_dots:
                    new_dots.append((x, y))
            else:
                if (x, amount - (y - amount)) not in new_dots:
                    new_dots.append((x, amount - (y - amount)))
    return len(new_dots)


def part2():
    text = read_input()
    dots_text, folds_text = text.split('\n\n')
    dots = []
    for line in safe_split(dots_text):
        a, b = line.split(',')
        dots.append((int(a), int(b)))
    folds = []
    for line in safe_split(folds_text):
        folds.append((line[11:12], int(line[13:])))

    for axis, amount in folds:
        new_dots = []
        if axis == 'x':
            for x, y in dots:
                if x < amount:
                    if (x, y) not in new_dots:
                        new_dots.append((x, y))
                else:
                    if (amount - (x - amount), y) not in new_dots:
                        new_dots.append((amount - (x - amount), y))
        elif axis == 'y':
            for x, y in dots:
                if y < amount:
                    if (x, y) not in new_dots:
                        new_dots.append((x, y))
                else:
                    if (x, amount - (y - amount)) not in new_dots:
                        new_dots.append((x, amount - (y - amount)))
        dots = new_dots
    for y in range(6):
        for x in range(40):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    return len(dots)


if __name__ == '__main__':
    print(part1())
    print(part2())
