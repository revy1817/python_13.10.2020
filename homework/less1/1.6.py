user_result = float(input("Сколько килломтроев вы пробежали в первый день \n"))
user_end_result = float(input("Сколько киллометров вы хотите пробежать \n"))
user_day_result = user_result
day = 1
while user_result < user_end_result:
    user_day_result = user_day_result + (user_day_result * 0.1)
    user_result += user_day_result
    day += 1
print(f"на {day} день спортсмен достиг результата — не менее {int(user_end_result)} км")