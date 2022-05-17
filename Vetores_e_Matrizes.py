#Ex1
print('Exercicio 1:')
import numpy as np
A = np.array([[5.90,7.10],[2.38,2.52],[2.90,2.00]])
B = 4.10*A
print(B)


print('')
print('Exercicio 2:')
#############
u = np.array([[3,-5,2]])
v = np.array([[4,6,3]])
uv = np.inner(u,v)
uXv = np.cross(u,v)
print(uv)
print(uXv)