## advent-of-code-24
A repository for hosting my advent of code solutions

## structure & assumptions
each solution resides in a:

```bash
main.py
```

and each problem input resides in

```bash
input.txt
```

both reside in a directory for the respective day.

the main function will search for input.txt in the same directory, so make sure it's in the leaf of the file

## boilerplate

The problems usually follow a structure of first needing to do some input parsing and later solving a part one and a part two for the input. The same input is usually for both parts.

Therefore each day I can reuse the following base structure to get a good starting point

```python
def parse_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
    return lines


def part_one(input_data):
    return 0


def part_two(input_data):
    return 0


def test_part_one(num):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input("example_part_one.txt")
    expected_output = num
    actual_output = part_one(example_input_data)

    if actual_output == expected_output:
        print(f"Test for part I : {GREEN}PASSED{RESET}")
    else:
        print(f"Test for part I : {RED}FAILED: expected {expected_output}, got {actual_output}{RESET}")


def test_part_two(num):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input("example_part_two.txt")
    expected_output = num
    actual_output = part_two(example_input_data)

    if actual_output == expected_output:
        print(f"Test for part II: {GREEN}PASSED{RESET}")
    else:
        print(f"Test for part II: {RED}FAILED: expected {expected_output}, got {actual_output}{RESET}")


if __name__ == "__main__":
    input_data = parse_input()
    test_part_one(0)
    print(f"Part 1 = {part_one(input_data)}")
    test_part_two(0)
    print(f"Part 2 = {part_two(input_data)}")
```

## testing

there are two tests for part one and part two that will expect a sepperate input file for each. 

```bash
example_part_{one/two}.txt
```

the test functions will require the user to send the expected output for these. Since the examples for each problem comes with a expected result this is a very good way to run the basic case and establish the base functionallity before attempting the personalized input. Right now they need to be updated in the source with the expected results. Might add some nicer way of doing this if I feel like it, but it works good for now. It's not super eligant that they both take two files as input and run two sepperate functions that are almost identical. I can probably find some way to remove some duplication. But for now it works for my needs.

## running

I have been running everything with python3 doing direct interpertation of the source file,

example

```bash
python3 main.py
```
