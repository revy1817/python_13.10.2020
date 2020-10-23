def user_info(name, surname, year_birth, city, email, phone_number):
    s = " "
    user_info_result = s.join([name, surname, year_birth, city, email, phone_number])
    return user_info_result


print(user_info(name=input("Введите имя \n"), surname=input("Введите фамилию \n"),
                year_birth=input("Ввдетие год рождения \n"), city=input("Введите город проживания \n"),
                email=input("Введите свой email \n"), phone_number=input("Введите номер своего телефона \n")))
