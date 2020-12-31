import time
import re
import itertools


def change_status(present_status, action):
    if action == 'on':
        return 1
    elif action == 'off':
        return 0
    elif action == 'toggle':
        return 0 if present_status == 1 else 1


def main(file_name='Day_6/6_input.txt'):
    light_status = {}
    pat = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'
    with open(file_name, 'r') as f:
        for instruction in f:
            match_obj = re.search(pat, instruction)
            act, x1, y1, x2, y2 = match_obj.groups()
            for coords in itertools.product(range(int(x1), int(x2)+1), 
                                            range(int(y1), int(y2)+1)):
                light_status[coords] = change_status(light_status.get(coords, 0), act)
    value_count = 0
    for val in light_status.values():
        value_count += val
    print(value_count)


def main2(file_name='Day_6/6_input.txt'):
    light_status = {}
    change_status2 = {'on': 1,
                      'off': -1,
                      'toggle': 2}
    pat = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'
    with open(file_name, 'r') as f:
        for instruction in f:
            match_obj = re.search(pat, instruction)
            act, x1, y1, x2, y2 = match_obj.groups()
            for coords in itertools.product(range(int(x1), int(x2)+1), 
                                            range(int(y1), int(y2)+1)):
                light_status[coords] = light_status.get(coords, 0) \
                                       + change_status2[act]
                if light_status[coords] < 0:
                    light_status[coords] = 0

    value_count = 0
    for val in light_status.values():
        value_count += val
    print(value_count)


if __name__ == '__main__':
    start1 = time.time()
    # main(file_name='Day_6/6_test.txt') # Test Case
    main()
    print(f'Part One finished in {time.time() - start1}')

    start2 = time.time()
    main2()
    print(f'Part Two finished in {time.time() - start2}')