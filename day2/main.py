def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        lines = file.readlines()
    reports = []
    for line in lines:
        a = line.strip().split()
        a = [int(item) for item in a]
        reports.append(a)
    return reports


def is_safe(report):
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False


def part_one(input_data):
    reports = input_data
    safe_reports = [report for report in reports if is_safe(report)]
    return len(safe_reports)


def part_two(input_data):
    reports = input_data
    safe_reports_with_dampener = [report for report in reports if is_safe_with_dampener(report)]
    return len(safe_reports_with_dampener)


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
    test_solution(part_one, "example.txt", 2)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 4)
    print(f"Part 2 = {part_two(input_data)}")
