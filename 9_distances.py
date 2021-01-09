import time
import re
import itertools


def parse_line(line):
    pat = r'(\w+) to (\w+) = (\d+)'
    matches = re.match(pat, line).groups()

    dist_dict = {}
    pair1 = (matches[0], matches[1])
    pair2 = (matches[1], matches[0])
    dist_dict[pair1] = int(matches[2])
    dist_dict[pair2] = int(matches[2])
    return dist_dict, [matches[0], matches[1]]


def main(file_name='Day_9/9_input.txt'):
    distances = {}
    places = set()
    with open(file_name, 'r') as f:
        for line in f:
            dist_dict, nodes = parse_line(line)
            distances.update(dist_dict)
            places.update(nodes)

    dist_path = {}
    for sequence in itertools.permutations(places, len(places)):
        distance = 0
        for i in range(len(sequence)-1):
            path = (sequence[i], sequence[i+1])
            distance = distance + distances[path]
        dist_path[sequence] = distance
    
    print(f'Min = {min(dist_path.values())}')
    print(f'Max = {max(dist_path.values())}')


if __name__ == '__main__':
    start1 = time.time()
    # main(file_name='Day_9/9_test.txt') # TestCase
    main()
    print(f'Part one and two finished in {time.time() - start1}')

