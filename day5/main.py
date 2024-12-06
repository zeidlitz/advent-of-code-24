from collections import defaultdict
import pdb


with open("pages.txt", "r") as file:
    lines = file.readlines()

pages_txt = []
for line in lines:
    pages_txt.append(line)
    # a = line.strip().split("|")
    # page_map[int(a[0])] = []

# for line in lines:
#     a = line.strip().split("|")
    # page_map[int(a[0])].append(int(a[1]))

with open("updates.txt", "r") as file:
    lines = file.readlines()

updates_txt = []
for line in lines:
    updates_txt.append(line)


def parse_rules(rules):
    graph = defaultdict(list)
    for rule in rules:
        a, b = map(int, rule.split('|'))
        graph[a].append(b)
    return graph


def is_valid_update(update, graph):
    index_map = {page: i for i, page in enumerate(update)}
    for a in graph:
        for b in graph[a]:
            if a in index_map and b in index_map:
                if index_map[a] > index_map[b]:
                    continue
    return update


def validate_updates(pages_txt, updates_txt):
    graph = parse_rules(pages_txt)
    results = []
    for update in updates_txt:
        update_list = list(map(int, update.split(',')))
        results.append(is_valid_update(update_list, graph))
    return results


correct_updates = validate_updates(pages_txt, updates_txt)


def find_middle_element(arr):
    n = len(arr)
    middle_index = n // 2
    if n % 2 != 0:
        middle_element = arr[middle_index]
    else:
        middle_element = (arr[middle_index - 1], arr[middle_index])

    return middle_element


middle_page_numbers = []
for updates in correct_updates:
    middle_page = int(find_middle_element(updates))
    middle_page_numbers.append(middle_page)

print(sum(middle_page_numbers))
