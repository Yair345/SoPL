from functools import reduce
from Ex1 import foo

lst = [x for x in range(1, 1000)]


def is_even(x):
    return x%2 == 0


def split_list(func, lst):
    return tuple([x for x in lst if func(x)]), tuple([x for x in lst if not func(x)])


# print(split_list(is_even, lst)[0])

# even_list, odd_list = split_list(is_even, lst)


def even_func(lst):
    return reduce(lambda x, y: x * y, lst)


def odd_func(func, lst):
    return reduce(lambda x, y: func(x) + y, lst)


def applay_funcs(func1, func2, lst, odd_func, split_func, split_factor):
    even_list, odd_list = split_func(split_factor, lst)
    print(func1(even_list))
    print(func2(odd_func, odd_list))


def main():
    # print("__________________________________________________")
    applay_funcs(even_func, odd_func, lst, foo, split_list, is_even)


if __name__ == "__main__":
    main()
