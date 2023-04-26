lista_1 = []
lista_2 = []

lista_1.append(456789)          #1
lista_1.append('Hola Mundo')
print(lista_1)

lista_2.append('Hola y Adios')
lista_2.append(5555)
print(lista_2)

lista_3 = lista_1[:-1]
print(lista_3)

lista_4 = lista_2[1:-1]
print(lista_4)

lista_4 = lista_2[1:2]
print(lista_4)

lista_5 = lista_4 + lista_3
print(lista_5)