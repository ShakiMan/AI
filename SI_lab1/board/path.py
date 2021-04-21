from copy import copy
from random import choice

from board.segment import Segment

INTERSECTIONS_EVALUATION_WEIGHT = 60
LENGTH_EVALUATION_WEIGHT = 4.5
SEGMENT_EVALUATION_WEIGHT = 6


def add_point_dislocation(point, direction):
    if direction is direction.up:
        point[1] += 1
    elif direction is direction.down:
        point[1] -= 1
    elif direction is direction.left:
        point[0] -= 1
    elif direction is direction.right:
        point[0] += 1
    return point


class Path:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.current_position = copy(self.start_point)
        self.segments = []
        self.length = 0
        self.segments_amount = 0
        self.intersections_amount = 0
        self.quality = 0

    def add_new_segment_to_path(self, possible_direction):
        self.add_one_move(choice(possible_direction))

    def add_one_move(self, direction):
        if len(self.segments) == 0:
            self.__add_segment(direction)
        else:
            current_segment = self.segments[len(self.segments) - 1]
            if current_segment.direction == direction:
                current_segment.add_length()
                self.add_current_point_dislocation(direction)
            else:
                self.__add_segment(direction)

        self.length += 1

    def add_current_point_dislocation(self, direction):
        add_point_dislocation(self.current_position, direction)

    def __add_segment(self, direction):
        self.segments.append(Segment(1, direction))
        self.segments_amount += 1
        self.add_current_point_dislocation(direction)

    def count_intersections(self, board):
        current_point = copy(self.start_point)
        self.intersections_amount = 0
        self.length = 0
        self.segments_amount = len(self.segments)
        for segment_item in self.segments:
            for i in range(segment_item.length):
                current_point = add_point_dislocation(current_point, segment_item.direction)
                self.length += 1
                if board[current_point[1]][current_point[0]] > 1:
                    self.intersections_amount += 1

    def evaluate_path(self):
        self.quality = INTERSECTIONS_EVALUATION_WEIGHT * self.intersections_amount + \
                       LENGTH_EVALUATION_WEIGHT * self.length + \
                       SEGMENT_EVALUATION_WEIGHT * self.segments_amount

    def find_first_intersection(self, board):
        current_checked_position = copy(self.start_point)
        self.current_position = copy(self.start_point)
        for i in range(len(self.segments)):
            for j in range(self.segments[i].length):
                current_checked_position = add_point_dislocation(current_checked_position, self.segments[i].direction)
                if board[current_checked_position[1]][current_checked_position[0]] > 1:
                    if j == 0:
                        return self.current_position, i - 1
                    elif j < self.segments[i].length:
                        self.segments[i].length = j
                        return self.current_position, i
                else:
                    self.current_position = add_point_dislocation(self.current_position, self.segments[i].direction)
        return self.current_position, -1
