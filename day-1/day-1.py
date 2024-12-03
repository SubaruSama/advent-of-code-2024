# Link: https://adventofcode.com/2024/day/1

result = []

def populate_lists(to_populate, mode):
    with open(to_populate, mode) as file:
        left_list = []
        right_list = []

        for line in file:
            values = line.strip().split()
            # print(values[0], values[1])

            left_list.append(int(values[0]))
            right_list.append(int(values[1]))

    return left_list, right_list

def lowest_value(given_list):
    index_lowest_value = given_list.index(min(given_list))
    lowest_value = given_list.pop(index_lowest_value)
    return lowest_value

def main():
    left_list, right_list = populate_lists("values.txt", "r")
    i = 0
    size_array = len(left_list) - 1

    while i <= size_array:
        left_lowest_value = lowest_value(left_list)
        # print(f"Left lowest value: {left_lowest_value}")

        right_lowest_value = lowest_value(right_list)
        # print(f"Right lowest value: {right_lowest_value}")

        result.append(abs(left_lowest_value - right_lowest_value))
        # print(f"Result so far(t): {result}")

        # print("===")
        i += 1
        # print(i)

    print(f"Sum of all: {sum(result)}")

if __name__ == "__main__":
    main()