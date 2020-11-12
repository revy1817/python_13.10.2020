class ComplexNumbers:

    def __init__(self, real_part, imaginary_part):
        self.real = float(real_part)
        self.imaginary = float(imaginary_part)

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumbers((self.real * other.real) - (self.imaginary * other.imaginary),
                              (self.real * other.imaginary) + (self.imaginary * other.real))


ComplexNumberA = ComplexNumbers(12, 11)
ComplexNumberB = ComplexNumbers(3, 21)
