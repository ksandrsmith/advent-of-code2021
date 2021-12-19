

def get_puzzle(day: int, part: int = 1, test: bool = True):
    if test:
        filename = f"puzzles/d{day}/test_data{part}.txt"
    else:
        filename = f"puzzles/d{day}/input_data{part}.txt"

    with open(filename, 'r') as f:
        data = f.readlines()
        return data
