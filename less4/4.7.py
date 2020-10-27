def fact(x):
    result = 1
    for itm in range(1, x + 1):
        result *= itm
        yield result


while True:
    user_number = input("Введите число факториал которого нужно вычесть \n")
    try:
        user_number = int(user_number)
        break
    except ValueError:
        print("Вы ввели не число")
for el in fact(user_number):
    print(el)
