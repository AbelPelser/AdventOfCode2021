from util import *


def iterate_over_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            yield y, x, grid[y][x]


def find_low_points(height_map):
    for y, x, height in iterate_over_grid(height_map):
        neighbour_coords = get_neighbour_coords_in_grid(height_map, (y, x))
        neighbours = [height_map[n_y][n_x] for (n_y, n_x) in neighbour_coords]
        if height < min(neighbours):
            yield y, x


def part1():
    height_map = read_input_as_digit_grid()
    sum_of_risk = 0
    for y, x, height in iterate_over_grid(height_map):
        neighbour_coords = get_neighbour_coords_in_grid(height_map, (y, x))
        neighbours = [height_map[n_y][n_x] for (n_y, n_x) in neighbour_coords]
        if height_map[y][x] < min(neighbours):
            sum_of_risk += height + 1
    return sum_of_risk


def find_basin(height_map, x, y, basin, seen=None):
    if seen is None:
        seen = set()
    if (x, y) in seen:
        return basin
    seen.add((x, y))
    for new_y, new_x in get_neighbour_coords_in_grid(height_map, (y, x)):
        if height_map[new_y][new_x] < 9:
            basin.add((new_x, new_y))
            basin = find_basin(height_map, new_x, new_y, basin, seen)
    return basin


def part2():
    height_map = read_input_as_digit_grid()
    basin_sizes = []
    for y, x in find_low_points(height_map):
        basin = find_basin(height_map, x, y, {(x, y)})
        basin_sizes.append(len(basin))
    return mult(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    print(part1())
    print(part2())
