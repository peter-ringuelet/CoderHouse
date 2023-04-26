lista_original = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print(list(set(lista_original)))

lista_ordenada = list(set(lista_original))
lista_ordenada.sort(reverse=True)
print(lista_ordenada)  # [75, 54, 53, 34, 9, 7, 1]

pos = 0
while (pos < len(lista_ordenada)):
    if (lista_ordenada[pos] % 2 == 1):
        lista_ordenada.pop(pos)
    else:
        pos+=1
print(lista_ordenada)

suma = sum(lista_ordenada)
print(suma)

lista_ordenada.insert(0,suma)
print(lista_ordenada)

