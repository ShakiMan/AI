class ReadData:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file


    def get_data(self):
        data_separator = ';'
        file = open(self.path_to_file, "r")
        first_row_data = file.readline().split(data_separator)
        width = int(first_row_data[0])
        height = int(first_row_data[1])
        points = []
        for row in file:
            row_data = row.split(data_separator)
            points.append([[int(row_data[0]), int(row_data[1])],
                           [int(row_data[2]), int(row_data[3])]])

        return width, height, points
