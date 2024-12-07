def parse_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line
            # do parsing if needed,
            # line.strip().split()
            # convert strings to ints
            # parsed_line = line.split(':')
            # v = parsed_line[1].strip().split(' ')
            # v = [int(item) for item in v]
    return lines


def part_one(input_data):
    return 0


def part_two(input_data):
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")
