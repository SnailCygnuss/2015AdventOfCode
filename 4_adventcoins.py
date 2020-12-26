import time
import hashlib


def main(inp_data='bgvyzdsv', part=1):
    num = 0
    h = hashlib.md5(f'{inp_data}{num}'.encode('utf-8')).hexdigest()
    if part == 1:
        start_string = '00000'
    elif part == 2:
        start_string = '000000'

    while not h.startswith(start_string):
        num = num + 1
        h = hashlib.md5(f'{inp_data}{num}'.encode('utf-8')).hexdigest()

    print(h)
    print(num)


def testcase():
    main('abcdef')
    main('pqrstuv')


if __name__ == '__main__':
    start1 = time.time()
    # testcase()
    main()
    main(part=2)
    print(f'Task Completed in {time.time() - start1}')