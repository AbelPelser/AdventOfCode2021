from util import *


def get_neighbours(grid, x, y):
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def get_pixel_index(grid, x, y, step_is_even, pixel_0):
    pixels = ''
    for x_n, y_n in get_neighbours(grid, x, y):
        if 0 <= x_n <= len(grid[0]) - 1 and 0 <= y_n <= len(grid) - 1:
            pixels += grid[y_n][x_n]
        else:
            if step_is_even:
                pixels += '.' if pixel_0 == '#' else '#'
            else:
                pixels += pixel_0
    return int(pixels.replace('#', '1').replace('.', '0'), 2)


def step(algorithm, current_image, step_n):
    s = 2
    new_image = ['' for _ in range(len(current_image) + 2 * s)]
    pixel_0 = algorithm[0]
    for y in range(-s, len(current_image) + s):
        for x in range(-s, len(current_image[0]) + s):
            index = get_pixel_index(current_image, x, y, step_n % 2 == 0, pixel_0)
            new_image[y + s] += algorithm[index]
    return new_image


def part1():
    lines = read_input_as_lines()
    algorithm = lines[0]
    current_image = lines[1:]
    for n in range(2):
        current_image = step(algorithm, current_image, n)
    total_lit = 0
    for line in current_image:
        total_lit += line.count('#')
    return total_lit


def part2():
    lines = read_input_as_lines()
    algorithm = lines[0]
    current_image = lines[1:]
    for n in range(50):
        current_image = step(algorithm, current_image, n)
    total_lit = 0
    for line in current_image:
        total_lit += line.count('#')
    return total_lit


if __name__ == '__main__':
    print(part1())
    print(part2())
