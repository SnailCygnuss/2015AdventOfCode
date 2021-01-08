import time
import re


def open_file(file_name='Day_8/8_input.txt'):
    with open(file_name) as f:
        inp_dat = list(map(str.strip, f.readlines()))
    return inp_dat


def count_char(string):
    pat1 = r'(\\x[0-9a-f]{2})'
    pat2 = r'(\\\")'
    pat3 = r'(\\{2})'
    new_string = string.strip('"')
    new_string = re.sub(pat1, 'X', new_string)
    new_string = re.sub(pat2, 'X', new_string)
    new_string = re.sub(pat3, 'X', new_string)
    return len(new_string)


def count_char2(string):
    pat2 = r'(\\)'
    new_string = re.sub(pat2, '\\\\\\\\', string)
    
    pat1 = r'\"'
    new_string = re.sub(pat1, '\\\"', new_string)
    
    new_string = '"' + new_string + '"'
    
    return len(new_string)


def testcase():
    inp_dat = open_file('Day_8/8_test.txt')
    str_lit = list(map(len, inp_dat))
    str_mem = list(map(count_char, inp_dat))
    for i in range(len(str_lit)):
        print(f'{str_lit[i]} -> {str_mem[i]}')    
    print(sum(str_lit) - sum(str_mem))
    test_str = '"\\xa8br\\x8bjr\\""'
    print(f'{len(test_str)} -> {count_char(test_str)}')
    test_str2 = '"draes\\xa2n\\\\g\\x27ek\\"lj\\"\\\\viqych"'
    print(f'{len(test_str2)} -> {count_char(test_str2)}')
    print('Part 2')
    str_lit2 = list(map(count_char2, inp_dat))
    for i in range(len(str_lit2)):
        print(f'{str_lit[i]} -> {str_lit2[i]}')


def main():
    inp_data = open_file()
    str_lit = list(map(len, inp_data))
    str_mem = list(map(count_char, inp_data))
    print(f'Part One - {sum(str_lit) - sum(str_mem)}')

    str_lit2 = list(map(count_char2, inp_data))
    print(f'Part Two - {sum(str_lit2) - sum(str_lit)}')


if __name__ == '__main__':
    start1 = time.time()
    # testcase()
    main()
    print(f'Part one and two finished in {time.time() - start1}')