import re
import time


def bswitch(num):
    num = ['0' if c=='1' else '1' for c in f'{num:016b}']
    num = int(''.join(num), 2)
    return num


def and_or_shift(val1, val2, operation):
    if operation == 'AND':
        return val1 & val2
    elif operation == 'OR':
        return val1 | val2
    elif operation == 'LSHIFT':
        return val1 << val2
    elif operation == 'RSHIFT':
        return val1 >> val2


calculated_var_value = {}
def get_var_value(var, var_values):
    if var in calculated_var_value:
        return calculated_var_value[var]
    
    if var not in var_values:
        calculated_var_value[var] = int(var)
    else:
        value = var_values[var]
        if len(value) == 1:
            calculated_var_value[var] = get_var_value(value[0], var_values)
        elif len(value) == 2:
            if value[0] == 'NOT':
                cal_value = get_var_value(value[1], var_values)
                calculated_var_value[var] = bswitch(cal_value)
        elif len(value) == 3:
            val1 = get_var_value(value[0], var_values)
            val2 = get_var_value(value[2], var_values)
            calculated_var_value[var] = and_or_shift(val1, val2, value[1])
    
    return calculated_var_value[var]
    

def parse_input(inp_dat):
    pat = r'(.+) -> (\w+)'
    var_values = {}
    for line in inp_dat:
        matches = re.search(pat, line)
        value, var = matches.groups()
        var_values[var] = value.split()

    return var_values


def main(input_file='Day_7/7_input.txt'):
    global calculated_var_value
    with open(input_file, 'r') as f:
        input_data = f.readlines()
    var_values = parse_input(input_data)
    a_value = get_var_value('a', var_values)
    print(a_value)
    calculated_var_value = {}
    calculated_var_value['b'] = a_value
    a_value_new = get_var_value('a', var_values)
    print(a_value_new)


if __name__ == '__main__':
    start1 = time.time()
    main()
    print(f'Part one and two finished in {time.time() - start1}')