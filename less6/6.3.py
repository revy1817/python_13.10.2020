class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker = Position(input("Введите имя \n"), input("Введите фамилию \n"), input("Введите должность \n"),
                  {"wage": float(input("Введите вашу зарплату \n")), "bonus": float(input("Введите премию \n"))})
print(worker.get_full_name(), worker.get_total_income())
