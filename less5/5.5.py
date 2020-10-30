with open("5.5_UserNumbers.txt", "w", encoding="UTF-8") as user_numbers_file:
    user_numbers_file.write(input("Введите числа, через пробел которые хотите добавить в новый файл и посчитать их"
                                  "сумму \n"))
with open("5.5_UserNumbers.txt", "r") as numbers_file:
    numbers = numbers_file.readline().split()
    sum_numbers = 0
    for el in numbers:
        try:
            sum_numbers += float(el)
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз!")
            break
    print(f"Сумма всех чисел в файле равна {sum_numbers}")
