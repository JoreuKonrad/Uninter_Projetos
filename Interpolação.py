#Criar uma parabola sendo que imita uma ponte com 7m de altura e 20m de comprimento
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *
x = [0,10,20]
y = [0,7,0]
print(lagrange(x,y))
f = interp1d(x,y,kind='quadratic')
xi = np.linspace(1,20,100)
yi = f(xi)
plt.plot(x,y,'o')
plt.plot(xi,yi)
plt.show()