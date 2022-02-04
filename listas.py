#Listas Simples

idade = [15, 18, 21, 30]

if 16 in idade:
    idade.remove(15)
else:
    idade.append(45)

idade.append(19)
#idade.append(19, 20) - não funciona
idade.insert(2, 23)

print (idade)

for elemento in idade:
    print("Recebi o elemento", elemento)


def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista =list()
    print(len(lista))
    print(lista)
    lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
