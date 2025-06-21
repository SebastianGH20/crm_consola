import json
import os
from datetime import datetime

def generar_id(prefijo, ruta_archivo, clave_id="id"):
    """
    Genera un nuevo ID único a partir del prefijo dado (USR o FAC)
    y la cantidad de elementos ya guardados en el archivo de datos.
    """
    if not os.path.exists(ruta_archivo):
        return f"{prefijo}001"

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            datos = []

    total = len(datos)
    nuevo_id = f"{prefijo}{total + 1:03}"
    return nuevo_id

def obtener_fecha_actual():
    """Devuelve la fecha y hora actual en formato dd/mm/yyyy HH:MM"""
    return datetime.now().strftime("%d/%m/%Y %H:%M")
