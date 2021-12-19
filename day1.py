from puzzle_reader import get_puzzle


def get_count_measurements_larger_previous():
    count = 0
    data = [int(string) for string in get_puzzle(1, 1, False)]
    for i, number in enumerate(data):
        if i != 0:
            if number > data[i-1]:
                count += 1
    return count


def get_count_sums_are_larger_than_the_previous_sum():
    data = [int(string) for string in get_puzzle(1, 1, False)]
    max_id = len(data)
    sums = []
    count = 0

    for i in range(0, max_id - 1):
        if i + 1 < max_id - 1:
            sums.append(sum(data[i:i+3]))
            if i != 0 and sums[i] > sums[i-1]:
                count += 1
    return count


def main():
    count = get_count_sums_are_larger_than_the_previous_sum()
    print(f"{count=}")


if __name__ == "__main__":
    main()
