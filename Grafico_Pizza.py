import matplotlib.pyplot as plt
x = [340,560,290]
cursos = ['Computação', 'Elétrica','Produção']
cores = ['r','m','y']
plt.axis('equal')
plt.pie(x,labels=cursos,colors=cores,shadow=True,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title('Número de estudantes por curso')
plt.show()