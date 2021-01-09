import time


def get_next_number(num_str):
    new_num_list = []
    present_num = None
    count = 0
    for i in num_str:
        if present_num is None:
            present_num = i
            count = 1
        elif i != present_num:
            new_num_list.extend([str(count), present_num])
            present_num = i
            count = 1
        elif i == present_num:
            count += 1
    # Add the last set of numbers
    new_num_list.extend([str(count), present_num])
    new_num = ''.join(new_num_list)
    return new_num


def main(start_num, reps=50):
    num = start_num
    
    for _ in range(reps):
        num = get_next_number(num)
    print(len(num))


if __name__ == '__main__':
    start1 = time.time()
    # main(start_num='1') # testcase
    main(start_num='3113322113', reps=40)
    main(start_num='3113322113', reps=50)
    print(f'Part one and two finished in {time.time() - start1}')