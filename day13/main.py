import re
from typing import Iterator
from sympy.core.numbers import Integer

import sympy as sp
from sympy.solvers import solve


def load_input_full(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


_input = load_input_full('input.txt')

machine_regex = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
)

a, b = sp.symbols('a b')


def get_equations(part_two: bool = False) -> Iterator[tuple[sp.Eq, sp.Eq]]:
    matches = machine_regex.findall(_input)
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


def part_one() -> int:
    spend = 0
    for equations in get_equations():
        solutions = solve_equations(equations)
        spend += get_cost(solutions[a], solutions[b])
    return spend


def part_two() -> int:
    spend = 0
    for equations in get_equations(part_two=True):
        solutions = solve_equations(equations)
        spend += get_cost(solutions[a], solutions[b])
    return spend


if __name__ == "__main__":
    print(part_one())
    print(part_two())
