import pdb


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        line = file.readline().strip()
    for char in line:
        res.append(int(char))
    return res


def convert_disk_format_to_dense_format(disk_format):
    dense_format = []
    file_index = 0
    for i in range(len(disk_format)):
        if i % 2 == 0:
            for i in range(disk_format[i]):
                dense_format.append(file_index)
            file_index += 1
        else:
            for i in range(disk_format[i]):
                dense_format.append(".")
    return dense_format


def left_shift_file_blocks(array):
    print("Shifting left, this will take some time...")
    n = len(array)
    for i in range(n - 1, -1, -1):
        if array[i] != '.':
            for j in range(n):
                if array[j] == '.':
                    array[j] = array[i]
                    array[i] = '.'
                    break
    array.pop(0)
    array.append(".")
    return array


def insert_data_block(memory_array, data, start_index, end_index):
    memory_array[start_index:end_index] = data
    return memory_array


def insert_data_blocks(memory_array, data):
    data_size = len(data)
    available_memory = 1
    for i in range(len(memory_array)):
        end_index = i + 1
        if (memory_array[i] == '.'):
            try:
                while (memory_array[i] == memory_array[end_index]):
                    available_memory += 1
                    end_index += 1
                    if available_memory == data_size:
                        print("inserting :", data)
                        memory_array = insert_data_block(memory_array, data, i, end_index)
            except IndexError:
                break
    return memory_array


def left_shift_files(memory_array):
    data_array = memory_array[::-1]
    data_array = [x for x in data_array if x != '.']
    data_size = 1
    for i in range(len(data_array)):
        end_index = i + 1
        try:
            pdb.set_trace()
            while (data_array[i] == data_array[end_index]):
                end_index += 1
                data_size += 1
            data = data_array[i:end_index]
            del data_array[i:end_index]
            memory_array = insert_data_blocks(memory_array, data)
        except IndexError:
            break
    return memory_array


def find_checksum(arr):
    checksum = 0
    for i in range(len(arr)):
        if (arr[i] == '.'):
            continue
        checksum += i * int(arr[i])
    return checksum


def part_one(input_data):
    dense_format = convert_disk_format_to_dense_format(input_data)
    shifted_format = left_shift_file_blocks(dense_format)
    checksum = find_checksum(shifted_format)
    return checksum


def part_two(input_data):
    dense_format = convert_disk_format_to_dense_format(input_data)
    # print("".join(str(x) for x in dense_format))
    shifted_format = left_shift_files(dense_format)
    # print("".join(str(x) for x in shifted_format))
    checksum = find_checksum(shifted_format)
    return checksum


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
    test_solution(part_one, "example.txt", 1928)
    # print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 2858)
    # print(f"Part 2 = {part_two(input_data)}")
