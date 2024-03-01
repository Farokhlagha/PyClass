class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show(self):
        print(self.real, "+", "i" if self.imag >= 0 else "- i", abs(self.imag))

a = Complex(5, 8)
a.show()