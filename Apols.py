from sympy import *
x,y = symbols('x y')
y = -80*x**2*7900*x-5000
expresion = parse_expr(y)
print(y)