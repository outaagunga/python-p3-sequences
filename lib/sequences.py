#!/usr/bin/env python3

def print_fibonacci(length):
    get_value = []
    if length >= 1:
        get_value.append(0)
    if length >= 2:
        get_value.append(1)

    for i in range (2, length):
        next_value = get_value[i-1] + get_value[i-2]
        get_value.append(next_value)

    print(get_value)
    pass