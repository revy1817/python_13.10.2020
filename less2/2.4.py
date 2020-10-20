user_input = list(input("Введите слова, через пробел \n").split())
for i in range(0, len(user_input)):
    print(i + 1, user_input[i][:10])
