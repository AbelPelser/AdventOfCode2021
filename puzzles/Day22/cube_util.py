def get_area_cube(cube):
    x_from, x_to, y_from, y_to, z_from, z_to = cube
    return (x_to - x_from) * (y_to - y_from) * (z_to - z_from)


def cubes_overlap(a, b):
    a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = a
    b_x_from, b_x_to, b_y_from, b_y_to, b_z_from, b_z_to = b
    if b_x_to <= a_x_from or a_x_to <= b_x_from:
        return False
    if b_y_to <= a_y_from or a_y_to <= b_y_from:
        return False
    if b_z_to <= a_z_from or a_z_to <= b_z_from:
        return False
    return True


def split_overlapping_cube(overlapping_cube, cube_to_split):
    # print(f'<{overlapping_cube}>, <{cube_to_split}>')
    a_x_from, a_x_to, a_y_from, a_y_to, a_z_from, a_z_to = overlapping_cube
    b_x_from, b_x_to, b_y_from, b_y_to, b_z_from, b_z_to = cube_to_split

    intersect_start_x = max(a_x_from, b_x_from)
    intersect_start_y = max(a_y_from, b_y_from)
    intersect_start_z = max(a_z_from, b_z_from)

    intersect_end_x = min(a_x_to, b_x_to)
    intersect_end_y = min(a_y_to, b_y_to)
    intersect_end_z = min(a_z_to, b_z_to)

    min_x = min(a_x_from, b_x_from)
    max_x = max(a_x_to, b_x_to)
    min_y = min(a_y_from, b_y_from)
    max_y = max(a_y_to, b_y_to)
    min_z = min(a_z_from, b_z_from)
    max_z = max(a_z_to, b_z_to)

    extends_left_x = b_x_from < intersect_start_x
    extends_right_x = b_x_to > intersect_end_x
    extends_left_y = b_y_from < intersect_start_y
    extends_right_y = b_y_to > intersect_end_y
    extends_left_z = b_z_from < intersect_start_z
    extends_right_z = b_z_to > intersect_end_z

    overlapping = intersect_start_x, intersect_end_x, \
                  intersect_start_y, intersect_end_y, \
                  intersect_start_z, intersect_end_z
    non_overlapping = []
    # 1
    if extends_left_x:
        non_overlapping.append((min_x, intersect_start_x,
                                intersect_start_y, intersect_end_y,
                                intersect_start_z, intersect_end_z))
    if extends_left_y:
        non_overlapping.append((intersect_start_x, intersect_end_x,
                                min_y, intersect_start_y,
                                intersect_start_z, intersect_end_z))
    if extends_left_z:
        non_overlapping.append((intersect_start_x, intersect_end_x,
                                intersect_start_y, intersect_end_y,
                                min_z, intersect_start_z))
    if extends_right_x:
        non_overlapping.append((intersect_end_x, max_x,
                                intersect_start_y, intersect_end_y,
                                intersect_start_z, intersect_end_z))
    if extends_right_y:
        non_overlapping.append((intersect_start_x, intersect_end_x,
                                intersect_end_y, max_y,
                                intersect_start_z, intersect_end_z))
    if extends_right_z:
        non_overlapping.append((intersect_start_x, intersect_end_x,
                                intersect_start_y, intersect_end_y,
                                intersect_end_z, max_z))
    # 2
    if extends_left_x:
        if extends_left_y:
            non_overlapping.append((min_x, intersect_start_x,
                                    min_y, intersect_start_y,
                                    intersect_start_z, intersect_end_z))
        if extends_right_y:
            non_overlapping.append((min_x, intersect_start_x,
                                    intersect_end_y, max_y,
                                    intersect_start_z, intersect_end_z))
        if extends_left_z:
            non_overlapping.append((min_x, intersect_start_x,
                                    intersect_start_y, intersect_end_y,
                                    min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((min_x, intersect_start_x,
                                    intersect_start_y, intersect_end_y,
                                    intersect_end_z, max_z))
    if extends_right_x:
        if extends_left_y:
            non_overlapping.append((intersect_end_x, max_x,
                                    min_y, intersect_start_y,
                                    intersect_start_z, intersect_end_z))
        if extends_right_y:
            non_overlapping.append((intersect_end_x, max_x,
                                    intersect_end_y, max_y,
                                    intersect_start_z, intersect_end_z))
        if extends_left_z:
            non_overlapping.append((intersect_end_x, max_x,
                                    intersect_start_y, intersect_end_y,
                                    min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_end_x, max_x,
                                    intersect_start_y, intersect_end_y,
                                    intersect_end_z, max_z))
    if extends_left_y:
        if extends_left_z:
            non_overlapping.append((intersect_start_x, intersect_end_x,
                                    min_y, intersect_start_y,
                                    min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_start_x, intersect_end_x,
                                    min_y, intersect_start_y,
                                    intersect_end_z, max_z))
    if extends_right_y:
        if extends_left_z:
            non_overlapping.append((intersect_start_x, intersect_end_x,
                                    intersect_end_y, max_y,
                                    min_z, intersect_start_z))
        if extends_right_z:
            non_overlapping.append((intersect_start_x, intersect_end_x,
                                    intersect_end_y, max_y,
                                    intersect_end_z, max_z))

    # 3
    if extends_left_x and extends_left_y and extends_left_z:
        non_overlapping.append((min_x, intersect_start_x,
                                min_y, intersect_start_y,
                                min_z, intersect_start_z))
    if extends_left_x and extends_left_y and extends_right_z:
        non_overlapping.append((min_x, intersect_start_x,
                                min_y, intersect_start_y,
                                intersect_end_z, max_z))
    if extends_left_x and extends_right_y and extends_left_z:
        non_overlapping.append((min_x, intersect_start_x,
                                intersect_end_y, max_y,
                                min_z, intersect_start_z))
    if extends_left_x and extends_right_y and extends_right_z:
        non_overlapping.append((min_x, intersect_start_x,
                                intersect_end_y, max_y,
                                intersect_end_z, max_z))
    if extends_right_x and extends_left_y and extends_left_z:
        non_overlapping.append((intersect_end_x, max_x,
                                min_y, intersect_start_y,
                                min_z, intersect_start_z))
    if extends_right_x and extends_left_y and extends_right_z:
        non_overlapping.append((intersect_end_x, max_x,
                                min_y, intersect_start_y,
                                intersect_end_z, max_z))
    if extends_right_x and extends_right_y and extends_left_z:
        non_overlapping.append((intersect_end_x, max_x,
                                intersect_end_y, max_y,
                                min_z, intersect_start_z))
    if extends_right_x and extends_right_y and extends_right_z:
        non_overlapping.append((intersect_end_x, max_x,
                                intersect_end_y, max_y,
                                intersect_end_z, max_z))
    return overlapping, non_overlapping
