import time
import re
import itertools


def format_inp(inp_str):
    inp_list = inp_str.strip().split('\n')
    inp_list = [x.strip() for x in inp_list]
    return inp_list


def parse_inp(inp_str):
    inp_list = format_inp(inp_str)
    pat = r'(\w+): \w+ (.{1,2}), \w+ (.{1,2}), \w+ (.{1,2}), \w+ (.{1,2}), \w+ (.{1,2})'
    features = ['cap', 'dur', 'fla', 'tex', 'cal']
    ingredients = {}
    for line in inp_list:
        match = re.match(pat, line)
        item_name = match.group(1)
        prop_dict = {}
        for idx, prop in enumerate(features, start=2):
            prop_dict[prop] = int(match.group(idx))
        ingredients[item_name] = prop_dict

    return ingredients


def find_product(ingredients, combo):
    sum_prop = [0, 0, 0, 0]
    for ing, qty in zip(ingredients.values(), combo):
        sum_prop[0] += ing['cap'] * qty
        sum_prop[1] += ing['dur'] * qty
        sum_prop[2] += ing['fla'] * qty
        sum_prop[3] += ing['tex'] * qty
    sum_prop = [x if x > 0 else 0 for x in sum_prop]
    prod = sum_prop[0] * sum_prop[1] * sum_prop[2] * sum_prop[3]
    return prod


def find_cals(ingredients, combo):
    cal_tot = 0
    for ing, qty in zip(ingredients.values(), combo):
        cal_tot += ing['cal'] * qty
    return cal_tot


def main(inp_str, cal_limit=None):
    ingredients = parse_inp(inp_str)

    max_limit = 100
    num_ingredients = len(ingredients)
    max_product = 0
    max_combo = None

    for combo in itertools.permutations(range(1, max_limit), num_ingredients):
        if sum(combo) != 100:
            continue
        if cal_limit is not None and find_cals(ingredients,
                                               combo) != cal_limit:
            continue
        product = find_product(ingredients, combo)
        if product > max_product:
            max_product = product
            max_combo = combo
    print(max_product)
    print(max_combo)
    return max_product


# Test functions ---------

test_str = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

test_format_inp_ret = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
]


def test_format_inp():
    assert format_inp(test_str) == test_format_inp_ret


test_parse_inp_ret = {
    'Butterscotch': {
        'cap': -1,
        'dur': -2,
        'fla': 6,
        'tex': 3,
        'cal': 8
    },
    'Cinnamon': {
        'cap': 2,
        'dur': 3,
        'fla': -2,
        'tex': -1,
        'cal': 3
    }
}


def test_parse_inp():
    assert parse_inp(test_str) == test_parse_inp_ret


def test_find_product():
    combo = [44, 56]
    prod_ret = find_product(test_parse_inp_ret, combo)
    assert prod_ret == 62842880


def test_main():
    prod = main(test_str)
    assert prod == 62842880


def test_find_cals():
    combo = [50, 50]
    tot_cals = find_cals(test_parse_inp_ret, combo)
    assert tot_cals == 550


def test_main2():
    prod = main(test_str, cal_limit=500)
    assert prod == 57600000


# End of Test Funcs ---------

if __name__ == "__main__":
    start1 = time.time()
    input_str = """
        Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
        Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
        Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
        Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
        """
    main(input_str)
    print(f'Finished Part One in {time.time() - start1}')

    start2 = time.time()
    main(input_str, cal_limit=500)
    print(f'Finished in {time.time() - start2}')
