user_numbers = int(input("Введите число \n"))
last_number = user_numbers % 10
numbers_left = user_numbers // 10
while numbers_left > 0:
    if last_number >= (numbers_left % 10):
        numbers_left = numbers_left // 10
    else:
        last_number = numbers_left % 10
print(f"Наибольшее число {last_number}")
