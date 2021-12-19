from puzzle_reader import get_puzzle


class Line:
    start: (int, int)
    end: (int, int)

    def __init__(self, start: (int, int), end: (int, int)):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start} -> {self.end}"

    def get_points(self):
        points: list = []
        if self.start[0] == self.end[0]:
            x = self.start[0]
            for y in range(min((self.start[1], self.end[1])), max((self.start[1], self.end[1])) + 1):
                coord = (x, y)
                points.append(coord)
        elif self.start[1] == self.end[1]:
            y = self.start[1]
            for x in range(min((self.start[0], self.end[0])), max((self.start[0], self.end[0])) + 1):
                coord = (x, y)
                points.append(coord)
        else:
            for x in range(min((self.start[0], self.end[0])), max((self.start[0], self.end[0])) + 1):
                for y in range(min((self.start[1], self.end[1])), max((self.start[1], self.end[1])) + 1):
                    coord = (x, y)
                    if coord == self.start or (x - self.start[0] != 0 and abs((y - self.start[1])/(x - self.start[0])) == 1):
                        points.append(coord)
        return points

    def is_horizontal_or_vertical(self):
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]


def get_count_dangerous_points():
    """Consider only horizontal and vertical lines. At how many points do at least two lines overlap?"""

    puzzle = get_puzzle(5, 1, False)

    lines: list[Line] = []

    for line in puzzle:
        start, end = line.split("->")
        start = tuple(int(coord) for coord in tuple(start.split(',')))
        end = tuple(int(coord) for coord in tuple(end.split(',')))
        lines.append(Line(start, end))

    max_x = max([line.start[0] for line in lines]+[line.end[0] for line in lines])
    max_y = max([line.start[1] for line in lines]+[line.end[1] for line in lines])

    map_points: list[list[int]] = [[0 for i in range(max_y+1)] for j in range(max_x+1)]

    count = 0

    for line in lines:
        if line.is_horizontal_or_vertical():
            for point in line.get_points():
                x, y = point
                map_points[x][y] += 1
                if map_points[x][y] == 2:
                    count += 1

    return count


def get_all_dangerous_points():
    """Consider all the lines. At how many points do at least two lines overlap?"""

    puzzle = get_puzzle(5, 1, False)

    lines: list[Line] = []

    for line in puzzle:
        start, end = line.split("->")
        start = tuple(int(coord) for coord in tuple(start.split(',')))
        end = tuple(int(coord) for coord in tuple(end.split(',')))
        lines.append(Line(start, end))

    max_x = max([line.start[0] for line in lines] + [line.end[0] for line in lines])
    max_y = max([line.start[1] for line in lines] + [line.end[1] for line in lines])

    map_points: list[list[int]] = [[0 for i in range(max_y + 1)] for j in range(max_x + 1)]

    count = 0

    for line in lines:
        for point in line.get_points():
            x, y = point
            map_points[x][y] += 1
            if map_points[x][y] == 2:
                count += 1

    return count


def main():
    print(get_all_dangerous_points())


if __name__ == '__main__':
    main()
