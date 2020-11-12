class InputNotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    number_list = []
    while True:
        user_number = input("Введите числа для добавления в список, для ввыхода введите q \n")
        if user_number.lower() == "q":
            break
        try:
            if user_number.isdigit():
                number_list.append(user_number)
            else:
                raise InputNotNumber("Вы ввели букву, попробуйте еще раз")
        except InputNotNumber as err:
            print(err)
    print(number_list)
