from util import *


def find_low_points(height_map):
    for (y, x), height in enumerate_matrix(height_map):
        neighbour_coords = get_neighbour_coords_in_matrix(height_map, (y, x))
        neighbours = [height_map[n_y][n_x] for (n_y, n_x) in neighbour_coords]
        if height < min(neighbours):
            yield y, x


def part1():
    height_map = read_input_as_digit_grid()
    sum_of_risk = 0
    for (y, x), height in enumerate_matrix(height_map):
        neighbour_coords = get_neighbour_coords_in_matrix(height_map, (y, x))
        neighbours = [height_map[n_y][n_x] for (n_y, n_x) in neighbour_coords]
        if height_map[y][x] < min(neighbours):
            sum_of_risk += height + 1
    return sum_of_risk


def find_basin(height_map, coord, basin, seen=None):
    if seen is None:
        seen = set()
    if coord in seen:
        return basin
    seen.add(coord)
    x, y = coord
    for new_y, new_x in get_neighbour_coords_in_matrix(height_map, (y, x)):
        if height_map[new_y][new_x] < 9:
            new_coord = (new_x, new_y)
            basin.add(new_coord)
            basin = find_basin(height_map, new_coord, basin, seen)
    return basin


def part2():
    height_map = read_input_as_digit_grid()
    basin_sizes = []
    for y, x in find_low_points(height_map):
        coord = (x, y)
        basin = find_basin(height_map, coord, {coord})
        basin_sizes.append(len(basin))
    return mult(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    print(part1())
    print(part2())
