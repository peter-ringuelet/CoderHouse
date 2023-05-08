class Persona():
    def __init__(self, nombre, apellido, mail, edad, dni) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.edad = edad
        self.dni = dni

    # Métodos get
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_mail(self):
        return self.mail

    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni

    # Métodos set
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_mail(self, mail):
        self.mail = mail

    def set_edad(self, edad):
        self.edad = edad
    
    def set_dni(self,dni):
        self.dni = dni
    
    # Metodo toString
    def __str__(self) -> str:
        return f"{self.nombre}-{self.apellido}-{self.mail}-{self.edad}-{self.dni}"

    