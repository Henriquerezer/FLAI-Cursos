# -*- coding: utf-8 -*-
"""exercicio4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LCZ81I5x0KFJ19tWkKfJPuuhzKgSq8mV

### EXEMPLO: **Álbum Premier League 2019-2020**
1. Total de cromos: **636**
2. Preço do livro ilustrado capa brochura: **R\$ 8,90**
3. Envelope com 5 cromos: **R\$ 2,50**

### SUPOSIÇÕES
1. Todas as figurinhas tem igual probabilidade de serem sorteradas
2. Um pacotinho é comprado por vez  

### ALGORITMO
1. Comprar um pacotinho de figurinhas (5 figurinhas cada, que podem ser repetidas);
2. Colar no álbum e verificar se o álbum está completo;
3. Caso esteja incompleto, comprar mais um pacotinho, caso contrário, terminar.

### PERGUNTAS
1. Qual o valor médio investido para completar o álbum nessas condições?
2. Quantos pacotes são necessários comprar, em média, para completar o álbum?
3. Qual é a distribuição empírica do valor investido para completar o álbum?
"""

n_album = 636
preco_pacote = 2.50
preco_album = 8.90
simulacoes = 1000

import numpy as np

# representação do álbum
album = np.zeros(n_album) 

# representação do pacote de figurinhas
pacotinho = np.random.choice(range(n_album), 5)
pacotinho

# 'colando' as figurinhas obtidas no álbum
for i in pacotinho:
    album[i] += 1

print(album)

# comprando figurinhas até completar o álbum
def SimulaAlbum():
    album = np.zeros(n_album) 
    pacotes = 0
    while not np.all(album > 0):
        pacotinho = np.random.choice(range(n_album), 5)
        pacotes += 1

        for i in pacotinho:
            album[i] += 1
 

    valor_gasto = preco_album + preco_pacote * pacotes 

    mais_repetidas = max(album)

    nao_repetidas = sum(album == 1)

    return valor_gasto,  mais_repetidas, nao_repetidas

SimulaAlbum()

valores = []
maisrep = []
nao_rep = []

for i in range(simulacoes):

  s1, s2, s3 = SimulaAlbum()

  valores.append(s1)
  maisrep.append(s2)
  nao_rep.append(s3)

  if (i+1) % 100 == 0:
    print('Simulação: ', i+1, '/', simulacoes)

print('O valor médio gasto foi:', round(np.mean(valores), 2))
print('O numero de pacotes médio foi:', round((np.mean(valores) - preco_album)/preco_pacote, 2))

import matplotlib.pyplot as plt
plt.hist(valores, bins = 20, density = True, edgecolor = 'black')
plt.title('Distribuição Empírica do Valor Gasto para Completar o Álbum')
plt.show()

"""### Faça as modificações e implementações necessárias para responder as seguintes perguntas adicionais:

4. Quantas vezes saiu a figurinha mais repetida, em média?
5. Em média, quantas figurinhas não se repetem ao completar o álbum?
6. Qual a probabilidade de se gastar mais que R\$3000,00 para completar o álbum?
7. Qual a probabilidade de se gastar menos que R\$1500,00 para completar o álbum?
8. Qual a probabilidade de se gastar mais do que a média para completar o álbum?
9. Qual é o intervalo de confiança de 95% para o gasto ao se completar o álbum?
10. Qual o valor médio gasto caso se esteja completando o álbum com mais um amigo?
11. Quanto se economiza ao utilizar o cenário da questão 10?
12. 
Qual o valor médio gasto caso se esteja completando o álbum com mais dois amigos?

13. Quanto se economiza ao utilizar o cenário da questão 12?
"""

# questao 4 
# adicionei uma nova variavel, para que fosse salvo os maior valor da variael album, neste caso o maior valor, significado o valor mais repetido (figurinha mais repetida) MÉDIA
np.mean(maisrep)

# Questão 5 
# foi adiconado uma váriavel igualada a (1), assim saberia quais posições do vetor teriam sido sorteadas apenas uma única vez. (Figurinha que tirei apenas uma vez) MÉDIA
np.mean(nao_rep)

#questão 6
#preciso transformar meus valores em um array, para que eu possa fazer operações algébricas, por exemplo calcular valores abaixo de um determinado valor. e calcular a média de vezes que pode ocorrer
(np.array(valores) > 3000).mean()

#questão 7
(np.array(valores) < 1500).mean()

#questão 8
(np.array(valores) > np.mean(valores)).mean()

#questão 9
# INTERVALO DE CONFIANÇA DE 95%
np.quantile(valores, [0.025,0.975])

#questão 10
# comprando figurinhas com um amigo até completar os dois albuns 
def SimulaAlbum2(n_amigos):
    album = np.zeros(n_album) 
    pacotes = 0
    while not np.all(album > n_amigos):
        pacotinho = np.random.choice(range(n_album), 5)
        pacotes += 1

        for i in pacotinho:
            album[i] += 1
 

    valor_gasto = preco_album + preco_pacote * pacotes 

  

    return valor_gasto

valores2 = []

for i in range(simulacoes):
  valores2.append(SimulaAlbum2(n_amigos = 1)) #DEFININDO QUE O NÚMERO DE AMIGOS É IGUAL A 1

  if (i+1) % 100 == 0:
    print('Simulações: ', 1+i, '/', simulacoes)

valor2 = np.mean(valores2)/2
print(valor2)

#questã 11 

diferença = np.mean(valores) - valor2
print('A diferença ao comprar com 3 amigos é igual a: ', diferença)

#ou 

1 - valor2/np.mean(valores) # porcentagem

#Questão 12

#questão 10
# comprando figurinhas com um amigo até completar os dois albuns 
def SimulaAlbum3(n_amigos):
    album = np.zeros(n_album) 
    pacotes = 0
    while not np.all(album > n_amigos):
        pacotinho = np.random.choice(range(n_album), 5)
        pacotes += 1

        for i in pacotinho:
            album[i] += 1
 

    valor_gasto = preco_album + preco_pacote * pacotes 

  

    return valor_gasto

valores3 = []

for i in range(simulacoes):
  valores3.append(SimulaAlbum3(n_amigos = 2)) #DEFININDO QUE O NÚMERO DE AMIGOS É IGUAL A 2

  if (i+1) % 100 == 0:
    print('Simulações: ', 1+i, '/', simulacoes)

valor3 = np.mean(valores2)/3
print('valor médio para cada amigo: ', valor3)

#questão 13
diferença2 = np.mean(valores) - valor3
print('A diferença ao comprar com 3 amigos é igual a: ', diferença2)