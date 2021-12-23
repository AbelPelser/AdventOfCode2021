from puzzles.Day23.point_util import SideRoom


class Pod:
    def __init__(self, letter, moved_into_room=False):
        self.letter = letter
        self.moved_into_room = moved_into_room
        self.cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[letter]

    def copy(self):
        return Pod(self.letter, self.moved_into_room)

    def dump(self):
        return self.letter.upper() if not self.moved_into_room else self.letter.lower()

    def can_move_out_from(self, room: SideRoom):
        if not room.is_home_of(self):
            return True
