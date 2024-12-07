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


if __name__ == "__main__":
    input_data = parse_input()
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")
```

## testing

todo, add some way to do unit testing of certain expectations. Maybe add some assertions or similar things? Maybe pytest or another test framework could be usefull?

## running

I have been running everything with python3 doing direct interpertation of the source file,

example

```bash
python3 main.py

```
