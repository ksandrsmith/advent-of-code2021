from puzzle_reader import get_puzzle


class BingoBoard:
    rows: list[list[str]]
    columns: list[list[str]]
    last_number: int

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.set_columns()

    def __str__(self):
        return str(self.rows)

    def set_columns(self):
        self.columns = [["0" for i in range(len(self.rows))] for j in range(len(self.rows))]
        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                self.columns[j][i] = self.rows[i][j]

    def is_win(self):
        win = False
        for row in self.rows:
            if row == ["*" for i in range(len(row))]:
                win = True
                break

        for column in self.columns:
            if column == ["*" for i in range(len(column))]:
                win = True
                break

        return win

    def mark_number(self, number: str):
        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                if number == self.rows[i][j]:
                    self.rows[i][j] = "*"
                    break
        self.set_columns()
        self.last_number = int(number)
        return self.is_win()

    def get_unmarked_sum(self):
        unmarked_sum = 0
        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                if self.rows[i][j] != "*":
                    unmarked_sum += int(self.rows[i][j])
        return unmarked_sum

    def get_score(self):
        return self.get_unmarked_sum()*self.last_number


def get_array_of_boards(data):
    boards = []
    rows = []
    for row in data[2:]:
        if row != '\n':
            rows.append(row.split())
        if row == '\n':
            board = BingoBoard(rows=rows)
            boards.append(board)
            rows = []
    return boards


def get_win_score():
    data = get_puzzle(4, 1, False)
    numbers = data[0].split(',')
    boards = get_array_of_boards(data)

    for number in numbers:
        for i, board in enumerate(boards):
            if board.mark_number(number):
                print(f"{i}:{board}")
                print(board.last_number)
                return board.get_score()


def get_last_win_score():
    data = get_puzzle(4, 1, False)
    numbers = data[0].split(',')
    boards = get_array_of_boards(data)
    winners = []

    for number in numbers:
        winners.reverse()
        if len(winners) > 0:
            for winner in winners:
                boards.pop(winner)
            winners = []
        for i, board in enumerate(iter(boards)):
            if board.mark_number(number):
                if len(boards) == 1:
                    return board.get_score()
                winners.append(i)


def main():
    print(get_last_win_score())


if __name__ == '__main__':
    main()