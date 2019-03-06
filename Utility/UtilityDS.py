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
