import time
import re


def sum_nums(str_chars):
    pat = r'([-]?\d+)'
    matches = re.findall(pat, str_chars)
    return sum(map(int, matches))


def recursively_count(inp_item):
    cnt = 0
    if type(inp_item) == type(list()):
        for itm in inp_item:
            cnt += recursively_count(itm)

    if type(inp_item) == type(dict()):
        # Go through each items in dictionary
        for _, val in inp_item.items():
            if val == 'red':
                # Exit and return 0
                return 0
        
        # If no red value found, add the values
        for _, val in inp_item.items():
            if type(val) in [type(dict()), type(list())]:
                cnt += recursively_count(val)
            elif type(val) == type(int()):
                cnt += val

    if type(inp_item) == type(int()):
        cnt += inp_item
    elif type(inp_item) == type(str()):
        cnt += 0

    return cnt
        

def main():
    with open('Day_12/12_input.txt', 'r') as f:
        inp_str = f.read().strip()
    eval_list = eval(inp_str)
    print(sum_nums(inp_str))
    print(recursively_count(eval_list))
    

def testcase():
    strings = ['[1,2,3]',
               '{"a":2,"b":4}',
               '[[[3]]]',
               '{"a":{"b":4},"c":-1}',
               '{"a":[-1,1]}',
               '[-1,{"a":1}]',
               '[]',
               '{}']
    results = [6, 6, 3, 3, 0, 0, 0, 0]

    for string, rslt in zip(strings, results):
        assert rslt == sum_nums(string)
        print('.', end='')
    print()

    strings2 = [[1,2,3],
                [1,{"c":"red","b":2},3],
                {"d":"red","e":[1,2,3,4],"f":5},
                [1,"red",5]]
    results2 = [6, 4, 0, 6]
    for string, rslt in zip(strings2, results2):
        assert rslt == recursively_count(string)
        print('.', end='')
    print()


if __name__ == '__main__':
    start1 = time.time()
    testcase()
    main()
    print(f'Part one finished in {time.time()- start1}')