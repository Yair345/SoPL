import time
import sys


def create_array_eager():
    start_time = time.time()

    array = [i for i in range(10001)]
    new_array = array[:5000]

    end_time = time.time()

    execution_time = end_time - start_time
    memory_size = sys.getsizeof(array)

    full_type = type(array)
    new_type = type(new_array)

    return execution_time, memory_size, full_type, new_type


execution_time, memory_size, full_type, new_type = create_array_eager()
print(f"Eager Evaluation - Time: {execution_time} seconds, Memory: {memory_size} bytes, Type Match: {full_type == new_type}")


def create_array_lazy():
    start_time = time.time()

    array = (i for i in range(10001))
    new_array = (next(array) for _ in range(5000))

    end_time = time.time()

    execution_time = end_time - start_time
    memory_size = sys.getsizeof(array)

    full_type = type(array)
    new_type = type(new_array)

    return execution_time, memory_size, full_type, new_type


execution_time, memory_size, full_type, new_type = create_array_lazy()
print(f"Lazy Evaluation - Time: {execution_time} seconds, Memory: {memory_size} bytes, Type Match: {full_type == new_type}")
