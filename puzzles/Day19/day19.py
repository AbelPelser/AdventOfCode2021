from collections import defaultdict

from util import *


def parse_input():
    sections = safe_split(read_input(), '\n\n')
    scanner_data = {}
    for section in sections:
        section_lines = safe_split(section)
        scan_nr = int(section_lines[0].split('scanner ')[1].split(' ---')[0])
        scanner_data[scan_nr] = {}
        for o_i, o in enumerate(all_orientations):
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



# orientations = [
#     lambda x, y, z: (x, y, z),
#     lambda x, y, z: (x, -z, y),
#     lambda x, y, z: (x, -y, -z),
#     lambda x, y, z: (x, z, -y),
#
#     lambda x, y, z: (-y, x, z),
#     lambda x, y, z: (z, x, y),
#     lambda x, y, z: (y, x, -z),
#     lambda x, y, z: (-z, x, -y),
#
#     lambda x, y, z: (-x, -y, z),
#     lambda x, y, z: (-x, -z, -y),
#     lambda x, y, z: (-x, y, -z),
#     lambda x, y, z: (-x, z, y),
#
#     lambda x, y, z: (y, -x, z),
#     lambda x, y, z: (z, -x, -y),
#     lambda x, y, z: (-y, -x, z),
#     lambda x, y, z: (-z, -x, y),
#
#     lambda x, y, z: (-z, y, x),
#     lambda x, y, z: (y, z, x),
#     lambda x, y, z: (z, -y, x),
#     lambda x, y, z: (-y, -z, x),
#
#     lambda x, y, z: (-z, -y, -x),
#     lambda x, y, z: (-y, z, -x),
#     lambda x, y, z: (z, y, -x),
#     lambda x, y, z: (y, -z, -x),
# ]


all_orientations = [
    #XX
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, -z),
    #XX
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-x, -z, y),
    lambda x, y, z: (x, -z, -y),
    lambda x, y, z: (-x, z, -y),
    lambda x, y, z: (-x, -z, -y),
    #XX
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (-y, z, x),
    lambda x, y, z: (y, -z, x),
    lambda x, y, z: (y, z, -x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, -x),
    #XX
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (-y, -x, z),
    lambda x, y, z: (y, -x, -z),
    lambda x, y, z: (-y, x, -z),
    lambda x, y, z: (-y, -x, -z),
    #XX
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (-z, x, y),
    lambda x, y, z: (z, -x, y),
    lambda x, y, z: (z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, -y),
    #XX
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-z, -y, x),
    lambda x, y, z: (z, -y, -x),
    lambda x, y, z: (-z, y, -x),
    lambda x, y, z: (-z, -y, -x),
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
    best_mapping = None
    best_o_i = None
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
                    # print(f'[{f0}][{t0}] == [{f1}][{t1}] ({diff1})')
                    mapping_candidate[f0].add(f1)
                    mapping_candidate[t0].add(t1)
        if len(mapping_candidate) >= 12:
            if best_mapping is None or len(mapping_candidate) > len(best_mapping):
                good = True
                for v in mapping_candidate.values():
                    if len(v) > 1:
                        good = False
                if good:
                    if best_mapping is not None:
                        print(f'overwriting best mapping {len(mapping_candidate)} > {len(best_mapping)}')
                    best_mapping = mapping_candidate
                    best_o_i = o_i
    if best_mapping:
        good = True
        for v in best_mapping.values():
            if len(v) > 1:
                good = False
        if not good:
            print(f'HELP! {best_mapping}')
    return best_mapping, best_o_i


def part1():
    scanner_data, diff_maps = parse_input()
    scanner_data0 = scanner_data[0][0]  # Everything relative to scanner 0
    while len(scanner_data) > 1:
        progress = False
        for i in scanner_data.keys():
            if i == 0:
                continue
            mapping, orientation_id = map_from_scanner0_to_another(scanner_data0, diff_maps[i])
            if not mapping:
                continue
            for targets in mapping.values():
                assert len(targets) == 1
            def_mapping = {k: v.pop() for k, v in mapping.items()}
            relative_beacon_position1 = None
            for point_in_scanner0, point_in_scanner1 in def_mapping.items():
                relative_beacon_position1 = (point_in_scanner0[0] - point_in_scanner1[0], point_in_scanner0[1] - point_in_scanner1[1], point_in_scanner0[2] - point_in_scanner1[2])
                print(f'Position of scanner {i} is {relative_beacon_position1} relative to 0')
                break
            # Move all points relative to scanner 0
            for point_in_scanner1 in scanner_data[i][0]:
                oriented = all_orientations[orientation_id](*point_in_scanner1)
                relative_to_scanner0 = (oriented[0] + relative_beacon_position1[0], oriented[1] + relative_beacon_position1[1], oriented[2] + relative_beacon_position1[2])
                scanner_data0.append(relative_to_scanner0)
            scanner_data0 = list(set(scanner_data0))
            print(f'Removing scanner {i}')
            progress = True
            del scanner_data[i]
            # def_mapping_upright = {}
            # print(def_mapping)
            # for point_in_scanner0, oriented_point_in_scanner1 in def_mapping.items():
            #     point_in_scanner1_index = scanner_data[i][orientation_id].index(oriented_point_in_scanner1)
            #     # Get upright point
            #     point_in_scanner1 = scanner_data[i][0][point_in_scanner1_index]
            #     def_mapping_upright[point_in_scanner0] = point_in_scanner1
            # # def_mapping_upright corresponds to original input
            # print(def_mapping_upright)
            break
        if not progress:
            print(f'No more progress - error {scanner_data.keys()}')
            break
    return len(set(scanner_data0))


def part2():
    scanner_data, diff_maps = parse_input()
    scanner_data0 = scanner_data[0][0]  # Everything relative to scanner 0
    scanner_distances = []
    while len(scanner_data) > 1:
        progress = False
        for i in scanner_data.keys():
            if i == 0:
                continue
            mapping, orientation_id = map_from_scanner0_to_another(scanner_data0, diff_maps[i])
            if not mapping:
                continue
            for targets in mapping.values():
                assert len(targets) == 1
            def_mapping = {k: v.pop() for k, v in mapping.items()}
            relative_beacon_position1 = None
            for point_in_scanner0, point_in_scanner1 in def_mapping.items():
                relative_beacon_position1 = (point_in_scanner0[0] - point_in_scanner1[0], point_in_scanner0[1] - point_in_scanner1[1], point_in_scanner0[2] - point_in_scanner1[2])
                print(f'Position of scanner {i} is {relative_beacon_position1} relative to 0')
                scanner_distances.append(relative_beacon_position1)
                break
            # Move all points relative to scanner 0
            for point_in_scanner1 in scanner_data[i][0]:
                oriented = all_orientations[orientation_id](*point_in_scanner1)
                relative_to_scanner0 = (oriented[0] + relative_beacon_position1[0], oriented[1] + relative_beacon_position1[1], oriented[2] + relative_beacon_position1[2])
                scanner_data0.append(relative_to_scanner0)
            scanner_data0 = list(set(scanner_data0))
            print(f'Removing scanner {i}')
            progress = True
            del scanner_data[i]
            # def_mapping_upright = {}
            # print(def_mapping)
            # for point_in_scanner0, oriented_point_in_scanner1 in def_mapping.items():
            #     point_in_scanner1_index = scanner_data[i][orientation_id].index(oriented_point_in_scanner1)
            #     # Get upright point
            #     point_in_scanner1 = scanner_data[i][0][point_in_scanner1_index]
            #     def_mapping_upright[point_in_scanner0] = point_in_scanner1
            # # def_mapping_upright corresponds to original input
            # print(def_mapping_upright)
            break
        if not progress:
            print(f'No more progress - error {scanner_data.keys()}')
            break
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
