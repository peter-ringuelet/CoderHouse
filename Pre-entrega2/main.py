from paquete_cliente.cliente import Cliente
import os 

def menu():
    os.system('clear')
    print("--------------------OPCIONES-------------------")
    print("\t 1) Ingresar sus datos: ")
    print("\t 2) Imprimir tus datos")
    print("\t 3) Comprar algo")
    print("\t 4) Cargar sueldo: ")
    print("\t 5) Verificar si es mayor de edad")
    print("\t 6) Finalizar el programa")
    print("-----------------------------------------------")

def cargar_cliente():
     nombre = input("Nombre: ")
     apellido = input("Apellido: ")
     mail = input("Mail: ")
     edad = int(input("Edad: "))
     dni = int(input("DNI: "))
     id = int(input("ID: "))
     saldo = int(input("Saldo: "))
     cliente = Cliente(nombre,apellido,mail,edad,dni,id,saldo)
     return cliente
 
def comprar(productos,cliente):
    producto = input("Ingrese el nombre del producto que quiere comprar(Teclado/Mouse): ")
    if producto in productos:
        cliente.comprar(productos[producto])
    else:
        print("El producto que se ha ingresado no esta disponible")
        
def actualizar_sueldo(cliente):
    dinero = int(input("Dinero que desea ingresar: "))
    cliente.cargar_sueldo(dinero)
    
     

productos = {"Teclado":250, "Mouse":150}

while True:
    menu()
    num = input("Ingrese un numero: ")
    if num == '1':
        cliente = cargar_cliente()
    else:
        try:
            if num == '2':
                print(cliente)
            elif num == '3':
                comprar(productos,cliente)
            elif num == '4':
                actualizar_sueldo(cliente)
            elif num == '5':
                cliente.es_mayor_de_edad()
            elif num == '6':
                break
            else:
                print("No se ha ingresado una opcion correcta")
        except:
            print("No se han cargado datos de ningun cliente aun")
    
        
    resetear = input("precione una tecla para volver al menu")
print("Se ha finalizado correctamente el programa")
        

