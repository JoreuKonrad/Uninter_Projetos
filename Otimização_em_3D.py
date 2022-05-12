import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D
import numpy as np
xx = np.linspace(-5,5,100)
yy = np.linspace(-5,5,100)
x,y = np.meshgrid(xx,yy)
f = x**2+y**2
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(x,y,z)

from sympy import *
x,y,f = symbols('x y f')
f = x**2+y**2
fx = diff(f,x)
fy = diff(f,y)
fxx = diff(f,x,2)
fyy = diff(f,y,2)
fxy = diff(fx,y)
fyx = diff(fy,x)
px = solve(Eq(fx,0))