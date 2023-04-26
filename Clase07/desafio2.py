dict = {'Dolar':'$','Euro':'€', 'Libra':'£'}
divisa = input('Ingrese una divisa: ')
print(dict.get(divisa, 'La divisa no se encuentra disponible'))