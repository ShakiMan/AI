import enum


class Segment:
    def __init__(self, length, direction):
        self.length = length
        self.direction = direction

    def add_length(self):
        self.length += 1


class Direction(enum.Enum):
    up = 1
    down = 2
    left = 3
    right = 4
