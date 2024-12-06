import pdb
import itertools

with open("pages.txt", "r") as file:
    lines = file.readlines()

page_map = {}
for line in lines:
    a = line.strip().split("|")
    page_map[int(a[0])] = []

for line in lines:
    a = line.strip().split("|")
    page_map[int(a[0])].append(int(a[1]))

with open("updates.txt", "r") as file:
    lines = file.readlines()

updates = []
for line in lines:
    a = line.strip().split(",")
    a = [int(item) for item in a]
    updates.append(a)

bad_pages = []
for update in updates:
    for i in range(len(update)):
        for page in page_map[update[i]]:
            arr = update[i + 1:]
            pdb.set_trace()

bad_pages.sort()
bad_pages = list(bad_pages for bad_pages, _ in itertools.groupby(bad_pages))

print(len(updates))
for page in bad_pages:
    updates.remove(page)
print(len(updates))


def find_middle_element(arr):
    n = len(arr)
    middle_index = n // 2
    if n % 2 != 0:
        middle_element = arr[middle_index]
    else:
        middle_element = (arr[middle_index - 1], arr[middle_index])

    return middle_element


# middle_page_numbers = []
# for updates in correct_updates:
#     middle_page = int(find_middle_element(updates))
#     middle_page_numbers.append(middle_page)

# print(sum(middle_page_numbers))
