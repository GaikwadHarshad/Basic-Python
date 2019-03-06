def validate_num(num):
    try:
        int(num)
        return True
    except Exception:
        return False


def add_key_dictionary(d):
    d.update({3: 15})
    return d


def concatenate_dict(d1, d2, d3):
    d4 = {}
    for d in (d1, d2, d3):
        d4.update(d)
    return d4


def dictionaries():
    dict1 = {1: 10, 2: 15, 3: 20}
    dict2 = {4: 25, 5: 30, 6: 35}
    return dict1, dict2


def script_generate1(number):
    dict1 = {}
    for d in range(1, number + 1):
        dict1[d] = d * d
    return dict1


def remove_key(d, k):
    if k in d:
        del d[k]
        return d
    else:
        return 0
