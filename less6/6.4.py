class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль начал движение со скоростью {self.speed}")

    def stop(self):
        print(f"Автомобиль остановился")

    def turn_direction(self, direction):
        print(f"Автомобиль повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f"Текущая скорость автомобиля {self.speed}км/ч")
        else:
            print(
                f"Текущая скорость автомобиля {self.speed}км/ч, что больше разрешной скорости сбавьте скорость "
                f"на {self.speed - 60}км/ч")


class SportCar(Car):
    def engine_on(self):
        print("Двигталеь заведен")


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f"Текущая скорость автомобиля {self.speed}км/ч")
        else:
            print(
                f"Текущая скорость автомобиля {self.speed}км/ч, что больше разрешной скорости сбавьте скорость "
                f"на {self.speed - 40}км/ч")


class PoliceCar(Car):
    def buzzer_on(self):
        print("Сирена включена!")


print("У вас городской автомобиль")
user_speed = int(input("Укажите скорость, целым числом, только цифры! \n"))
user_color = input("Укажите цвет автомобиля \n")
user_name = input("Укажите имя \n")
user_is_police = input("Это полицейкся машина, напишите да или нет \n")
if user_is_police.lower() == "да":
    user_is_police = True
else:
    user_is_police = False
user_car = WorkCar(user_speed, user_color, user_name, user_is_police)
user_car.show_speed()
