def es_multiplo(num1,num2):
    if (num1 % num2 == 0):
        if(num2 % num1 == 0):
            print("Ambos numeros son multiplos entre si")
        else:
            print(f"{num1} es multiplo de {num2}")
    elif (num2 % num1 == 0):
        if (num1 % num2 == 0):
            print("Ambos numeros son multiplos entre si")
        else:
            print(f"{num2} es multiplo de {num1}")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: ")) 

es_multiplo(num1,num2)
