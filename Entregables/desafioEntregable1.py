def año_bisiestro(año):
    '''
    Input:
    Se ingresa un numero entero que representa un año
    
    Output:
    Se imprime por pantalla un string que dice si el año es o no bisiesto.
    En caso de no ser un numero, se imprime un mensaje por pantalla informandolo
    '''
    if (año.isnumeric()):
        if ((int(año) % 4 == 0) and not (int(año) % 100 == 0)):
            print(f"El año {año} es bisiesto")
        elif (int(año) % 400 == 0):
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} no es bisiesto")
    else:
        print(f"Debe ingrsesar un numero, {año} no lo es.")


año = (input("Ingrese un numero: "))
año_bisiestro(año)
