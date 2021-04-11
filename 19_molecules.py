import time
import re
import random


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


def find_steps(repl_list, target_med):
    """Find nnumber of steps to go from 'e' to target_med.
    Slow and does not work!!!"""
    med_len = len(target_med)
    step = 1

    set_new_med_list = set(replace_mol(repl_list, 'e'))

    while target_med not in set_new_med_list:
        step += 1
        new_med_list = []

        for new_med in set_new_med_list:
            repl_med_list = replace_mol(repl_list, new_med)
            new_med_list.extend(repl_med_list)

        set_new_med_list = set(new_med_list)

        filtered_med_list = []
        for new_med in set_new_med_list:
            # Remove meds that exceed target length
            if len(new_med) <= med_len:
                filtered_med_list.append(new_med)
        set_new_med_list = set(filtered_med_list)
        print(len(set_new_med_list))

    return step


def find_steps2(repl_list, target_med):
    """Tries random replacements until 'e'. Works but not a good solution.
    Does not work for test case 2."""

    random.shuffle(repl_list)
    final_med = target_med
    count = 0
    while final_med != 'e':
        present_med = final_med
        for repl, pat in repl_list:
            if pat in final_med:
                final_med = final_med.replace(pat, repl, 1)
                # print(final_med)
                count += 1
        if present_med == final_med:
            # Reinitialize the loop
            print('Reinitializing')
            # input('Continue?')
            count = 0
            random.shuffle(repl_list)
            final_med = target_med
        # print(final_med)

    return count


def test_read_file():
    f_names = ['Day_19/19_test.txt', 'Day_19/19_test2.txt']

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
    f_names = ['Day_19/19_test.txt', 'Day_19/19_test2.txt']

    repl, med = read_file(f_names[0])
    new_med_list = replace_mol(repl, med)
    assert len(set(new_med_list)) == 4

    repl, med = read_file(f_names[1])
    new_med_list = replace_mol(repl, med)
    assert len(set(new_med_list)) == 7


def test_find_steps():
    repl_list, med = read_file(f_name='Day_19/19_test.txt')
    repl_list.append(('e', 'H'))
    repl_list.append(('e', 'O'))

    step = find_steps2(repl_list, med)
    assert step == 3


def main():
    start1 = time.time()
    repl_list, med = read_file()
    new_med_list = replace_mol(repl_list, med)
    print(len(set(new_med_list)))
    print(f'Part 1 Time: {time.time() - start1}')

    start2 = time.time()
    steps = find_steps2(repl_list, med)
    print(steps)
    print(f'Part 2 Time: {time.time() - start2}')


if __name__ == '__main__':
    main()
