from array import *
from copy import deepcopy
from itertools import groupby
from operator import itemgetter
import itertools
import textwrap


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


# ----------------------------dictionary-------------------------------------------

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
    dictionary1 = {1: 10, 2: 15, 3: 20}
    dictionary2 = {4: 25, 5: 30, 6: 35}
    return dictionary1, dictionary2


# script to generate dictionary
def script_generate1(number):
    dictionary1 = {}
    for d in range(1, number + 1):
        dictionary1[d] = d * d
    return dictionary1


# removing key from dictionary
def remove_key(d, key):
    if key in d:
        del d[key]
        return d
    else:
        return 0


# getting unique values from dictionary
def unique_values(value):
    unique_data = set(val for d in value for val in d.values())
    return unique_data


# create dictionary from strings
def create_dict(string):
    d = {}
    for letter in string:
        d[letter] = d.get(letter, 0)+1
    return d


# print dictionary in table format
def dict_to_table(d):
    for k, v in d.items():
        name, age, address = v
        print("{:<8} | {:<15} | {:<10} | {:<15}".format(k, name, age, address))


# count number of value associated with key having success True
def count_key_values(dictionary1):
    dictionary = sum(d['success'] for d in dictionary1)
    return dictionary


# convert a list into nested dictionary key
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


# count number of items in dictionary values that is list
def count_items_dict(d):
    count_val = sum(len(val) for val in d.values())
    return count_val

# ----------------------------------tuple------------------------------------------------


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


# check element existence in tuples
def check_existence(tuple_z, element):
    for t in tuple_z:
        if element == t:
            return True
    return False


# removing element from tuple
def remove_tuple(tuple_1, item):
    new_tuple = []
    for l in list(tuple_1):
        if item != l:
            new_tuple.append(l)
    return tuple(new_tuple)


# slicing on tuple
def slice_tuple(tuple_2):
    s1 = tuple_2[3:5]
    s2 = tuple_2[4:]
    s3 = tuple_2[:4]
    return s1, s2, s3


# reverse tuple
def rev_tuple(tuple_3):
    rev = tuple_3[::-1]
    return rev

# -----------------------------Set--------------------------------------------------


# create set 1
def create_set():
    new_set = set([10, 20, 30, 40, 50])
    return new_set


# create set2
def create_set2():
    new_set2 = set([20, 40, 60, 70, 90])
    return new_set2


# iteration over set
def iteration(set_1):
    for s in set_1:
        print(s)


# add member in set
def add_member(set_2):
    set_2.add("Pune")
    set_2.add("Delhi")
    return set_2


# remove item(s) from the set
def remove_item(set_3):
    pop_set = set(set_3)
    pop_set.pop()
    pop_set.pop()
    return pop_set


# remove specific items if present
def rem_spec_item(set_3, item):
    if item not in set_3:
        return "item not found"
    else:
        new_set = []
        for s in list(set_3):
            if item != s:
                new_set.append(s)
        return set(new_set)


# intersection between sets
def intersect(set_4, set_5):
    return set_4 & set_5


# unions of sets
def union(set_6, set_7):
    return set_6 | set_7


# get set difference
def difference(set_8, set_9):
    set_10 = set_8 - set_9
    return set_10


# get symmetric difference in sets
def symmetric_diff(set_11, set_12):
    return set_11 ^ set_12


# clear set
def clear_set(set_13):
    return set_13.clear()


# frozenset
def fro_set(frozen):
    return frozenset(frozen)


# minimum in set
def min_set(set_14):
    # return min(set_14)
    for s in set_14:
        min1 = s
        break
    for s1 in set_14:
        if min1 > s1:
            min1 = s1
    return min1


# maximum in set
def max_set(set_15):
    for s in set_15:
        max1 = s
        break
    for s1 in set_15:
        if max1 < s1:
            max1 = s1
    return max1

# -----------------------------List-----------------------------------------------


# creating List
def create_list(element):
    li = []
    try:
        for e in range(element):
            input1 = int(input("Enter element : "))
            valid = validate_num(input1)
            if valid:
                li.append(input1)
            else:
                print("enter number only")
    except Exception as e:
            print(e)
    return li


# creating list for all types and len > 2
def create_list_all(element):
    li = []
    try:
        for e in range(element):
            input2 = input("Enter element : ")
            if len(input2) >= 2:
                li.append(input2)
            else:
                print("String should be len 2 or more")
    except Exception as e:
        print(e)
    return li


# creating list for all types
def list_all_types(element):
    li = []
    try:
        for e in range(element):
            input2 = input("Enter element : ")
            li.append(input2)
    except Exception as e:
        print(e)
    return li


# sum of all list
def sum_list(li):
    sum1 = 0
    for l in li:
        sum1 += l
    return sum1


# Multiplication of list
def multiplication_list(li):
    mul = 1
    for l in li:
        mul *= l
    return mul


# smallest element from list
def small_element(li):
    small = li[0]
    for l in li:
        if small > l:
            small = l
    return small


# count of string whose First and Last char is same
def count_string_char(li):
    counter = 0
    for l in li:
        if l[0] == l[-1]:
            counter += 1
    return counter


# get a sorted list
def print_sort_list(list_of_tuple):
    return sorted(list_of_tuple, key=last)


# getting last element from list of tuple
def last(element):
    return element[-1]


# remove duplicates from list
def remove_duplicate(li):
    copy_list = set()
    new_list = []
    for l in li:
        if l not in copy_list:
            new_list.append(l)
            copy_list.add(l)
    return new_list


# clone or copy lists
def clone_list(li):
    clone = li[:]
    return clone


# Word is longer than N number in list
def word_longer(li, n):
    word_list = []
    for l in li:
        if len(l) >= n:
            word_list.append(l)
    return word_list


# getting common members from lists
def common_member(list1, list2):
    member = []
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                member.append(l2)
    return member


# remove element of specified position in List
def specified_element_rm(li):
    color = [c for (l, c) in enumerate(li) if l not in (0, 4, 5)]
    return color


# permutations of list
def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]


# get list difference
def get_diff_list(list1, list2):
    return set(list1)-set(list2)


# append a list
def append_list(list1, list2):
    return list1 + list2


# circular identicals of list
def circular_identical(list1, list2):
    if ' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)):
        return True
    else:
        return False


# find common item in lists
def common_items(list1, list2):
    return set(list1) & set(list2)


# split the word in list
def split_word(list1):
    for letter, words in groupby(sorted(list1), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)


# remove duplicate from list in list
def list_to_list(list1):
    list1.sort()
    new_list = list(n for n, _ in groupby(list1))
    return new_list

# -----------------------String-------------------------------------------------------


# string validation
def validate_string(st):
    try:
        string = st
        if string.isalpha():
            return True
        else:
            return False
    except Exception as e:
        print(e)


# calculate length of the  string
def str_len(st):
    count = 0
    for c in st:
        count += 1
    return count


# get characters frequency
def char_frequency(st):
    freq = {}
    for s in st:
        freq[s] = freq.get(s, 0) + 1
    return str(freq)


# replace chars with $ except 1st char
def replace_char(st):
    ch = st[0]
    st = st.replace(ch, '$')
    st = ch + st[1:]
    return st


# add suffix string ing/ly at end
def string_suffix(st):
    len_str = len(st)
    if len_str > 2:
        if st[-3:] == 'ing':
            st += 'ly'
        else:
            st += 'ing'
    return st


# get the longest word from string list
def get_long_word(st):
    word_string = []
    for s in st:
        word_string.append((len(s), s))
    word_string.sort()
    return word_string[-1][1]


# get UPPER/Lower Case
def upper_lower(st):
    return st.upper(), st.lower()


# get unique words in sorted way
def sort_word():
    try:
        str_list = input("Enter comma separate words :")
        words = [word for word in str_list.split(",")]
        return ",".join(sorted(list(set(words))))
    except Exception as e:
        print(e)


# get last part of the string before specified char
def last_part_string():
    st = 'https://www.w3resource.com/python-exercises$programming'
    print("String is : ", st)
    print("After Result : ", st.rsplit('$', 1)[0], "\n""After Result", st.rsplit('/', 1)[0])


# get formatted result of string
def format_string(st):
    return textwrap.fill(st, width=50)


# count substring in string
def count_substring(sub):
    string = "python is an interpreted, python is high-level, python is general-purpose programming language"
    return string.count(sub)


# reverse string
def reverse_string(st):
    return ''.join(reversed(st))


# get lowercase letter of N char with whole string
def get_lowercase(st, n):
    return st[:n].lower() + st[n:]

# -------------------------------------------------------------------------------
