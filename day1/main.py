import pdb

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


for n in range(len(left_list)):
    left_n = left_list[n]
    right_n = right_list[n]
    if (left_n > right_n):
        distances.append(left_n - right_n)
    else:
        distances.append(right_n - left_n)

print("Part 1")
print("distances        : ", sum(distances))


for number in left_list:
    similarity_list.append(number * right_list.count(number))

print("Part 2")
print("similarity score : ", sum(similarity_list))
