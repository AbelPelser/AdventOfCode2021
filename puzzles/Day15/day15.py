from util import *


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


def part1():
    lines = read_input_as_lines()
    lines_nr = [list(map(int, list(l))) for l in lines]
    d, p = dijkstra2(lines_nr)
    return d[(len(lines[0]) - 1, len(lines) - 1)]


def dijkstra2(grid):
    visited = set()
    unvisited = set()
    distances = {(0, 0): 0}
    paths = {(0, 0): []}
    x = 0
    y = 0
    while True:
        if (x, y) in visited:
            raise ValueError
        current_distance = distances[(x, y)]
        current_path = paths[(x, y)]
        for new_x, new_y in get_neighbours(grid, x, y):
            potential_best_d = current_distance + grid[new_y][new_x]
            current_neighbour_d = distances.get((new_x, new_y))
            if current_neighbour_d is None or potential_best_d < current_neighbour_d:
                distances[(new_x, new_y)] = potential_best_d
                paths[(new_x, new_y)] = current_path + [(new_x, new_y)]
        visited.add((x, y))
        unvisited = set.union(unvisited, {(a, b) for a, b in get_neighbours(grid, x, y)})
        unvisited = {t for t in unvisited if t not in visited}
        if (len(visited) == (len(grid) * len(grid[0]))) or len(unvisited) == 0:
            break
        x, y = min(unvisited, key=lambda t: distances[t])
    return distances, paths


def update_row(row, increase):
    res = [(e + increase) for e in row]
    for i in range(len(res)):
        if res[i] > 9:
            res[i] -= 9
    assert len(row) == len(res)
    return res


def part2():
    lines = read_input_as_lines()
    lines_nr = [list(map(int, list(l))) for l in lines]
    # Widen
    for i in range(len(lines_nr)):
        row = lines_nr[i][:]
        for increase in range(1, 5):
            lines_nr[i] += update_row(row, increase)
    lines_nr_orig = lines_nr[:]
    # Deepen
    for increase in range(1, 5):
        to_add = [update_row(line, increase) for line in lines_nr_orig]
        lines_nr += to_add
    d, p = dijkstra2(lines_nr)
    return d[(len(lines_nr[0]) - 1, len(lines_nr) - 1)]


if __name__ == '__main__':
    print(part1())
    print(part2())
