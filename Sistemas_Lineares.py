#Solucionando um sistema linear
import numpy as np
a = np.array([[4,2,-1],[3,3,2],[0,5,2]]) #Coeficientes do sistema
b = np.array([[7],[20],[-1]]) #Termos independentes
x = np.linalg.solve(a,b)
print(x)