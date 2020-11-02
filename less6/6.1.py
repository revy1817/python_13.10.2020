import time


class TrafficLight:
    __color = {"красный": 7, "желтый": 2, "зеленый": 10}

    def running(self):
        print("Светафор включился")
        while True:
            for el in self.__color:
                print(f"Загорелся {el} цвет")
                time.sleep(self.__color[el])


a = TrafficLight()
a.running()
