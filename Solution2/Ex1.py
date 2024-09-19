import time


def apply_func(f, lst):
    return [f(v) for v in lst]


def sum_list(lst):
    return sum(lst)


def imperative_sum(lst):
    total = 0
    for v in lst:
        total += v
    return total


def my_sum(f):
    return sum([f(v) for v in list(range(10000))])


foo = lambda x: x / 2 + 2

my_list = apply_func(foo, list(range(10000)))

# Time Python's built-in sum
start_builtin_sum = time.time()
builtin_sum_result = sum_list(my_list)
end_builtin_sum = time.time()

builtin_sum_time = end_builtin_sum - start_builtin_sum


# Time custom sum
start_custom_sum = time.time()
custom_sum_result = imperative_sum(my_list)
end_custom_sum = time.time()

custom_sum_time = end_custom_sum - start_custom_sum

print(my_sum(foo))
output = f"""
Results:
---------
1. Built-in sum result  : {builtin_sum_result}
2. Custom sum result    : {custom_sum_result}

Time Performance:
------------------
1. Built-in sum time    : {builtin_sum_time:.6f} seconds
2. Custom sum time      : {custom_sum_time:.6f} seconds
"""
print(output)
