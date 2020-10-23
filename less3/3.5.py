result = 0
no_error = True
while no_error is True:
    user_elements = input("Введите числа через пробел! Для прекращение введите любую букву \n").split()
    for i in range(len(user_elements)):
        try:
            number = int(user_elements[i])
            result += number
        except ValueError:
            print(result)
            no_error = False
            break
    if not no_error:
        break
    print(result)
    user_next_try = input("Хотите ли вы добавить еще чисел? Если да - напишите Да, если нет - нажмите Enter или "
                          "введите любые символы \n")
    user_next_try = user_next_try.lower()
    if "да" in user_next_try:
        pass
    else:
        break
