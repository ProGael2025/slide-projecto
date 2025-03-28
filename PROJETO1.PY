#IPORTANDOI MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("desemprego.csv", delimiter=',')

print(dados)

#IMPORTANDO AS VARIAVES
periodo = dados['periodo']
valor = dados['valor']

print(valor)

#CRIANDO O CONJUNTO DE DADOS
labels = periodo
sizes = valor

#CRIANDO A REPRESENTAÇÃO, ÁREA DE PLOTAGEM
figl, axl = plt.subplots()

#CRIANDO A RE´RESENTAÇÃO, ÁREA DE PLOTAGEM
axl.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)

#COM O CODIGO ABAIXO O GRAFICO FICARÁ EM CIRCULO
axl.axis('equal')

#colocando titulo no grafico
plt.title("VARIAÇÃO TRIMESTRAL DE DESEMPREGO NO BRASIL")

#MOSTRAR O GRAFICO
plt.show()
