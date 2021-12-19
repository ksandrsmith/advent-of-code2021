from puzzle_reader import get_puzzle


def get_power_consumption():

    data = get_puzzle(3, 1, False)

    sums = [[0, 0]]

    gam_rate = ""
    eps_rate = ""

    for string in data:
        for i, bit in enumerate(string):
            if bit == "0" or bit == "1":
                if len(sums) == i:
                    sums.append([0, 0])
                if bit == "0":
                    sums[i][0] += 1
                else:
                    sums[i][1] += 1

    for temp in sums:
        if temp[0] > temp[1]:
            gam_rate += "0"
            eps_rate += "1"
        else:
            gam_rate += "1"
            eps_rate += "0"

    gamma = int(gam_rate, 2)
    epsilon = int(eps_rate, 2)

    return gamma*epsilon


def find_oxygen_rating(data: list[str]):
    result = ""
    for i in range(0, len(data[0]) - 1):
        if len(data) == 1:
            result = data[0]
            break
        count = 0
        for string in data:
            count += int(string[i])
        if count >= len(data) - count:
            result += "1"
        else:
            result += "0"
        data = [string for string in data if string.startswith(result)]
    return result


def find_co2_scrubber_rating(data: list[str]):
    result = ""
    for i in range(0, len(data[0]) - 1):
        if len(data) == 1:
            result = data[0]
            break
        count = 0
        for string in data:
            count += int(string[i])
        if count >= len(data) - count:
            result += "0"
        else:
            result += "1"
        data = [string for string in data if string.startswith(result)]
    return result


def get_live_support_rating():
    data = get_puzzle(3, 1, False)
    oxygen_rating = find_oxygen_rating(data)
    co2_scrubber_rating = find_co2_scrubber_rating(data)

    return int(oxygen_rating, 2)*int(co2_scrubber_rating, 2)


def main():
    print(get_live_support_rating())


if __name__ == '__main__':
    main()