lista = [1,2,3,4,5,6,7,8,9,10]

print(len(lista))
def media(lista):
    tot = len(lista)
    sum = 0;
    for i in range(0,tot):
        sum += lista[i]
    return sum / tot

print(media(lista))
