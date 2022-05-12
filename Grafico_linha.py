import matplotlib.pyplot as plt
x = ['Março','Abril','Maio','Junho','Julho']
y = [35000,29000,27000,32000,33000]
plt.plot(x,y) # Se substituir por plt.plot(x,y,'r o') --> Irá transformar em gráfico de linha
plt.ylim(0,40000) #aplicar um limite de paramentro na escada Y
plt.title('Produção de Março até Julho')
plt.xlabel('Mês')
plt.ylabel('Produção')

plt.show()