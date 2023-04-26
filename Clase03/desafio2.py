nombre = input('Ingrese nombre: ')
edad = int(input('Ingrese edad: '))

resultado = (nombre != '***') and ((edad > 5) and (edad < 20)) and ((len(nombre) >= 4) and (len(nombre) < 8)) and ((edad*3) > 35)

print(resultado)