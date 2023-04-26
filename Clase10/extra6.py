def separar(lista):
    lista1 = []
    lista2 = []
    for i in lista:
        if ((i % 2) == 0):
            lista1.append(i)
        else:
            lista2.append(i)
    lista1.sort()
    lista2.sort()
    return lista1,lista2

lista = [1,2,3,4,5,6,10,8,9,11]
lista1, lista2 = separar(lista)
print(lista1)
print(lista2)
