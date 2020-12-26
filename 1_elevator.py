import time


def find_floor(input_data):
    level = 0
    for char in input_data:
        level += 1 if char == '(' else -1
    return level


def find_first_basement(input_data):
    level = 0
    for idx, char in enumerate(input_data, start=1):
        level += 1 if char == '(' else -1
        if level == -1:
            pos = idx
            break
    return pos


def main():
    with open('Day_1/1_input.txt', 'r') as f:
        inp_dat = f.read()

    inp_dat = inp_dat.strip()
    print(find_floor(inp_dat))
    print(find_first_basement(inp_dat))


def testcase():
    case1 = '(())'
    case2 = '(()(()('
    case3 = '))((((('
    case4 = ')())())'
    print(find_floor(case1))
    print(find_floor(case2))
    print(find_floor(case3))
    print(find_floor(case4))

    case5 = '()())'
    print(find_first_basement(case5))


if __name__ == '__main__':
    start1 = time.time()
    testcase()
    main()
    print(f'Completed in {time.time()-start1}')