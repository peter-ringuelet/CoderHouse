num = int(input('Ingrese un numero entero entre el 0 y el 9: '))
lista = [1,3,7]
while not(0 <= num <= 9):
    num = int(input('Ingrese un numero entero entre el 0 y el 9: '))
if num in lista:
    print(f'El numero {num} se encuentra en la lista')
else:
    print(f'El numero {num} NO se encuentra en la lista')
