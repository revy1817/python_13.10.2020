number_list = []
while True:
    user_number = input("Введите целые числа через пробел \n").split()
    try:
        for x in range(len(user_number)):
            number = int(user_number[x])
            number = number_list.append(number)

        break
    except ValueError:
        print("Вы ввели не число попробуйте еще раз")


def parser(z, y):
    """
    Функция для подсчета повторений
    :param z: Искомое число
    :param y: Лист чисел
    :return: количество цифр в листе
    """
    count = 0
    for itm in range(len(y)):
        if z == y[itm]:
            count += 1
    return count


new_list = [number_list[x] for x in range(len(number_list)) if parser(number_list[x], number_list) == 1]
print(*new_list)