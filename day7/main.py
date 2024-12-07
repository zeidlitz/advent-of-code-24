from itertools import product


def find_operator_combinations(numbers, target):
    if len(numbers) < 2:
        return 0
    operators = ['+', '*']

    def evaluate_left_to_right(ops, nums):
        result = nums[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += nums[i + 1]
            elif op == '*':
                result *= nums[i + 1]
        return result

    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_left_to_right(ops, numbers) == target:
            return target
    return 0


def get_list_from_file():
    data_map = {}
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            parsed_line = line.split(':')
            k = int(parsed_line[0])
            v = parsed_line[1].strip().split(' ')
            v = [int(item) for item in v]
            data_map[k] = v
    return data_map


def part_one(input_data):
    result = []
    for k in input_data:
        result.append(find_operator_combinations(input_data[k], k))
    result = [i for i in result if i != 0]
    return sum(result)


def part_two(input_data):
    return 0


if __name__ == "__main__":
    input_data = get_list_from_file()
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")
