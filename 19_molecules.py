import time
import re


def read_file(f_name='Day_19/19_input.txt'):
    """Read the input file"""

    repl_list = []
    with open(f_name, 'r') as f:

        for line in f:
            if line == '\n':
                continue
            match = re.match(r'(\w+) => (\w+)', line.rstrip())
            if match:
                repl_list.append((match.group(1), match.group(2)))
            else:
                medicine = line.rstrip()

    return repl_list, medicine


def replace_mol(repl_list, medicine):
    """Replaces molecule in the medicines
    and returns a new list"""

    new_med_list = []
    for pat, repl in repl_list:
        for m in re.finditer(pat, medicine):
            before = medicine[:m.start()]
            after = medicine[m.end():]
            new_med = before + repl + after
            new_med_list.append(new_med)
    
    return new_med_list


def test_read_file():
    f_names = ['Day_19/19_test.txt',
               'Day_19/19_test2.txt']

    for f in f_names:
        repl, med = read_file(f)
        assert repl == [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]
        assert med in ['HOH', 'HOHOHO']


def test_repl_mol():
    """Test the molecule replacing function"""

    repl_list, med = read_file(f_name='Day_19/19_test.txt')
    new_med_list = replace_mol(repl_list, med)
    assert new_med_list == ['HOOH', 'HOHO', 'OHOH', 'HOOH', 'HHHH']


def test_count_new_med():
    """Count the number of new medicines generated"""
    f_names = ['Day_19/19_test.txt',
               'Day_19/19_test2.txt']

    repl, med = read_file(f_names[0])
    new_med_list = replace_mol(repl, med)
    assert len(set(new_med_list)) == 4

    repl, med = read_file(f_names[1])
    new_med_list = replace_mol(repl, med)
    assert len(set(new_med_list)) == 7


def main():
    repl_list, med = read_file()
    new_med_list = replace_mol(repl_list, med)
    print(len(set(new_med_list)))


def main2():
    # repl_list, med = read_file()
    repl_list, med = read_file(f_name='Day_19/19_test.txt')
    med_len = len(med)
    step = 1
    repl_list.append(('e', 'H'))
    repl_list.append(('e', 'O'))
    set_new_med_list = set(replace_mol(repl_list, 'e'))
    print(set_new_med_list)

    # for _ in range(3):
    while med not in set_new_med_list:
        step += 1
        new_med_list = []

        for new_med in set_new_med_list:
            repl_med_list = replace_mol(repl_list, new_med)
            new_med_list.extend(repl_med_list)

        set_new_med_list = set(new_med_list)
        print(set_new_med_list)

        filtered_med_list = []
        for new_med in set_new_med_list:
            # Remove meds that exceed target length
            if len(new_med) <= med_len:
                filtered_med_list.append(new_med)
        set_new_med_list = set(filtered_med_list)

    print(step)

if __name__ == '__main__':
    start1 = time.time()
    # main()
    print(f'Part 1 finished in {time.time() - start1}')
    main2()
