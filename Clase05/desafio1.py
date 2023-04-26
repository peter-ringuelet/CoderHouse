suma = 0
numero = (input('Ingrese un numero: '))
while (numero != 'exit()'):
    if (numero.isnumeric()):
        suma += int(numero)
    numero = (input('Ingrese un numero: '))
print(suma)