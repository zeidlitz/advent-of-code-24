import re

with open("input.txt", "r") as file:
    input_string = file.read()

result = []
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(pattern, input_string)

for match in matches:
    result.append(int(match[0]) * int(match[1]))

print("sum part 1 : ", sum(result))

pattern = r"(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\))|(\bdo\(\))|(\bdon't\(\))"

matches = re.findall(pattern, input_string)

enabled = True
valid_mul_matches = []

for match in matches:
    mul_match, do_match, dont_match = match
    if dont_match:
        enabled = False
    elif do_match:
        enabled = True
    elif mul_match and enabled:
        valid_mul_matches.append(mul_match)

result_sum = sum(
    int(x) * int(y)
    for mul in valid_mul_matches
    for x, y in [re.findall(r"\d{1,3}", mul)]
)

print("sum part 2 : ", result_sum)
