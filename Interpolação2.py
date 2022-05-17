#determinar o volume de um garrafa a qual foi dada os valores de alguns pontos.
from scipy.interpolate import *
x = [4.6,15.45,17.72,10.65,1.73,7.69,0.45]
y = [5.97,2.11,2.37,3.74,4.94,5.37,3.27]
f = lagrange(x,y)
print(f)