import re
from collections import defaultdict

from puzzles.Day22.cube_util import cubes_overlap, get_area_cube, join_cube, split_overlapping_cube
from util import *


class Grid:
    def __init__(self):
        self.cubes_on = []
        self.cubes_by_x_from = defaultdict(set)
        self.cubes_by_x_to = defaultdict(set)
        self.cubes_by_y_from = defaultdict(set)
        self.cubes_by_y_to = defaultdict(set)
        self.cubes_by_z_from = defaultdict(set)
        self.cubes_by_z_to = defaultdict(set)

    def remove_cube(self, cube_to_remove):
        x_from, x_to, y_from, y_to, z_from, z_to = cube_to_remove
        self.cubes_by_x_from[x_from].remove(cube_to_remove)
        self.cubes_by_x_to[x_to].remove(cube_to_remove)
        self.cubes_by_y_from[y_from].remove(cube_to_remove)
        self.cubes_by_y_to[y_to].remove(cube_to_remove)
        self.cubes_by_z_from[z_from].remove(cube_to_remove)
        self.cubes_by_z_to[z_to].remove(cube_to_remove)
        self.cubes_on.remove(cube_to_remove)

    def get_join_candidate(self, cube):
        x_from, x_to, y_from, y_to, z_from, z_to = cube
        x_matches = self.cubes_by_x_from[x_from].intersection(self.cubes_by_x_to[x_to])
        y_matches = self.cubes_by_y_from[y_from].intersection(self.cubes_by_y_to[y_to])
        z_matches = self.cubes_by_z_from[z_from].intersection(self.cubes_by_z_to[z_to])
        x_and_y_matches = x_matches.intersection(y_matches)
        x_and_z_matches = x_matches.intersection(z_matches)
        y_and_z_matches = y_matches.intersection(z_matches)

        candidate_sets = [
            x_and_y_matches.intersection(self.cubes_by_z_to[z_from]),
            x_and_y_matches.intersection(self.cubes_by_z_from[z_to]),
            x_and_z_matches.intersection(self.cubes_by_y_to[y_from]),
            x_and_z_matches.intersection(self.cubes_by_y_from[y_to]),
            y_and_z_matches.intersection(self.cubes_by_x_to[x_from]),
            y_and_z_matches.intersection(self.cubes_by_x_from[x_to])
        ]
        for candidate_set in candidate_sets:
            if len(candidate_set) > 0:
                return candidate_set.pop()
        return None

    def add_cube(self, cube_to_add):
        candidate = self.get_join_candidate(cube_to_add)
        if candidate:
            joined = join_cube(candidate, cube_to_add)
            self.remove_cube(candidate)
            self.add_cube(joined)
            return
        x_from, x_to, y_from, y_to, z_from, z_to = cube_to_add
        self.cubes_by_x_from[x_from].add(cube_to_add)
        self.cubes_by_x_to[x_to].add(cube_to_add)
        self.cubes_by_y_from[y_from].add(cube_to_add)
        self.cubes_by_y_to[y_to].add(cube_to_add)
        self.cubes_by_z_from[z_from].add(cube_to_add)
        self.cubes_by_z_to[z_to].add(cube_to_add)
        self.cubes_on.append(cube_to_add)

    def process_cube(self, is_on, current_cube):
        existing_overlapping = None
        for cube in self.cubes_on:
            if cubes_overlap(current_cube, cube):
                existing_overlapping = cube
                break
        if not existing_overlapping:
            if is_on:
                self.add_cube(current_cube)
            return
        self.remove_cube(existing_overlapping)
        _, non_overlap = split_overlapping_cube(current_cube, existing_overlapping)
        for cube_slice in non_overlap:
            self.add_cube(cube_slice)
        overlap, non_overlap = split_overlapping_cube(existing_overlapping, current_cube)
        if is_on:
            self.add_cube(overlap)
        for cube_slice in non_overlap:
            self.process_cube(is_on, cube_slice)


def parse_input():
    lines = read_input_as_lines()
    data = []
    for line in lines:
        on_or_off, remainder = line.split(' ', 1)
        is_on = on_or_off == 'on'
        boundaries = re.match('x=(-?\\d+)..(-?\\d+),y=(-?\\d+)..(-?\\d+),z=(-?\\d+)..(-?\\d+)', remainder).groups()
        a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = tuple(map(int, boundaries))
        data.append((is_on, (a_x_from, a_x_to + 1, a_y_from, a_y_to + 1, a_z_from, a_z_to + 1)))
    return data


def part1():
    data = parse_input()
    grid = Grid()
    for is_on, cube in data:
        x_from, x_to, y_from, y_to, z_from, z_to = cube
        if x_from > 50 or y_from > 50 or z_from > 50 or x_to < -50 or y_to < -50 or z_to < -50:
            continue
        grid.process_cube(is_on, cube)
    return sum((get_area_cube(c) for c in grid.cubes_on))


def part2():
    data = parse_input()
    grid = Grid()
    for i, (is_on, cube) in enumerate(data):
        grid.process_cube(is_on, cube)
    return sum((get_area_cube(c) for c in grid.cubes_on))


if __name__ == '__main__':
    print(part1())
    print(part2())
