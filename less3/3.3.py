def sum_max_two_elements(a, b, c):
    elements = [a, b, c]
    min_element = min(elements)
    elements.remove(min_element)
    sum_max_elements = sum(elements)
    return sum_max_elements


while True:
    user_elements = input("Введите три числа через пробел! \n").split()
    if len(user_elements) == 3:
        try:
            for i in range(len(user_elements)):
                user_elements[i] = int(user_elements[i])
            break
        except ValueError:
            print("Вы ввели не число попробуйте еще раз")
    else:
        print("Вы ввели больше или меньше элементов, попробуйте еще раз!")

print(sum_max_two_elements(*user_elements))
