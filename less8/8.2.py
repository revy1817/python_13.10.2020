class My_error_zero_division(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    dividend = input("Введите делимое \n")
    divider = input("Введите делитель \n")
    try:
        dividend, divider = float(dividend), float(divider)
        if divider == 0:
            raise My_error_zero_division("На ноль делить нельзя введите другое число!")
        print(dividend / divider)
    except ValueError:
        print("Вы ввели не число!")
    except My_error_zero_division as err:
        print(err)
        continue
