#resolvendo a derivada de F(x) = -2*x**3-4*x**2+13*x-1
from sympy import *
x,f = symbols('x f')
f = -2*x**3-4*x**2+13*x-1
print(diff(f,x)) #Derixada da função 'f' em relação a variavel 'x'

#resolvendo a derivada de g(x) = 2*x+ln(x)
x,g = symbols('x g')
g = 2*x+ln(x)
print(diff(g,x))

#resolvendo a derivada de h(x) = sen(x)
x,h = symbols('x h')
h = sin(x)
print(diff(h,x))

#Aplicando a segunda derivada em uma função. Exemplo: g(x) = 2*x+ln(x)
x,g = symbols('x g')
g = 2*x+ln(x)
print(diff(g,x,2))

#Aplicando a segunda derivada em uma função. Exemplo: F(x) = -2*x**3-4*x**2+13*x-1
x,f = symbols('x f')
f = -2*x**3-4*x**2+13*x-1
print(diff(f,x,2))




