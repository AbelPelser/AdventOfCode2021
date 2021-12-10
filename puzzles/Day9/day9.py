from util import *


def part1():
    lines = read_input_as_lines()
    sum_of_risk = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            value = int(lines[y][x])
            if x > 0 and x < len(lines[y]) - 1 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x > 0 and x < len(lines[y]) - 1 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x == 0 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x == len(lines[y]) - 1 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x-1]):
                    sum_of_risk += value + 1
            elif x > 0 and x < len(lines[y]) - 1 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x == 0 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x == len(lines[y]) - 1 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x-1]):
                    sum_of_risk += value + 1
            elif x == 0 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x+1]):
                    sum_of_risk += value + 1
            elif x == len(lines[y]) - 1 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x-1]):
                    sum_of_risk += value + 1
    return sum_of_risk


def find_low_points(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            value = int(lines[y][x])
            if x > 0 and x < len(lines[y]) - 1 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x > 0 and x < len(lines[y]) - 1 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x == 0 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x == len(lines[y]) - 1 and y > 0 and y < len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y+1][x]) and value < int(lines[y][x-1]):
                    yield y, x
            elif x > 0 and x < len(lines[y]) - 1 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x-1]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x == 0 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x == len(lines[y]) - 1 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x-1]):
                    yield y, x
            elif x == 0 and y == len(lines) - 1:
                if value < int(lines[y-1][x]) and value < int(lines[y][x+1]):
                    yield y, x
            elif x == len(lines[y]) - 1 and y == 0:
                if value < int(lines[y+1][x]) and value < int(lines[y][x-1]):
                    yield y, x

def find_basin(lines_nr, x, y, basin, seen):
    if (x, y) in seen:
        return
    seen.append((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        if new_x < 0 or new_x >= len(lines_nr[0]) or new_y < 0 or new_y >= len(lines_nr):
            continue
        if lines_nr[new_y][new_x] < 9:
            if (new_x, new_y) not in basin:
                basin.append((new_x, new_y))
            find_basin(lines_nr, new_x, new_y, basin, seen)

def part2():
    lines = read_input_as_lines()
    lines_nr = []
    basin_sizes = []
    for line in lines:
        lines_nr.append(list(map(int, list(line))))
    for y, x in find_low_points(lines):
        basin = [(x, y)]
        find_basin(lines_nr, x, y, basin, [])
        basin_sizes.append(len(basin))
    return mult(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    print(part1())
    print(part2())
