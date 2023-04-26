class Cliente:
    def __init__(self, id, nombre, email, saldo):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._saldo = saldo

    def __str__(self):
        return f"Cliente: {self._nombre}, Email: {self._email}, Id: {self._id}, Saldo: {self._saldo}"

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def get_saldo(self):
        return self._saldo

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_email(self, email):
        self._email = email

    def set_saldo(self, saldo):
        self._saldo = saldo

    def agregar_saldo(self, monto):
        self._saldo += monto
        return self._saldo

    def realizar_compra(self, monto):
        if self._saldo >= monto:
            self._saldo -= monto
            return True
        else:
            return False
