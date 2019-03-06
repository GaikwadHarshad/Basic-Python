def validate_num(num):
    try:
        int(num)
        return True
    except Exception:
        return False


def add_key_dictionary(d):
    d.update({3: 15})
    return d
