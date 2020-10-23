def divide(x, y):
    while True:
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            print("Делить на 0 НЕЛЬЗЯ!")
            y = float(input("Введите делитель не равный нулю! \n"))


while True:
    user_number_1 = input("Введите делимое \n")
    user_number_2 = input("Введите делитель \n")
    try:
        user_number_1 = float(user_number_1)
        user_number_2 = float(user_number_2)
        break
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз!")

print(divide(user_number_1, user_number_2))
