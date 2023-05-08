from paquete_persona.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, mail, edad, dni, id, sueldo):
        super().__init__(nombre, apellido, mail,edad,dni)
        self.id = id
        self.sueldo = sueldo

    # Métodos get
    def get_id(self):
        return self.id

    def get_sueldo(self):
        return self.sueldo

    # Métodos set
    def set_id(self,id):
        self.id = id

    def set_sueldo(self, sueldo):
        self.sueldo = sueldo
    
    # Metodo toString
    def __str__(self) -> str:
        return f"{super().__str__()}-{self.id}-${self.sueldo}"

    #Metodos extra
    def comprar(self,precio):
        if (self.sueldo >= precio):
            self.sueldo -= precio
            print ("Se ha comprado exitosamente")
        else:
            print("No dispone del dinero suficiente para comprar el producto")
    
    def cargar_sueldo(self,monto):
        self.sueldo += monto
        print(f"Se ha cargado exitosamente el sueldo, ahora dispone de ${self.sueldo}")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
    
    
        
    