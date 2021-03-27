import time
import itertools
import copy


def read_file(f_name='Day_18/18_input.txt'):

    with open(f_name, 'r') as f:
        data = []
        for line in f:
            row = []
            for char in line.strip():
                row.append(char)
            data.append(row)

    return data


def test_read_file():
    test_file = 'Day_18/18_test.txt'
    data = read_file(test_file)
    data_exp = ['.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..']
    data = [''.join(line) for line in data]

    assert data == data_exp


def find_no_neighbours(i, j, lights_data):
    """
    Find number of neighbouring lights
    that are turned for lights at (i,j)
    """

    num_neighbours = 0
    limit_x = len(lights_data)
    limit_y = len(lights_data[0])

    for x, y in itertools.product([-1, 0, 1], repeat=2):
        if x == 0 and y == 0:
            continue
        coord_x = i + x
        coord_y = j + y

        if 0 <= coord_x < limit_x and 0 <= coord_y < limit_y:
            neighbour = lights_data[coord_x][coord_y]

            if neighbour == '#':
                num_neighbours += 1

    return num_neighbours


def test_find_no_n():
    test_file = 'Day_18/18_test.txt'
    data = read_file(test_file)

    assert find_no_neighbours(0, 1, data) == 0
    assert find_no_neighbours(0, 2, data) == 3
    assert find_no_neighbours(1, 4, data) == 4
    assert find_no_neighbours(5, 2, data) == 3
    assert find_no_neighbours(5, 5, data) == 1


def count_lights(lights_data):
    """Count number of lights that are turned on"""
    no_lights = 0
    for row in lights_data:
        for light in row:
            if light == '#':
                no_lights += 1

    return no_lights


def test_count_lights():
    test_file = 'Day_18/18_test.txt'
    data = read_file(test_file)

    assert count_lights(data) == 15


def change_lights(lights_data):
    """Return the new state of lights"""
    new_state = copy.deepcopy(lights_data)

    for i, j in itertools.product(range(len(lights_data)), repeat=2):
        num_neighbours = find_no_neighbours(i, j, lights_data)
        curr_state = lights_data[i][j]

        if curr_state == '#' and num_neighbours not in [2, 3]:
            new_state[i][j] = '.'
        elif curr_state == '.' and num_neighbours == 3:
            new_state[i][j] = '#'

    return new_state


def print_lights(lights_data):
    for row in lights_data:
        print(''.join(row))
    print()


def test_change_lights():
    test_file = 'Day_18/18_test.txt'
    data = read_file(test_file)

    for _ in range(4):
        print_lights(data)
        data = change_lights(data)
    assert count_lights(data) == 4

    data = read_file(test_file)
    data[0][0] = '#'
    data[0][-1] = '#'
    data[-1][0] = '#'
    data[-1][-1] = '#'

    for _ in range(5):
        print_lights(data)
        data = change_lights(data)
        data[0][0] = '#'
        data[0][-1] = '#'
        data[-1][0] = '#'
        data[-1][-1] = '#'
    assert count_lights(data) == 17


def main():
    inp_data = read_file()

    for _ in range(100):
        inp_data = change_lights(inp_data)

    print('Part 1:', count_lights(inp_data))

    inp_data = read_file()
    inp_data[0][0] = '#'
    inp_data[0][-1] = '#'
    inp_data[-1][0] = '#'
    inp_data[-1][-1] = '#'

    for _ in range(100):
        inp_data = change_lights(inp_data)
        inp_data[0][0] = '#'
        inp_data[0][-1] = '#'
        inp_data[-1][0] = '#'
        inp_data[-1][-1] = '#'
    print('Part 2:', count_lights(inp_data))


if __name__ == '__main__':
    start1 = time.time()
    main()
    print(f'Part One and Two finished in {time.time() - start1}')
