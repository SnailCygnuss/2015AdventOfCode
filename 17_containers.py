import time


INP_DAT = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40,
           21, 7, 18, 43, 10, 47, 36, 24, 22, 40]


COMBOS = []


def combo_finder(inp_data=INP_DAT, tar=150, curr_list=[], level=0):
    if tar == 0:
        COMBOS.append(curr_list.copy())
        curr_list.pop()
        if len(inp_data) == 0:
            curr_list.pop()
    elif len(inp_data) == 0 and tar > 0:
        curr_list.pop()
    else:
        for idx, size in enumerate(inp_data):
            if level == 0:
                curr_list = []
            if idx == (len(inp_data) - 1) and size != tar:
                if len(curr_list) > 0:
                    curr_list.pop()
            elif size > tar:
                continue
            elif size <= tar:
                curr_list.append(size)
                combo_finder(inp_data[idx+1:], tar=tar-size,
                             curr_list=curr_list, level=level+1)


def find_min_number(list_of_containers):
    list_of_lens = []
    for container_list in list_of_containers:
        list_of_lens.append(len(container_list))

    return min(list_of_lens)


def find_number_of_min(list_of_containers):
    min_len = find_min_number(list_of_containers)
    count_of_min = 0
    for container_list in list_of_containers:
        if len(container_list) == min_len:
            count_of_min = count_of_min + 1

    return count_of_min


def print_combos_to_file(list_of_containers):
    with open('result.txt', 'w') as f:
        for com in list_of_containers:
            f.write(str(com))
            f.write('\n')


def main(inp_data=INP_DAT, tar=150):
    global COMBOS
    COMBOS = []
    combo_finder(inp_data, tar)
    # print_combos_to_file(COMBOS)
    print(len(COMBOS))
    print(find_number_of_min(COMBOS))


def test_main():
    test_data = [20, 15, 10, 5, 5]

    main(test_data, 25)
    assert len(COMBOS) == 4


def test_combo():
    test_data = [20, 15, 10, 5, 5]

    main(test_data, 25)
    assert COMBOS == [[20, 5], [20, 5], [15, 10], [15, 5, 5]]


def test_find_min():
    test_data = [20, 15, 10, 5, 5]

    main(test_data, 25)
    assert find_min_number(COMBOS) == 2


def test_find_num_min():
    test_data = [20, 15, 10, 5, 5]

    main(test_data, 25)
    assert find_number_of_min(COMBOS) == 3


if __name__ == '__main__':
    start1 = time.time()
    main()
    print(f'Part One and Two finished in {time.time() - start1}')
