from datetime import datetime

class Factura:
    ESTADOS_VALIDOS = ["Pendiente", "Pagada", "Cancelada"]

    def __init__(self, descripcion, monto, estado):
        self.numero = None  # Se asignará externamente con formato FAC001, FAC002, etc.
        self.fecha_emision = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.descripcion = descripcion
        self.monto = float(monto)
        self.estado = estado if estado in self.ESTADOS_VALIDOS else "Pendiente"

    def __str__(self):
        return (f"Número: {self.numero}\n"
                f"Fecha: {self.fecha_emision}\n"
                f"Descripción: {self.descripcion}\n"
                f"Monto: ${self.monto:.2f}\n"
                f"Estado: {self.estado}")
