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
new_list = [number_list[el] for el in range(len(number_list)) if number_list[el] > number_list[el - 1] and el != 0]
print(new_list)
