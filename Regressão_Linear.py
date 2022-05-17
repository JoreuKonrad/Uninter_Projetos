#Regressão linear é criar uma linha reta que aproxime dos comportamentos.
#Coeficiente correlação é o quanto a linha está proxima do ponto.
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats #Note que é usado 'from' e nao 'import' da biblioteca
x = np.array([1,2,3,4])
y = np.array([5000,5300,5200,5500])
a,b,correlacao,p,erro = stats.linregress(x,y)
print('Reta de regressão y=%.2fx=%.2f'%(a,b))
print('Coeficiente de correlação: r=%.2f'%correlacao)
plt.plot(x,y,'o',label='Dados Originais')
f= a*x+b
plt.plot(x,f,'r',label='Reta de regressao')
plt.ylim(4900,5600)
plt.legend()
plt.show()