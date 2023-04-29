# código de geração do gráfico 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('gasolina.csv')

# define o estilo do Seaborn
sns.set_style('darkgrid')

# cria o gráfico de linha
sns.lineplot(data=df, x='dia', y='venda')

# rotulos aos eixos x e y

plt.xlabel('Dia')
plt.ylabel('Preço de venda')

# salva o gráfico em um arquivo PNG
plt.savefig('gasolina.png')
