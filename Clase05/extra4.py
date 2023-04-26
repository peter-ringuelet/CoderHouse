cant = int(input('Ingrese cuantos numeros quiere introducir: '))
sum = 0
for i in range(cant):
    num = int(input(f'Ingrese el numero {i+1}: '))
    sum += num
print(sum / cant)