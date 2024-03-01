
class Fraction:
    def __init__(self, ss, mm):
        # properties
        self.s = ss
        self.m = mm

    # methods
    def sum(self, other): # other is not key word just one agreement between programmer
        s= self.s * other.m + self.m *other.s
        m = self.m *other.m 
        x = Fraction(s, m)
        return x

    def mul(self, other):
        result_s =  self.s * other.s
        result_m =  self.m * other.m 
        x = Fraction(result_s,result_m)
        return x

    def sub(self):
        ...

    def div(self):
        ...

    def fraction(self):
        ...

    def show(self):
        print(self.s, '/', self.m)

a = Fraction(2, 3)
a.show()

b = Fraction(7, 1)
b.show()

z = b.mul(a)
z.show()


    