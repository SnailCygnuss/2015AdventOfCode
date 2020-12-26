import time


def find_wrapping_paper(inp_data):
    dims = [int(x) for x in inp_data.split('x')]
    area = [dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0]]
    required_paper =  (2 * sum(area)) + min(area)
    return required_paper


def find_ribbon(inp_data):
    dims = [int(x) for x in inp_data.split('x')]
    dims.sort()
    vol = dims[0] * dims[1] * dims[2]
    ribbon_length = 2 * dims[0] + 2 * dims[1] + vol
    return ribbon_length


def main():
    with open('Day_2/2_input.txt', 'r') as f:
        input_data = map(str.strip, f.readlines())

    total_paper = 0
    total_ribbon = 0
    for dims in input_data:
        total_paper += find_wrapping_paper(dims)
        total_ribbon += find_ribbon(dims)
    print(total_paper)
    print(total_ribbon)


def testcase():
    case1 = '2x3x4'
    case2 = '1x1x10'
    print(find_wrapping_paper(case1))
    print(find_wrapping_paper(case2))
    print(find_ribbon(case1))
    print(find_ribbon(case2))


if __name__ == '__main__':
    start1 = time.time()
    testcase()
    main()
    print(f'Part One finished in {time.time() - start1}')