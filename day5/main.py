def parse_input(input_file="input.txt"):
    with open(input_file, 'r') as file:
        return file.read().splitlines()


def is_order_valid(instruction, rules):
    for A, B in rules:
        if A in instruction and B in instruction:
            index_a = instruction.index(A)
            index_b = instruction.index(B)
            if index_b < index_a:
                return False
    return True


def find_valid_order(instruction, rules):
    if len(instruction) == 1:
        return instruction

    for i in range(len(instruction)):
        current_instruction = instruction[:i] + instruction[i + 1:]
        if is_order_valid(current_instruction, rules):
            ordered = find_valid_order(current_instruction, rules)
            if ordered is not None:
                return [instruction[i]] + ordered
    return None


def sort_me(instruction, rules):
    i = 0
    while i != len(instruction):
        i = len(instruction)
        for rule in rules:
            A, B = rule[0], rule[1]
            if A not in instruction or B not in instruction:
                continue
            first_page = instruction.index(A)
            second_page = instruction.index(B)
            if first_page > second_page:
                i -= 1
                instruction.pop(first_page)
                instruction.insert(second_page, A)
    return instruction


def part_one(data_input):
    count = 0
    valid_instructions = []
    data_input = "\n".join(data_input)
    rules_input, instructions_input = data_input.split("\n\n", 1)
    rules = [(int(a), int(b)) for a, b in (line.split('|') for line in rules_input.splitlines())]
    for line in instructions_input.split("\n"):
        instruction = [int(page) for page in line.split(",")]
        if is_order_valid(instruction, rules):
            count += 1
            valid_instructions.append(line)
    return sum([int(instruction.split(",")[len(instruction.split(",")) // 2]) for instruction in valid_instructions])


def part_two(data_input):
    count = 0
    invalid_instructions = []
    data_input = "\n".join(data_input)
    rules_input, instructions_input = data_input.split("\n\n", 1)
    rules = [(int(a), int(b)) for a, b in (line.split('|') for line in rules_input.splitlines())]
    for line in instructions_input.split("\n"):
        instruction = [int(page) for page in line.split(",")]
        if not is_order_valid(instruction, rules):
            count += 1
            invalid_instructions.append(instruction)
    ordered_instructions = []
    for instruction in invalid_instructions:
        ordered_instruction = sort_me(instruction, rules)
        if ordered_instruction:
            ordered_instructions.append(ordered_instruction)
    return sum([instruction[len(instruction) // 2] for instruction in invalid_instructions])


def test_solution(func, input_data, result):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input(input_data)
    expected_output = result
    actual_output = func(example_input_data)

    if actual_output == expected_output:
        print(f"Test for {func.__name__} - {GREEN}PASSED{RESET}: expected {actual_output}, got {actual_output}")
    else:
        print(f"Test for {func.__name__} - {RED}FAILED{RESET}: expected {expected_output}, got {actual_output}")


if __name__ == "__main__":
    input_data = parse_input()
    test_solution(part_one, "example.txt", 143)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 123)
    print(f"Part 2 = {part_two(input_data)}")
