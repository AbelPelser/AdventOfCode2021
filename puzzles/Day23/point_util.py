class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
        neighbour.neighbours.append(self)

    def get_possible_moves(self, moving_pod=None, current_cost=None):
        pass

    def remove_inhabitant(self):
        pass

    def get_inhabitant(self):
        pass

    def get_coordinate(self):
        return self.x, self.y

    def add_pod(self, inhabitant):
        pass

    def is_vacant(self):
        pass

    def accepts_pod(self):
        return self.is_vacant()

    def get_cost_of_move_into(self, cost_per_move):
        return cost_per_move

    def get_moves_from(self):
        yield from MoveFinder(self).find()


class Hallway(Point):
    def __init__(self, x, y, pod=None):
        super().__init__(x, y)
        self.pod = pod

    def remove_inhabitant(self):
        res = self.pod
        self.pod = None
        return res

    def get_inhabitant(self):
        return self.pod

    def add_pod(self, pod):
        self.pod = pod

    def is_vacant(self):
        return self.pod is None

    def copy(self):
        return Hallway(self.x, self.y, pod=(self.pod.copy() if self.pod else None))

    def dump(self):
        if self.pod:
            return self.pod.dump()
        return '.'


class SideRoom(Point):
    def __init__(self, x, y, home_of, size, pods=None):
        super().__init__(x, y)
        self.home_of = home_of
        self.size = size
        if pods is None:
            self.pods = []
        else:
            self.pods = pods

    def is_home_of(self, pod):
        return self.home_of == pod.letter

    def remove_inhabitant(self):
        return self.pods.pop()

    def get_inhabitant(self):
        return self.pods[-1]

    def add_pod(self, inhabitant):
        self.pods.append(inhabitant)

    def is_vacant(self):
        return len(self.pods) == 0

    def accepts_pod(self):
        return len(self.pods) < self.size

    def get_cost_of_move_into(self, cost_per_move):
        return (self.size - len(self.pods)) * cost_per_move

    def has_foreign_pods(self):
        for pod in self.pods:
            if not self.is_home_of(pod):
                return True
        return False

    def is_complete(self):
        return len(self.pods) == self.size and not self.has_foreign_pods()

    def copy(self):
        return SideRoom(self.x, self.y, self.home_of, self.size, pods=[pod.copy() for pod in self.pods])

    def dump(self):
        return ''.join((pod.dump() for pod in self.pods[::-1])).rjust(self.size, '.')


class Move:
    def __init__(self, from_point, to_point, cost):
        self.from_point = from_point
        self.to_point = to_point
        self.cost = cost


class MoveFinder:
    def __init__(self, starting_point):
        self.starting_point = starting_point
        self.starting_cost = 0
        self.current_known = {starting_point}
        self.cost_per_move = starting_point.get_inhabitant().cost
        if isinstance(starting_point, SideRoom):
            self.starting_cost += self.cost_per_move * (starting_point.size - len(starting_point.pods))

    def find(self, current_point=None, current_cost=None):
        if current_point is None:
            current_point = self.starting_point
        if current_cost is None:
            current_cost = self.starting_cost
        for neighbour in current_point.neighbours:
            if neighbour in self.current_known:
                continue
            self.current_known.add(neighbour)
            if neighbour.accepts_pod():
                cost_of_move = current_cost + neighbour.get_cost_of_move_into(self.cost_per_move)
                yield neighbour, cost_of_move
                if isinstance(neighbour, Hallway):
                    yield from self.find(current_point=neighbour, current_cost=cost_of_move)
