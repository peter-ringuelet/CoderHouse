from cliente import Cliente
import os
import time

def menu():
    '''
    Imprime el menu y retorna la opcion seleccionada
    '''
    os.system('cls')
    print("Menú de opciones:")
    print("1. Crear cliente")
    print("2. Consultar datos del cliente")
    print("3. Modificar datos del cliente")
    print("4. Salir")
    opcion = input("Ingrese la opción que desea: ")
    return opcion


def crear_cliente():
    id_cliente = (input("Ingrese el ID del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    sueldo = input("Ingrese el sueldo del cliente: ")

    cliente = Cliente(id_cliente, nombre, email, sueldo)
    print("Cliente creado exitosamente.")
    return cliente


def consultar_datos(cliente):
    if cliente is not None:
        print(cliente)  # Aquí se llama al método __str__ de la clase Cliente
    else:
        print("No hay ningún cliente creado.")


def modificar_datos(cliente):
    if cliente is not None:
        id_cliente = int(input("Ingrese el nuevo ID del cliente: "))
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        email = input("Ingrese el nuevo email del cliente: ")
        sueldo = input("Ingrese el nuevo saldo del cliente: ")

        cliente.set_id(id_cliente)
        cliente.set_nombre(nombre)
        cliente.set_email(email)
        cliente.set_sueldo(sueldo)

        print("Datos del cliente modificados exitosamente.")
    else:
        print("No hay ningún cliente creado.")


def main():
    cliente = None

    while True:
        opcion = menu()

        if opcion == '1':
            cliente = crear_cliente()
            reset = input("Precione cualquier tecla para vovler al menu")
        elif opcion == '2':
            consultar_datos(cliente)
            reset = input("Precione cualquier tecla para vovler al menu")
        elif opcion == '3':
            modificar_datos(cliente)
            reset = input("Precione cualquier tecla para vovler al menu")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción correcta.")


if __name__ == "__main__":
    main()
