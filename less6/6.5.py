class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером.")


print("У вас маркер")
user_title = input("Введите наименование проекта \n")
user = Handle(user_title)
user.draw()
