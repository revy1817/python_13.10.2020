user_time = int(input("Введите время в секундах \n"))
hours = user_time // 3600
minutes = (user_time // 60) - (hours * 60)
print(f"Время в формате ЧЧ/ММ/СС - {hours}:{minutes}:{user_time - ((hours * 3600) + (minutes * 60))}")
