from util import *

GROWTH_PER_DIMENSION_PER_STEP = 1


def get_pattern_coords(x, y):
    for d_y in (-1, 0, 1):
        for d_x in (-1, 0, 1):
            yield x + d_x, y + d_y


class ImageEnhancer:
    def __init__(self, grid, algorithm):
        self.grid = []
        for row in grid:
            self.grid.append([])
            for char in row:
                self.grid[-1].append(1 if char == '#' else 0)
        self.algorithm = [int(value) for value in list(algorithm.replace('.', '0').replace('#', '1'))]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.step_count = 0

    def set_image(self, grid):
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def get_value_of_area_around_pixel(self, x, y):
        area_value = 0
        bit_i = 8
        for x_n, y_n in get_pattern_coords(x, y):
            if 0 <= x_n <= self.width - 1 and 0 <= y_n <= self.height - 1:
                pixel = self.grid[y_n][x_n]
            elif self.step_count % 2 == 0:
                pixel = 0
            else:
                pixel = self.algorithm[0]
            area_value += pixel << bit_i
            bit_i -= 1
        return area_value

    def step(self):
        margin = GROWTH_PER_DIMENSION_PER_STEP
        new_image = []
        for y in range(-margin, self.height + margin):
            new_image.append([])
            for x in range(-margin, self.width + margin):
                index = self.get_value_of_area_around_pixel(x, y)
                new_image[-1].append(self.algorithm[index])
        self.step_count += 1
        self.set_image(new_image)

    def enhance(self, n_steps):
        for _ in range(n_steps):
            self.step()

    def get_n_pixels_lit(self):
        return sum((line.count(1) for line in self.grid))


def enhance_input_image_and_count_lit(n_steps):
    lines = read_input_as_lines()
    enhancer = ImageEnhancer(lines[1:], lines[0])
    enhancer.enhance(n_steps)
    return enhancer.get_n_pixels_lit()


def part1():
    return enhance_input_image_and_count_lit(2)


def part2():
    return enhance_input_image_and_count_lit(50)


if __name__ == '__main__':
    print(part1())
    print(part2())
