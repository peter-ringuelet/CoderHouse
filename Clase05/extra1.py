num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
opcion = 0

while (opcion != 4):
    print("""
1) Mostrar una suma de los dos números
2) Mostrar una resta de los dos números (el primero menos el segundo)
3) Mostrar una multiplicación de los dos números
4) Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
""")

    opcion = (input("Ingrese una de las siguientes opciones(1,2,3,4): "))

    if(opcion == '1'):
        print(num1 + num2)
    elif(opcion == '2'):
        print(num1 - num2)
    elif(opcion == '3'):
        print(num1 * num2)
    elif(opcion == '4'):
        break
    else:
        print('La opcion no es correcta')
