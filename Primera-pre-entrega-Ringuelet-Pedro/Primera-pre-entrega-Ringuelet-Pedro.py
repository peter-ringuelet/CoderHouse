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
        guardar_db(registro)
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

def guardar_db(registro):
    '''
    INPUT: diccionario con los usuarios y contraseñas

    OUTPUT: agrega al archivo db.json el diccionario de usuarios y contraseñas
    '''
    with open("db.json", "w") as file:
        json.dump(registro, file, indent=4)

def cargar_registro(registro):
    '''
    INPUT: registro(diccionario) donde se almacenaran los usuarios y contraseñas de la base de datos

    OUTPUT: devuelve el diccionario con todo el contenido de la base de datos(archivo .json)
    '''
    try:
        with open("db.json", "r") as file:
            registro.update(json.load(file))
    except:
        crear_archivo()

def crear_archivo():
    '''
    INPUT: no recibe parametros

    OUTPUT: crea un archivo .json vacio en la carpeta donde se esta ejecutando el programa
    '''
    with open("db.json", "w") as file:
        json.dump({}, file, indent=4)

def imprimir_menu():
    '''
    INPUT: no recibe parametros

    OUTPUT: imprime en pantalla el menu con todas las opciones
    '''
    os.system('cls')
    print("--------------------OPCIONES-------------------")
    print("\t1) Registrar cuenta")
    print("\t2) Imprimir todos los usuarios con sus contraseñas")
    print("\t3) Login")
    print("\t4) Finalizar el programa")
    print("-----------------------------------------------")

def registrar_cuenta(registro):
    '''
    INPUT: recive un registro(diccionario) en el cual se almacenan todos los user-password

    OUTPU: en caso de no estar registrado el usuario, lo agrega al registro(diccionario) y a la base de datos(archivo .json), sino se debera ingresar un usuario nuevo y/o contraseña
    '''
    user = input("Ingrese un nombre de usuario: ")
    while (user.count(' ') > 0 or len(user) < 5):
        print(
            "El nombre de usuario debe tener 5 o mas caracteres y no puede tener espacios")
        user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    while (password.count(" ") > 0 or len(password) < 8):
        print("La contraseña debe tener 8 o mas caracteres y no puede tener espacios")
        password = input("Ingrese una contraseña: ")
    almacenar(user, password, registro)


# ______PROGRAMA PRINCIPAL______
registro = {}
cargar_registro(registro)

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
