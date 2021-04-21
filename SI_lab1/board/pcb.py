from copy import copy

from board.path import Path, add_point_dislocation
from board.segment import Direction


class PCB:
    def __init__(self, points_list, width, height):
        self.points_list = points_list
        self.width = width
        self.height = height
        self.quality = 0
        self.paths_list = []
        self.board = []

    def create_clean_board(self):
        self.board = []
        for h in range(self.height):
            self.board.append([])
            for w in range(self.width):
                self.board[h].append(0)

    def assign_points(self):
        for point in self.points_list:
            self.paths_list.append(Path(point[0], point[1]))

    def create_random_solution(self):
        self.quality = 0
        for my_path in self.paths_list:
            self.creat_random_path_solution(my_path)
        self.repair_paths()

    def creat_random_path_solution(self, path, condition=False):
        if not condition:
            path.current_position = copy(path.start_point)
            path.segments = []
        direction_multiply = 1
        while not (path.current_position[0] == path.end_point[0] and path.current_position[1] == path.end_point[1]):
            possible_directions = []
            for direct in Direction:
                if direct is Direction.up:
                    if (self.height - path.current_position[1] - 1) > 0:
                        if path.end_point[1] - path.current_position[1] > 0:
                            for i in range(direction_multiply):
                                possible_directions.append(direct)
                        possible_directions.append(direct)
                elif direct is Direction.down:
                    if path.current_position[1] > 0:
                        if path.end_point[1] - path.current_position[1] < 0:
                            for i in range(direction_multiply):
                                possible_directions.append(direct)
                        possible_directions.append(direct)
                elif direct is Direction.left:
                    if path.current_position[0] > 0:
                        if path.end_point[0] - path.current_position[0] < 0:
                            for i in range(direction_multiply):
                                possible_directions.append(direct)
                        possible_directions.append(direct)
                elif direct is Direction.right:
                    if (self.width - path.current_position[0] - 1) > 0:
                        if path.end_point[0] - path.current_position[0] > 0:
                            for i in range(direction_multiply):
                                possible_directions.append(direct)
                        possible_directions.append(direct)
            path.add_new_segment_to_path(possible_directions)
        self.__repair_path(path)

    def change_path_solution(self, path):
        last_correct_segment = -1
        condition = False
        point, last_correct_segment = path.find_first_intersection(self.board)
        if last_correct_segment != -1:
            path.segments = path.segments[:last_correct_segment + 1]
            condition = True
        self.creat_random_path_solution(path, condition)

    def checking_all_coordinates_on_pcb(self):
        for path_item in self.paths_list:
            actual_point = copy(path_item.start_point)
            self.board[actual_point[1]][actual_point[0]] += 1
            for segment_item in path_item.segments:
                for i in range(segment_item.length):
                    actual_point = add_point_dislocation(actual_point, segment_item.direction)
                    self.board[actual_point[1]][actual_point[0]] += 1

    def evaluate_board(self):
        self.checking_all_coordinates_on_pcb()
        self.quality = 0
        for path_item in self.paths_list:
            path_item.count_intersections(self.board)
            path_item.evaluate_path()
            self.quality += path_item.quality

    def check_intersections(self):
        intersections = 0
        for path in self.paths_list:
            paths_intersections = path.intersections_amount
            intersections += paths_intersections
            if paths_intersections > 0:
                print(intersections, "intersections on path")
                return False
        return True

    def repair_paths(self):
        for p in self.paths_list:
            self.__repair_path(p)

    def __repair_path(self, path):
        segments_to_remove = []
        i = 0
        while i < len(path.segments) - 1:
            fst_segment = path.segments[i]
            scd_segment = path.segments[i + 1]
            if fst_segment.direction == Direction.up and scd_segment.direction == Direction.down:
                i += self.__repair(fst_segment, scd_segment, segments_to_remove, i)
            elif fst_segment.direction == Direction.down and scd_segment.direction == Direction.up:
                i += self.__repair(fst_segment, scd_segment, segments_to_remove, i)
            elif fst_segment.direction == Direction.left and scd_segment.direction == Direction.right:
                i += self.__repair(fst_segment, scd_segment, segments_to_remove, i)
            elif fst_segment.direction == Direction.right and scd_segment.direction == Direction.left:
                i += self.__repair(fst_segment, scd_segment, segments_to_remove, i)
            i += 1
        for j in range(len(segments_to_remove), 0, -1):
            del path.segments[segments_to_remove[j - 1]]

    def __repair(self, fst_segment, scd_segment, segments, i):
        difference = fst_segment.length - scd_segment.length
        if difference > 0:
            fst_segment.length = difference
            segments.append(i + 1)
            return 1
        elif difference < 0:
            segments.append(i)
            scd_segment.length = difference * -1
            return 0
        elif difference == 0:
            segments.append(i)
            segments.append(i + 1)
            return 1
