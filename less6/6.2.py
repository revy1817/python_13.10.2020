class Road:
    asphalt_per_1m2 = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self):
        asphalt = self._length * self._width * self.asphalt_per_1m2 * self.thickness / 1000
        print(f"На дорогу длиной {self._length}м и шириной {self._width}м нужно {asphalt} тонн асфальта")


a = Road(20, 5000)
a.calculation()