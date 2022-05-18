import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,y)
Z = X**2+Y**2
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()
