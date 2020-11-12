class Date:
    def __init__(self, date):
        self.day, self.month, self.year = date.split("-")

    @classmethod
    def date_to_int(cls, date):
        date = date.split("-")
        date_int = []
        for el in date:
            try:
                el = int(el)
                date_int.append(el)
            except ValueError:
                print("Вы ввели не число")
        return date_int

    @staticmethod
    def date_valid(date):
        date = date.split("-")
        for idx in range(len(date)):
            date[idx] = int(date[idx])
        if 0 < date[0] > 31 or 0 < date[1] > 12 or 1900 < date[2] > 2021:
            return print("Дата введена не корректно")
        else:
            return print("Дата введена корректно")


Date.date_valid("21-11-2001")
print(Date.date_to_int("21-11-2001"))
