# Encontrar o valor máximo da função y = -4*x**2+4000*x-200000
from sympy import *
x,y = symbols('x y')
y = -4*x**2+4000*x-200000
df = diff(y,x)
d2f = diff(y,x,2)
p = solve(Eq(df,0))
l = y.subs(x,p[0])
ds = d2f.subs(x,p[0])
print('Preço ótimo:',p[0])
print('Lucro Máximo:',l)
print('Derivada segunda:',ds)

#############

print('')
print('Segundo Exercicio:')
#Encontrar o valor minimo da função c = x**2-20*x+300
x,c = symbols('x c')
c = x**2-20*x+300
df = diff(c,x)
df2 = diff(c,x,2)
p = solve(Eq(df,0))
ds = d2f.subs(x,p[0])
print('Produção ótima:',p[0])
print('Derivada segunda:',ds)

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,25,100)
c= x**2-20*x+300
plt.plot(x,c)
plt.show()
