import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV em um DataFrame do Pandas
df = pd.read_csv("gasolina.csv")

# estilo do gráfico

sns.set_style('darkgrid')

# Cria um gráfico de linha utilizando o método lineplot do Seaborn
sns.lineplot(x="dia", y="venda", data=df)

# Adiciona um título e rótulos aos eixos x e y
plt.title("Preço da gasolina ao longo dos dias")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")

# Salva o gráfico em um arquivo png
plt.savefig("gasolina1.png")