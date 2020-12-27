import time
import re


def check_three_vowel(string):
    pat = r'[aeiou]'
    matches = re.findall(pat, string)
    return True if len(matches) >=3 else False


def check_double_letter(string):
    pat = r'(\w)\1'
    matches = re.findall(pat, string)
    return True if len(matches) >= 1 else False


def check_prohibited(string):
    pat = r'(ab|cd|pq|xy)'
    matches = re.findall(pat, string)
    return True if len(matches) == 0 else False


def check_two_pairs(string):
    pat = r'(\w{2}).*\1'
    matches = re.findall(pat, string)
    return True if len(matches) > 0 else False


def check_one_letter_repeat(string):
    pat = r'(\w).\1'
    matches = re.findall(pat, string)
    return True if len(matches) > 0 else False


def main(file_name='Day_5/5_input.txt'):
    with open(file_name, 'r') as f:
        input_data = map(str.strip, f.readlines())

    nice_count = 0
    for string in input_data:
        pattern_matches = [check_three_vowel(string),
                           check_double_letter(string),
                           check_prohibited(string)]
        if all(pattern_matches):
            nice_count += 1
    print(nice_count)


def main2(file_name='Day_5/5_input.txt'):
    with open(file_name, 'r') as f:
        input_data = map(str.strip, f.readlines())

    nice_count = 0
    for string in input_data:
        pattern_matches = [check_two_pairs(string),
                           check_one_letter_repeat(string)]
        if all(pattern_matches):
            nice_count += 1
    print(nice_count)


if __name__ == '__main__':
    start1 = time.time()
    # main(file_name='Day_5/5_test.txt') # Testcase
    main()
    print(f'Part one finished in {time.time() - start1}')

    start2 = time.time()
    # main2(file_name='Day_5/5_test2.txt') # Testcase
    main2()
    print(f'Part two finished in {time.time() - start2}')