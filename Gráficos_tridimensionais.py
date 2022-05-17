import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
Z = np.linspace(0,15,1000)
X = np.sin(Z)
Y = np.cos(Z)
ax.plot3D(X,Y,Z,'red')
plt.show()