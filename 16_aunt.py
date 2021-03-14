import time


def parse_line(line):
    items = line.split(': ', 1)[1]
    items_list = items.split(', ')
    item_dict = {}
    for item in items_list:
        item_name, item_qty = item.split(': ')
        item_dict[item_name.strip()] = int(item_qty.strip())

    return item_dict


def test_parse_line():
    test_line = 'Sue 7: cars: 6, vizslas: 5, cats: 3'
    out_dict = {'cars': 6, 'vizslas': 5, 'cats': 3}

    assert parse_line(test_line) == out_dict


def check_inp_in_dict(inp_key, inp_val, item_dict, p=1):
    if inp_key in item_dict:
        if p == 2 and inp_key in ['cats', 'trees']:
            if item_dict[inp_key] <= inp_val:
                return False
        elif p == 2 and inp_key in ['pomeranians', 'goldfish']:
            if item_dict[inp_key] >= inp_val:
                return False
        elif item_dict[inp_key] != inp_val:
            return False
    return True


def test_check_inp_in_dict_true1():
    test_key = 'cats'
    test_val = 2
    inp_dict = {'cars': 2, 'dogs': 4, 'cat': 2}
    assert check_inp_in_dict(test_key, test_val, inp_dict)


def test_check_inp_in_dict_true2():
    test_key = 'cats'
    test_val = 2
    inp_dict = {'cars': 2, 'dogs': 4, 'cats': 2}
    assert check_inp_in_dict(test_key, test_val, inp_dict)


def test_check_inp_in_dict_false():
    test_key = 'cats'
    test_val = 2
    inp_dict = {'cars': 2, 'dogs': 4, 'cats': 3}
    assert not check_inp_in_dict(test_key, test_val, inp_dict)


def main(f_name='Day_16/16_input.txt'):

    aunt_sue_list = []
    with open(f_name, 'r') as f:
        for inp_line in f:
            aunt_sue_list.append(parse_line(inp_line))

    inp_ticker = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    matching_aunt_sues = [1] * len(aunt_sue_list)

    for tk_key, tk_val in inp_ticker.items():
        for idx, val in enumerate(matching_aunt_sues):
            if val == 0:
                continue
            if not check_inp_in_dict(tk_key, tk_val, aunt_sue_list[idx]):
                matching_aunt_sues[idx] = 0

    print('Part 1: Aunt Sue is ', end='')
    for idx, val in enumerate(matching_aunt_sues):
        if val == 1:
            print(idx + 1)

    matching_aunt_sues2 = [1] * len(aunt_sue_list)

    for tk_key, tk_val in inp_ticker.items():
        for idx, val in enumerate(matching_aunt_sues2):
            if val == 0:
                continue
            if not check_inp_in_dict(tk_key, tk_val, aunt_sue_list[idx], p=2):
                matching_aunt_sues2[idx] = 0

    print('SomethingPart 2: Aunt Sue is ', end='')
    for idx, val in enumerate(matching_aunt_sues2):
        if val == 1:
            print(idx + 1)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Part One and Two finished in {time.time() - start}')
