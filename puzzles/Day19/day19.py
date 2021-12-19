from collections import defaultdict

from util import *


def parse_input():
    sections = safe_split(read_input(), '\n\n')
    scanner_data = {}
    for section in sections:
        section_lines = safe_split(section)
        scan_nr = int(section_lines[0].split('scanner ')[1].split(' ---')[0])
        scanner_data[scan_nr] = {}
        for o_i, o in enumerate(orientations):
            scanner_data[scan_nr][o_i] = []
            for line in section_lines[1:]:
                line_data = line.split(',')
                data = (int(line_data[0]), int(line_data[1]), int(line_data[2]))
                scanner_data[scan_nr][o_i].append(o(*data))
    diff_maps = {}
    for scan_nr in scanner_data.keys():
        diff_maps[scan_nr] = {}
        for o_i in scanner_data[scan_nr].keys():
            diff_maps[scan_nr][o_i] = make_difference_map(scanner_data[scan_nr][o_i])
    return scanner_data, diff_maps


orientations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, -y),

    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (-z, x, -y),

    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, z, y),

    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-z, -x, y),

    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-y, -z, x),

    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (y, -z, -x),
]


def make_difference_map(scanner_data_xyz_list):
    result = {}
    for i in range(len(scanner_data_xyz_list)):
        x_a, y_a, z_a = scanner_data_xyz_list[i]
        result[(x_a, y_a, z_a)] = {}
        for j in range(len(scanner_data_xyz_list)):
            x_b, y_b, z_b = scanner_data_xyz_list[j]
            result[(x_a, y_a, z_a)][(x_b, y_b, z_b)] = (x_b - x_a, y_b - y_a, z_b - z_a)
    return result


def map_from_scanner0_to_another(scanner_data0_oriented, diff_maps1):
    relative_differences0 = make_difference_map(scanner_data0_oriented)
    relative_differences0_inverted = {}
    for f0 in relative_differences0.keys():
        for t0 in relative_differences0[f0].keys():
            diff0 = relative_differences0[f0][t0]
            if diff0 == (0, 0, 0):
                continue
            relative_differences0_inverted[diff0] = (f0, t0)
    for o_i in diff_maps1.keys():
        relative_differences1 = diff_maps1[o_i]
        mapping_candidate = defaultdict(set)
        for f1 in relative_differences1.keys():
            for t1 in relative_differences1[f1].keys():
                diff1 = relative_differences1[f1][t1]
                if diff1 == (0, 0, 0):
                    continue
                if diff1 in relative_differences0_inverted.keys():
                    f0, t0 = relative_differences0_inverted[diff1]
                    mapping_candidate[f0].add(f1)
                    mapping_candidate[t0].add(t1)
        if len(mapping_candidate) >= 12:
            return mapping_candidate, o_i
    return None, -1


def reconstruct_data():
    scanner_data, diff_maps = parse_input()
    scanner_data0 = scanner_data[0][0]
    scanner_distances = []
    while len(scanner_data) > 1:
        for i in scanner_data.keys():
            if i == 0:
                continue
            mapping, orientation_id = map_from_scanner0_to_another(scanner_data0, diff_maps[i])
            if not mapping:
                continue
            def_mapping = {k: v.pop() for k, v in mapping.items()}
            position = None
            for point_in_scanner0, point_in_scanner1 in def_mapping.items():
                position = (point_in_scanner0[0] - point_in_scanner1[0], point_in_scanner0[1] - point_in_scanner1[1], point_in_scanner0[2] - point_in_scanner1[2])
                scanner_distances.append(position)
                break
            # Move all points relative to scanner 0
            for point_in_scanner1 in scanner_data[i][0]:
                reoriented = orientations[orientation_id](*point_in_scanner1)
                relative_to_scanner0 = (reoriented[0] + position[0], reoriented[1] + position[1], reoriented[2] + position[2])
                scanner_data0.append(relative_to_scanner0)
            scanner_data0 = list(set(scanner_data0))
            del scanner_data[i]
            break
    return scanner_distances, scanner_data0


def part1():
    _, scanner_data0 = reconstruct_data()
    return len(set(scanner_data0))


def part2():
    scanner_distances, _ = reconstruct_data()
    best_manhattan = None
    for i in range(len(scanner_distances)):
        for j in range(len(scanner_distances)):
            if i == j:
                continue
            m = manhattan(scanner_distances[i], scanner_distances[j])
            if best_manhattan is None or m > best_manhattan:
                best_manhattan = m
    return best_manhattan


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


if __name__ == '__main__':
    print(part1())
    print(part2())
