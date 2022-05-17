#obter as aproximações da Serie de Fourier seguindo a função y=x, utilizando 2,3 e 4 termos da série
#No final, obter o grafico dos respectivos termos.
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
x,f = symbols('x f')
init_printing()
f = x
s = fourier_series(f,(x,-pi,pi))
y = s.truncate(2)
print(y)
plt.plot(x,y,x,f)
plt.show()
