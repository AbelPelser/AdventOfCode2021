import re
from collections import defaultdict
from typing import List

from puzzles.Day22.cube_util import cubes_overlap, get_area_cube, split_overlapping_cube
from util import *


def part1():
    lines = read_input_as_lines()
    data = []
    for line in lines:
        on_or_off, remainder = line.split(' ', 1)
        on = on_or_off == 'on'
        boundaries_as_strings = re.match('x=(-?\\d+)..(-?\\d+),y=(-?\\d+)..(-?\\d+),z=(-?\\d+)..(-?\\d+)',
                                         remainder).groups()
        bounds = tuple(map(int, boundaries_as_strings))
        data.append((on, bounds))

    cubes = defaultdict(bool)
    for on_or_off, (x_from, x_to, y_from, y_to, z_from, z_to) in data:
        if x_from > 50 or y_from > 50 or z_from > 50:
            continue
        if x_to < -50 or y_to < -50 or z_to < -50:
            continue
        if x_from < -50:
            x_from = -50
        if y_from < -50:
            y_from = -50
        if z_from < -50:
            z_from = -50
        if x_to > 50:
            x_to = 50
        if y_to > 50:
            y_to = 50
        if z_to > 50:
            z_to = 50
        for x in range(x_from, x_to + 1):
            for y in range(y_from, y_to + 1):
                for z in range(z_from, z_to + 1):
                    cubes[(x, y, z)] = on_or_off
    return len([x for x in cubes.keys() if cubes[x] == True])


def cube_contains_cube(a, b):
    a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = a
    b_x_from, b_x_to, b_y_from, b_y_to, b_z_from, b_z_to = b
    return a_x_from <= b_x_from and a_x_to >= b_x_to and \
           a_y_from <= b_y_from and a_y_to >= b_y_to and \
           a_z_from <= b_z_from and a_z_to >= b_z_to


def process_cube(is_on, current_cube, cubes_on: List):
    if get_area_cube(current_cube) == 0:
        return cubes_on
    existing_overlapping = None
    cubes_on_copy = cubes_on[:]
    for cube in cubes_on_copy:
        if cubes_overlap(current_cube, cube):
            existing_overlapping = cube
            break
    if not existing_overlapping:
        if is_on:
            cubes_on_copy.append(current_cube)
        return cubes_on_copy
    cubes_on_copy.remove(existing_overlapping)
    # Slices that are in the existing cube and not in this one
    # No cubes in cubes_on should ever already overlap, so we can safely add them back to the list
    _, non_overlap = split_overlapping_cube(current_cube, existing_overlapping)
    for cube_slice in non_overlap:
        cubes_on_copy.append(cube_slice)
    # Slices that are in this cube and not in the existing one
    # Need to be reprocessed in case they overlap with more cubes
    overlap, non_overlap = split_overlapping_cube(existing_overlapping, current_cube)
    if is_on:
        cubes_on_copy.append(overlap)
    for cube_slice in non_overlap:
        cubes_on_copy = process_cube(is_on, cube_slice, cubes_on_copy)
    return cubes_on_copy


def part2():
    lines = read_input_as_lines()
    data = []
    for line in lines:
        on_or_off, remainder = line.split(' ', 1)
        on = on_or_off == 'on'
        boundaries_as_strings = re.match('x=(-?\\d+)..(-?\\d+),y=(-?\\d+)..(-?\\d+),z=(-?\\d+)..(-?\\d+)',
                                         remainder).groups()
        a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = tuple(map(int, boundaries_as_strings))
        data.append((on, (a_x_from, a_x_to + 1, a_y_from, a_y_to + 1, a_z_from, a_z_to + 1)))

    cubes_on = []
    for i, (is_on, cube) in enumerate(data):
        print(i)
        cubes_on = process_cube(is_on, cube, cubes_on)
    total = 0
    for cube in cubes_on:
        total += get_area_cube(cube)
    return total


if __name__ == '__main__':
    # print(part1())
    print(part2())
