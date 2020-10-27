import functools


def times(el, next_el):
    return el * next_el


numbers = [x for x in range(100, 1001) if x % 2 == 0]
print(functools.reduce(times, numbers))
