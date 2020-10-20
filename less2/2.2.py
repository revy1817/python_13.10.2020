user_input = list(input("Введите текст, через пробел \n").split())
n = 0
for _ in user_input[1::2]:
    user_input[n], user_input[n + 1] = user_input[n + 1], user_input[n]
    n = n + 2
print(user_input)