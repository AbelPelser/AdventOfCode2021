from algorithms import dijkstra_distance
from util import *

# from scipy.sparse.csgraph

def get_neighbours(lines_nr, x, y):
    if x > 0:
        yield x - 1, y
        # if y > 0:
        # yield x-1,y-1
        # if y < len(lines_nr) - 1:
        #     yield x - 1, y + 1
    if x < len(lines_nr[0]) - 1:
        yield x + 1, y
        # if y > 0:
        #     yield x+1, y-1
        # if y < len(lines_nr) - 1:
        #     yield x+1, y+1
    if y > 0:
        yield x, y - 1
    if y < len(lines_nr) - 1:
        yield x, y + 1
#
# def get_neighbours(grid, *coord):
#     neighbours = []
#     for value in coord:





def find_shortest_path_from_top_left_to_bottom_right(grid):
    distances = dijkstra_distance(
        start_node=(0, 0),
        get_neighbours_of_node=lambda node: get_neighbour_coords_in_matrix(grid, node[0], node[1]),
        get_cost_of_node=lambda node: grid[node[1]][node[0]]
    )
    return distances[(len(grid[0]) - 1, len(grid) - 1)]


def part1():
    return find_shortest_path_from_top_left_to_bottom_right(read_input_as_digit_grid())


def update_row(row, increase):
    res = [(e + increase) for e in row]
    for i in range(len(res)):
        if res[i] > 9:
            res[i] -= 9
    return res


def get_grid_expansion(grid, distance):
    result = []
    for row in grid:
        result.append([])
        for item in row:
            new_item = item + distance
            if new_item > 9:
                new_item -= 9
            result[-1].append(new_item)
    return result


def part2():
    grid = read_input_as_digit_grid()
    # Widen
    for i in range(len(grid)):
        row = grid[i][:]
        for increase in range(1, 5):
            grid[i] += update_row(row, increase)
    lines_nr_orig = grid[:]
    # Deepen
    for increase in range(1, 5):
        to_add = [update_row(line, increase) for line in lines_nr_orig]
        grid += to_add

    return find_shortest_path_from_top_left_to_bottom_right(grid)


if __name__ == '__main__':
    print(part1())
    print(part2())
