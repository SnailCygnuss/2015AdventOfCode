import time
import itertools


def return_coords(char):
    char_options = {'^': (1, 0),
                    'v': (-1, 0),
                    '>': (0, 1),
                    '<': (0, -1)}
    return char_options[char]


def find_presents_at_each_house(directions):
    present_count = {}
    present_coords = [0, 0]
    present_count[tuple(present_coords)] = 1

    for char in directions:
        
        movement = return_coords(char)
        present_coords[0] += movement[0]
        present_coords[1] += movement[1]
        # print(char)
        # print(present_coords)
        # input()
        present_count[tuple(present_coords)] = present_count.get(tuple(present_coords), 0) + 1

    # print(present_count)
    # print(f'Count: {len(present_count)}')
    return len(present_count), present_count


def find_presents_with_robo_santa(directions):
    # Part Two
    santa_dirs = itertools.compress(directions, itertools.cycle([1, 0]))
    robo_santa_dirs = itertools.compress(directions, itertools.cycle([0, 1]))

    _, santa_presents = find_presents_at_each_house(santa_dirs)
    _, robo_presents = find_presents_at_each_house(robo_santa_dirs)
    # Quick way to combine presents. Count delivered at each house is inaccurate
    combined_presents = {**santa_presents, **robo_presents}
    return len(combined_presents)


def main(file_name='Day_3/3_input.txt'):
    with open(file_name, 'r') as f:
        inp_data = f.readline().strip()

    part1, _ = find_presents_at_each_house(inp_data)
    print(f'Part One: {part1}')
    part2 = find_presents_with_robo_santa(inp_data)
    print(f'Part Two: {part2}')


def testcase():
    case1 = '>'
    case2 = '^>v<'
    case3 = '^v^v^v^v^v'
    print(find_presents_at_each_house(case1))
    print(find_presents_at_each_house(case2))
    print(find_presents_at_each_house(case3))
    print(find_presents_with_robo_santa('^v'))
    print(find_presents_with_robo_santa(case2))
    print(find_presents_with_robo_santa(case3))


if __name__ == '__main__':
    start1 = time.time()
    testcase()
    main()
    print(f'Completed in {time.time() - start1}')