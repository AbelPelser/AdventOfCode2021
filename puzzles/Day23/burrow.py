from collections import defaultdict

from puzzles.Day23.pod import Pod
from puzzles.Day23.point_util import Hallway, SideRoom


class Burrow:
    def __init__(self):
        self.grid = defaultdict(dict)
        self.hallways = []
        self.rooms = []
        self.n_levels = None

    def setup_from_input(self, lines):
        self.n_levels = len(lines) - 3
        self.point_setup()
        hallway_str = lines[1][1:-1]
        for i in range(len(hallway_str)):
            self.hallways[i].pod = Pod(hallway_str[i]) if hallway_str[i] != '.' else None
        for room_i in range(len(self.rooms)):
            for line_i in range(len(lines) - 2, 1, -1):
                room = self.rooms[room_i]
                letter = lines[line_i][3 + 2 * room_i]
                if letter != '.':
                    room.add_pod(Pod(letter))
        self.init_neighbours()
        self.init_grid()

    def point_setup(self):
        self.hallways = [Hallway(x, 1) for x in range(1, 12)]
        self.rooms = [
            SideRoom(3, 2, 'A', self.n_levels),
            SideRoom(5, 2, 'B', self.n_levels),
            SideRoom(7, 2, 'C', self.n_levels),
            SideRoom(9, 2, 'D', self.n_levels)
        ]

    def init_neighbours(self):
        for i in range(1, len(self.hallways)):
            self.hallways[i - 1].add_neighbour(self.hallways[i])
        for room_i in range(len(self.rooms)):
            self.hallways[(room_i + 1) * 2].add_neighbour(self.rooms[room_i])

    def init_grid(self):
        for x in range(1, 12):
            self.grid[1][x] = self.hallways[x - 1]
        for i in range(len(self.rooms)):
            self.grid[2][3 + i * 2] = self.rooms[i]

    def is_finished(self):
        return all(room.is_complete() for room in self.rooms)

    def move(self, from_coord, to_coord):
        from_field = self.get_target_of_coord(from_coord)
        to_field = self.get_target_of_coord(to_coord)
        pod_to_move = from_field.remove_inhabitant()
        to_field.add_pod(pod_to_move)
        if isinstance(to_field, SideRoom):
            pod_to_move.moved_into_room = True

    def dump(self):
        s = '#############\n#'
        for hallway in self.hallways:
            s += hallway.dump()
        s += '#\n##'
        for i, level in enumerate(zip(*(room.dump() for room in self.rooms))):
            s += '#' + '#'.join(level) + '#'
            if i == 0:
                s += '##'
            s += '\n  '
        s += '#########'
        return s

    def move_is_legal(self, from_point, to_point):
        if any(isinstance(n, SideRoom) for n in to_point.neighbours):
            return False
        subject = from_point.get_inhabitant()
        if isinstance(to_point, SideRoom):
            if not to_point.is_home_of(subject) or to_point.has_foreign_pods():
                return False
        if isinstance(from_point, SideRoom):
            if from_point.is_home_of(subject) and not from_point.has_foreign_pods():
                return False
            if subject.moved_into_room:
                return False
        if isinstance(from_point, Hallway) and isinstance(to_point, Hallway):
            return False
        return True

    def get_all_possible_moves(self):
        for from_point in self.rooms + self.hallways:
            if from_point.is_vacant():
                continue
            for to_point, cost in from_point.get_moves_from():
                if self.move_is_legal(from_point, to_point):
                    yield cost, (from_point.get_coordinate(), to_point.get_coordinate())

    def get_target_of_coord(self, coord):
        x, y = coord
        return self.grid[y][x]

    def prioritize_moves(self, moves):
        remaining = []
        for cost, (from_point, to_point) in moves:
            from_target = self.get_target_of_coord(from_point)
            to_target = self.get_target_of_coord(to_point)
            subject = from_target.get_inhabitant()
            if isinstance(to_target, SideRoom) and to_target.is_home_of(subject):
                yield cost, (from_point, to_point)
            else:
                remaining.append((cost, (from_point, to_point)))
        remaining = sorted(remaining, key=lambda t: t[0])
        yield from remaining

    def copy(self):
        copy = Burrow()
        copy.n_levels = self.n_levels
        copy.hallways = [h.copy() for h in self.hallways]
        copy.rooms = [r.copy() for r in self.rooms]
        copy.init_neighbours()
        copy.init_grid()
        return copy
