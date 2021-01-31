import time
import itertools
import re


def parse_line(string):
    pat = r'(\w+) .+ (lose|gain) (\d+) .+ (\w+).'
    match_obj = re.match(pat, string)
    main_per = match_obj.group(1)
    val = int(match_obj.group(3))
    if match_obj.group(2) == 'lose':
        val = val * -1
    nei_per = match_obj.group(4)
    return main_per, nei_per, val


def parse_file(inp_file='Day_13/13_input.txt'):
    relation_data = {}

    with open(inp_file, 'r') as f:
        for line in f:
            per1, per2, val1 = parse_line(line)
            relation_data.setdefault(per1, {})
            relation_data[per1][per2] = val1
    
    return relation_data


def calculate_score(first_guest, order, rel_dat):
    '''Calculate forward score for an arrangement'''
    score = 0
    for per1, per2 in zip(order, order[1:]):
        score += rel_dat[per1][per2]
    score += rel_dat[first_guest][order[0]]
    score += rel_dat[order[-1]][first_guest]
    return score


def calculate_score_helper(first_guest, order, rel_dat):
    '''Calculate score forward and backward'''
    score1 = calculate_score(first_guest, order, rel_dat)
    score2 = calculate_score(first_guest, order[::-1], rel_dat)
    return score1 + score2


def find_table_max_score(relation_data):
    '''Go through each permutation and find max score'''
    # Find all guest names
    guest_list = list(relation_data.keys())
    # Remove one guest to reduce permutations
    first_guest = guest_list.pop()
    max_val = 0
    for arrgnmt in itertools.permutations(guest_list):
        arrgnmt_val = calculate_score_helper(first_guest, 
                                             arrgnmt, 
                                             relation_data)
        if arrgnmt_val > max_val:
            max_val = arrgnmt_val
    return max_val


def add_self(relation_data):
    '''Add 'Me' to the guest list'''
    guest_list = relation_data.keys()
    relation_data.setdefault('Me', {})

    for per in guest_list:
        relation_data['Me'][per] = 0
        relation_data[per]['Me'] = 0

    return relation_data


def main():
    rel_dat = parse_file()
    print('Part 1:', find_table_max_score(rel_dat))

    new_rel_dat = add_self(rel_dat)
    print('Part 2:', find_table_max_score(new_rel_dat))


def testcase():
    '''Test Cases'''
    print('Running Tests...')

    test_string = 'David would lose 7 happiness units by sitting next to Bob.'
    per1, per2, val1 = parse_line(test_string)
    assert per1 == 'David'
    assert per2 == 'Bob'
    assert val1 == -7
    print('Function: parse_line Pass')

    parse_result = {'Alice': {'Bob': 54, 'Carol': -79},
                    'Bob'  : {'David': -63, 'Alice': 83}}
    rel_test = parse_file(inp_file='Day_13/13_test.txt')
    for key, values in parse_result.items():
        for per2, val in values.items():
            assert rel_test[key][per2] == val
    print('Function: parse_file Pass')
    
    test_arrangement = ['David', 'Alice', 'Bob', 'Carol']
    test_score = calculate_score_helper(test_arrangement[0], 
                                        test_arrangement[1:],
                                        rel_test)
    assert test_score == 330
    print('Function: calculate_score Pass')

    test_answer = find_table_max_score(rel_test)
    assert test_answer == 330
    print('Function: find_table_max_score Pass')

    print('All Test Completed')


if __name__ == '__main__':
    testcase()
    start1 = time.time()
    main()
    print(f'Part one and two finished in {time.time() - start1}')
