import time
import re


alfbts = 'abcdefghjkmnpqrstuvwxyz'
NEXT_LETTER = {}
for char, next_char in zip(alfbts, alfbts[1:]):
    NEXT_LETTER[char] = next_char
NEXT_LETTER[alfbts[-1]] = alfbts[0]


def next_pass(curr_pass):
    last_char = curr_pass[-1]
    next_char = NEXT_LETTER[last_char]
    if last_char in 'iol':
        next_char = NEXT_LETTER[next_char]

    if next_char == 'a':
        wrap_around_pass = next_pass(curr_pass[:-1])
    else:
        wrap_around_pass = curr_pass[:-1]
    new_pass = wrap_around_pass + next_char
    return new_pass


def check_increasing_letters(psswd):
    check_len = len(psswd) - 2
    for idx, char in enumerate(psswd):
        if char in 'fghijklmnoyz':
            continue
        if idx >= check_len:
            break
        next_char = NEXT_LETTER[char]
        next_char2 = NEXT_LETTER[next_char]
        if next_char == psswd[idx+1] and next_char2 == psswd[idx+2]:
            return True
    return False


def check_two_different(psswd):
    pat = r'.*(\w)\1.*(\w)\2'
    matches = re.match(pat, psswd)
    if matches:
        return True
    else:
        return False


def main(curr_pass='hxbxwxba'):
    while True:
        new_pass = next_pass(curr_pass)
        cond1 = check_increasing_letters(new_pass)
        cond2 = check_two_different(new_pass)
        if all([cond1, cond2]):
            print(new_pass)
            break
        else:
            curr_pass = new_pass

    return new_pass


def testcase():
    curr_pass = 'xx'
    for _ in range(5):
        print(curr_pass)
        curr_pass = next_pass(curr_pass)
    pass_check = ['hijklmmn',
                  'abbceffg',
                  'abbcegjk',
                  'abcdefgh',
                  'abcdffaa',
                  'ghijklmn',
                  'ghjaabcc']

    print('Check increasing')
    for p in pass_check:
        print(check_increasing_letters(p))

    print('Check double letters')
    for p in pass_check:
        print(check_two_different(p))

    main(curr_pass='abcdefgh')
    main(curr_pass='ghijklmn')


if __name__ == "__main__":
    start1 = time.time()
    # testcase()
    new_pass = main()
    main(curr_pass=new_pass)
    print(f'Part One and Two finished in {time.time()-start1}')
