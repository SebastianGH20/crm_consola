from datetime import datetime

class Usuario:
    def __init__(self, nombre, apellidos, email, telefono=None, direccion=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y")
        self.id = None  # Se asignará externamente con formato USR001, USR002, etc.
        self.facturas = []  # Lista de facturas asociadas a este usuario

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.email})"
