from array import *
from copy import deepcopy

# validate number
def validate_num(num):
    try:
        int(num)
        return True
    except Exception:
        return False


# function to get occurrence of specific element
def get_occurrence():
    array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
    print("Original array: " + str(array_num))
    ele = int(input("Enter specific element : "))
    element = validate_num(ele)
    if element:
        return str(array_num.count(element))


# add key into dictionary
def add_key_dictionary(d):
    d.update({3: 15})
    return d


# concatenation of dictionaries
def concatenate_dict(d1, d2, d3):
    d4 = {}
    for d in (d1, d2, d3):
        d4.update(d)
    return d4


# getting dictionaries initialized
def dictionaries():
    dict1 = {1: 10, 2: 15, 3: 20}
    dict2 = {4: 25, 5: 30, 6: 35}
    return dict1, dict2


# script to generate dictionary
def script_generate1(number):
    dict1 = {}
    for d in range(1, number + 1):
        dict1[d] = d * d
    return dict1


# removing key from dictionary
def remove_key(d, k):
    if k in d:
        del d[k]
        return d
    else:
        return 0


# getting unique values from dictionary
def unique_values(value):
    unique_data = set(val for d in value for val in d.values())
    return unique_data


# create dictionary from string
def create_dict(st):
    d = {}
    for letter in st:
        d[letter] = d.get(letter, 0)+1
    return d


# print dictionary in table format
def dict_to_table(d):
    for k, v in d.items():
        name, age, address = v
        print("{:<8} | {:<15} | {:<10} | {:<15}".format(k, name, age, address))


# count number of value associated with key having success True
def count_key_values(dict1):
    dictionary = sum(d['success'] for d in dict1)
    return dictionary


# convert a list into nested dictionary keys
def list_to_dict(list_name):
    new_dictionary = current_d = {}
    for name in list_name:
        current_d[name] = {}
        current_d = current_d[name]
    return new_dictionary


# check multiple key exist or not in dictionary
def check_mul_key(d, d1, d2, d3):
    a = (d.keys() >= d1)
    b = (d.keys() >= d2)
    c = (d.keys() >= d3)
    return a, b, c


# count number of items in dictionary value that is list
def count_items_dict(d):
    count_val = sum(len(val) for val in d.values())
    return count_val


# unpack tuple
def unpack_tuple(tuplex):
    v1, v2, v3 = tuplex
    return v1 + v2 + v3


# clone tuples
def clone_tuple(tuple_x):
    new_tuple = deepcopy(tuple_x)
    return new_tuple


# get repeated items in tuple
def get_repeat_items(tuple_y):
    for t in tuple_y:
        if tuple_y.count(t) > 1:
            return True, t
        else:
            return False
