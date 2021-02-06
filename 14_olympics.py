import time
import re


def analyse_line(string):
    data_dict = {}
    pattern = r'(\w+) can fly (\d+) km/s for (\d+) .+ (\d+) .+'
    matches = re.match(pattern, string)
    data_dict['name'] = matches.group(1)
    data_dict['speed'] = int(matches.group(2))
    data_dict['trav_time'] = int(matches.group(3))
    data_dict['rest_time'] = int(matches.group(4))
    data_dict['tot_time'] = data_dict['trav_time'] + data_dict['rest_time']
    return data_dict


def parse_data(inp_file='Day_14/14_input.txt'):
    input_data = []
    with open(inp_file, 'r') as f:
        for line in f:
            input_data.append(analyse_line(line))

    return input_data


def distance_covered(n_secs, reindeer_data):
    """Calculate the distance covered by reindeer
    at the end of n_secs"""
    dist = 0
    state = 1
    cur_time = 0
    while cur_time < n_secs:
        time_rem = n_secs - cur_time
        if state:
            if reindeer_data['trav_time'] > time_rem:
                time_inc = time_rem
            else:
                time_inc = reindeer_data['trav_time']
            dist += reindeer_data['speed'] * time_inc
            state = 0
        else:
            time_inc = reindeer_data['rest_time']
            state = 1

        cur_time += time_inc
    
    return dist


def find_ren_list_max(dist_covered):
    """Find list of reindeers in thea lead"""
    max_dist = max(dist_covered.values())
    ren_list = []
    for ren, dist in dist_covered.items():
        if dist == max_dist:
            ren_list.append(ren)
    return ren_list


def points_received(n_secs, reindeer_datas):
    dist_covered = {}
    pts_received = {}
    ren_state = {}
    for reindeer_stat in reindeer_datas:
        dist_covered[reindeer_stat['name']] = 0
        pts_received[reindeer_stat['name']] = 0
        ren_state[reindeer_stat['name']] = 1

    curr_time = 0
    while curr_time < n_secs:
        for ren_stats in reindeer_datas:
            ren_name = ren_stats['name']
            time_pos = curr_time % ren_stats['tot_time'] 
            if ren_state[ren_name]:
                dist_covered[ren_name] += ren_stats['speed']
            # Change reindeer state
            if time_pos == ren_stats['trav_time'] - 1:
                ren_state[ren_name] = 0
            elif time_pos == ren_stats['tot_time'] - 1:
                ren_state[ren_name] = 1

        # Award a point to leading reindeer
        lead_ren_list = find_ren_list_max(dist_covered)
        for lead_ren in lead_ren_list:
            pts_received[lead_ren] += 1 
        curr_time += 1

    return pts_received


def main():
    target_time = 2503

    reindeer_stats = parse_data()

    distance_list = []
    for reindeer_stat in reindeer_stats:
        distance_list.append(distance_covered(target_time, reindeer_stat))

    print(max(distance_list))
    
    points = points_received(target_time, reindeer_stats)
    print(max(points.values()))


def testcase():
    print('Testing Functions')
    test_file = 'Day_14/14_test.txt'
    test_string = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'
    expected_parse = [{'name': 'Comet', 'speed': 14, 
                       'trav_time': 10, 'rest_time': 127,
                       'tot_time': 137},
                      {'name': 'Dancer', 'speed': 16, 
                      'trav_time': 11, 'rest_time': 162,
                      'tot_time': 173}]
    
    assert analyse_line(test_string) == expected_parse[0]
    print('Func analyse_line:      Pass')
    assert parse_data(test_file) == expected_parse
    print('Func parse_data:        Pass')

    assert distance_covered(1, expected_parse[0]) == 14
    assert distance_covered(1, expected_parse[1]) == 16
    assert distance_covered(10, expected_parse[0]) == 140
    assert distance_covered(10, expected_parse[1]) == 160

    assert distance_covered(1000, expected_parse[0]) == 1120
    assert distance_covered(1000, expected_parse[1]) == 1056
    print('Func distance_covered:  Pass')

    dist_covered_test = {'Comet': 1, 'Dancer': 10}
    assert find_ren_list_max(dist_covered_test) == ['Dancer']
    dist_covered_test = {'Comet': 10, 'Dancer': 1}
    assert find_ren_list_max(dist_covered_test) == ['Comet']
    dist_covered_test = {'Comet': 10, 'Dancer': 10, 'Vixen': 10}
    assert find_ren_list_max(dist_covered_test) == ['Comet', 'Dancer', 'Vixen']
    print('Func find_ren_list_max: Pass')

    expected_pts = {'Comet': 312, 'Dancer': 689}
    assert points_received(1000, expected_parse) == expected_pts
    print('Func points_received:   Pass')
    print('Tests Completed\n')


if __name__ == '__main__':
    testcase()
    start1 = time.time()
    main()
    print(f'Part one and two finished in {time.time() - start1} s')
