import os
import json

# ______DEFINO FUNCIONES______


def almacenar(name, password, registro):
    '''
        INPUT: nombre y contraseña que quieras registrar(Strings), junto con el registro(diccionario) donde se almacenan

        OUTPUT: si el usuario no esta registrado lo registra y lo informa por pantalla,
        sino solo informa que ya esta registrado el usuario
    '''
    if (name not in registro):
        registro[name] = password
        guardar_db(name, password)
        print("Se ha registrado con exito.")
    else:
        print("El usuario que ha ingresado ya se encuentra registrado")


def imprimir(registro):
    '''
        INPUT: registro(diccionario) con los usuarios y contraseñas

        OUTPUT: Imprime en pantalla todos los usuaarios con sus respectivas contraseñas
    '''
    if len(registro) != 0:
        print("Los pares user-password almacenados en la base de datos son: ")
        for name in registro:
            print(f"    {name}  {registro[name]}")
    else:
        print("No se han registrado usuarios hasta el momento")


def login(name, password, registro):
    '''
    INPUT: usuario y contraseña(Strings) junto con el registro donde se almacenan los mismos(diccionario)

    OUTPUT: imprime por pantalla si se pudo loguear o no el usuario
    '''
    if (name in registro) and (registro[name] == password):
        print("Se ha logueado correctamente")
    else:
        print("El usuario o contraseña son incorrectos")


def guardar_db(name, password):
    '''
    INPUT: usuario y contraseña(Strings)

    OUTPUT: agrega a la base de datos el usuario y contraseña
    '''
    file = open("db.txt", "a")
    file.write(f"{name} {password} \n")
    file.close()


def cargar_registro(registro):
    '''
    INPUT: registro(diccionario) donde se almacenaran los usuarios y contraseñas de la base de datos

    OUTPUT: devuelve el diccionario con todo el contenido de la base de datos
    '''
    file = open("db.txt", "r")
    arreglo = file.read().split()
    for i in range(0, len(arreglo)-1, 2):
        registro[arreglo[i]] = arreglo[i+1]
    file.close()


def crear_archivo():
    file = open("db.txt", "w")
    file.close()


def actualizar_registro(registro):
    try:
        cargar_registro(registro)
    except:
        crear_archivo()
        cargar_registro(registro)


def imprimir_menu():
    os.system('cls')
    print("--------------------OPCIONES-------------------")
    print("\t1) Registrar cuenta")
    print("\t2) Imprimir todos los usuarios con sus contraseñas")
    print("\t3) Login")
    print("\t4) Finalizar el programa")
    print("-----------------------------------------------")


def registrar_cuenta(registro):
    user = input("Ingrese un nombre de usuario: ")
    while (user.count(' ') > 0 or len(user)<5):
        print("El nombre de usuario debe tener 5 o mas caracteres y no puede tener espacios")
        user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    while (password.count(" ") > 0 or len(password)<8):
        print("La contraseña debe tener 8 o mas caracteres y no puede tener espacios")
        password = input("Ingrese una contraseña: ")
    almacenar(user, password, registro)


# ______PROGRAMA PRINCIPAL______
registro = {}
actualizar_registro(registro)

while True:
    imprimir_menu()
    num = input("Ingrese un numero: ")
    os.system('cls')
    if (num == '4'):
        print("El programa ha finalizado.")
        break
    elif (num == '1'):
        registrar_cuenta(registro)
    elif (num == '2'):
        imprimir(registro)
    elif (num == '3'):
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        login(user, password, registro)
    else:
        print("No ha seleccionado una opcion valida")

    fin = input("\n Precione ENTER para volver al menu")
