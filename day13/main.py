import re
from typing import Iterator
from sympy.core.numbers import Integer

import sympy as sp
from sympy.solvers import solve


def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        return file.read()

# _input = load_input_full('input.txt')


machine_regex = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
)

a, b = sp.symbols('a b')


def get_equations(input_data, part_two: bool = False) -> Iterator[tuple[sp.Eq, sp.Eq]]:
    matches = machine_regex.findall(input_data)
    for match in matches:
        x1, y1, x2, y2 = int(match[0]), int(match[1]), int(match[2]), int(match[3])
        x3 = int(match[4]) + 10000000000000 if part_two else int(match[4])
        y3 = int(match[5]) + 10000000000000 if part_two else int(match[5])
        yield (
            sp.Eq((x1 * a) + (x2 * b), x3),
            sp.Eq((y1 * a) + (y2 * b), y3)
        )


def solve_equations(equations: tuple[sp.Eq, sp.Eq]):
    solutions = solve(equations, (a, b))
    return solutions


def get_cost(a: int | float, b: int | float) -> int:
    if a < 0 or b < 0:
        return 0
    if isinstance(a, Integer) and isinstance(b, Integer):
        return (a * 3) + b
    return 0


def part_one(input_data) -> int:
    spend = 0
    for equations in get_equations(input_data):
        solutions = solve_equations(equations)
        spend += get_cost(solutions[a], solutions[b])
    return spend


def part_two(input_data) -> int:
    spend = 0
    for equations in get_equations(input_data, part_two=True):
        solutions = solve_equations(equations)
        spend += get_cost(solutions[a], solutions[b])
    return spend


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
    test_solution(part_one, "example_part_one.txt", 480)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example_part_two.txt", 100)
    print(f"Part 2 = {part_two(input_data)}")
