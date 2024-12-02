with open("input.txt", "r") as file:
    lines = file.readlines()

left_list = []
right_list = []
distances = []
similarity_list = []

for line in lines:
    left, right = line.strip().split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()


for number in range(len(left_list)):
    left_number = left_list[number]
    right_number = right_list[number]
    distances.append(abs(left_number - right_number))

print("Part 1")
print("distances        : ", sum(distances))

for number in left_list:
    similarity_list.append(number * right_list.count(number))

print("Part 2")
print("similarity score : ", sum(similarity_list))
