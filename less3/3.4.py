def my_func(x, y):
    result = x
    expo_try = 1
    while expo_try < abs(y):
        result = result * x
        expo_try += 1
    return 1 / result


x, y = 5, -3
print(my_func(x, y))
