import math

def second_equation(a, b, c):
    Δ = b**2 - 4*a*c
    if Δ > 0:
        x1 = (-b-math.sqrt(Δ)) /(2*a)
        x2 = (-b+math.sqrt(Δ)) /(2*a)
        print(x1, x2)
    elif Δ == 0:
        x = -b / (2*a)
        print(x)
    elif Δ < 0:
        print("no answer")

second_equation(3, 5, 7)
second_equation(2, 7, 1)