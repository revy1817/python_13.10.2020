class Storage:
    def __init__(self, name):
        self._name = name
        self.__box = {}

    def add_to_storage(self, name, quantity):
        if name in self.__box:
            add = self.__box[name] = self.__box[name] + quantity
        else:
            add = self.__box[name] = quantity
        return add

    def remove_from_storage(self, name, quantity, department_name):
        """
        Функция отнимает количество забранной орг техники, и передает выбронному депортаменту
        :param name: Наименование техники
        :param quantity: Количество
        :param department_name: Наименование департамента
        """
        if name not in self.__box:
            return print("Данной техники нет на складе!")
        remove = self.__box[name] = self.__box[name] - quantity
        if remove < 0:
            return print("Такого количества техники нет на складе!")
        global department
        department = [department_name, {name: quantity}]
        return remove, department

    def show_box(self):
        """
        :return: Функция возращает содержимое бокса
        """
        return self.__box


class Technics:
    def __init__(self, quantity):
        self.quantity = quantity
        self.name = ""


class Printer(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Printer"


class Scanner(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Scanner"


class Xerox(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.name = "Xerox"


if __name__ == '__main__':
    storage = Storage("Склад")
    while True:
        user_name_techics = input(
            "Введите одно наименование техники которую надо добавить (ксерокс, сканер, принтер) для выхода введите q\n")
        if user_name_techics.lower() == "q":
            break
        user_quantity = input("Введите количество \n")
        try:
            user_quantity = int(user_quantity)
        except ValueError:
            print("Вы ввели не целое число, попробуйте еще раз!")
        if user_name_techics.lower() == "принтер":
            user_technics = Printer(user_quantity)
        elif user_name_techics.lower() == "ксерокс":
            user_technics = Xerox(user_quantity)
        elif user_name_techics.lower() == "сканер":
            user_technics = Scanner(user_quantity)
        try:
            storage.add_to_storage(user_technics.name, user_technics.quantity)
        except NameError:
            print("Вы ввели несуществующую технику попробуйте еще раз")
            pass
    print(storage.show_box())
