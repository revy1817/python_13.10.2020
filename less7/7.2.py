class Clothing:
    suit_tissue = []
    coat_tissue = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def calculate_all_tissue(cls):
        return sum(cls.suit_tissue) + sum(cls.coat_tissue)


class Suit(Clothing):
    def __init__(self, h):
        self.h = h
        super().suit_tissue.append(self.calculate_suit_tissue)

    @property
    def calculate_suit_tissue(self):
        return 2 * self.h + 0.3


class Coat(Clothing):
    def __init__(self, v):
        self.v = v
        super().coat_tissue.append(self.calculate_coat_tissue)

    @property
    def calculate_coat_tissue(self):
        return self.v / 6.5 + 0.5


if __name__ == "__main__":
    coat1 = Coat(30)
    coat2 = Coat(40)
    suit1 = Suit(99)
    suit2 = Suit(204)
    print(Coat.calculate_all_tissue())
