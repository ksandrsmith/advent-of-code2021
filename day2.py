from puzzle_reader import get_puzzle


def get_multiply_with_aim():
    commands = get_puzzle(2, 1, False)

    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        match command.split():
            case ["forward", value]:
                horizontal += int(value)
                if aim != 0:
                    depth += aim * int(value)
            case ["up", value]:
                aim -= int(value)
            case ["down", value]:
                aim += int(value)

    return horizontal*depth


def get_multiply():
    commands = get_puzzle(2, 1, False)

    horizontal = 0
    depth = 0

    for command in commands:
        match command.split():
            case ["forward", value]:
                horizontal += int(value)
            case ["up", value]:
                depth -= int(value)
            case ["down", value]:
                depth += int(value)

    return horizontal * depth


def main():
    print(get_multiply_with_aim())


if __name__ == "__main__":
    main()
