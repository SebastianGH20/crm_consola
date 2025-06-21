import json
import os
from models.factura import Factura
from utils.helpers import generar_id
from utils.validaciones import monto_valido
from services.gestor_usuarios import cargar_usuarios

RUTA_FACTURAS = "data/facturas.json"

def cargar_facturas():
    if not os.path.exists(RUTA_FACTURAS):
        return []
    with open(RUTA_FACTURAS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_facturas(lista_facturas):
    with open(RUTA_FACTURAS, "w", encoding="utf-8") as f:
        json.dump(lista_facturas, f, indent=4, ensure_ascii=False)

def crear_factura():
    print("=== CREAR FACTURA ===")
    email = input("Ingrese email del usuario: ").strip()
    usuarios = cargar_usuarios()
    usuario = next((u for u in usuarios if u["email"].lower() == email.lower()), None)

    if not usuario:
        print("Error: No se encontró un usuario con ese email.")
        return

    print(f"\nUsuario encontrado: {usuario['nombre']} {usuario['apellidos']}")
    descripcion = input("Ingrese descripción del servicio/producto: ").strip()
    monto_str = input("Ingrese monto total: ").strip()

    if not monto_valido(monto_str):
        print("Error: El monto debe ser un número positivo.")
        return

    print("Seleccione estado:")
    print("1. Pendiente")
    print("2. Pagada")
    print("3. Cancelada")
    opcion_estado = input("Estado: ").strip()
    estado_map = {"1": "Pendiente", "2": "Pagada", "3": "Cancelada"}
    estado = estado_map.get(opcion_estado, "Pendiente")

    nueva_factura = Factura(descripcion, monto_str, estado)
    nueva_factura.numero = generar_id("FAC", RUTA_FACTURAS)

    facturas = cargar_facturas()
    facturas.append({
        "numero": nueva_factura.numero,
        "fecha_emision": nueva_factura.fecha_emision,
        "email_usuario": usuario["email"],
        "descripcion": nueva_factura.descripcion,
        "monto": nueva_factura.monto,
        "estado": nueva_factura.estado
    })

    guardar_facturas(facturas)

    print("\nFactura creada exitosamente!")
    print(f"Número de factura: {nueva_factura.numero}")
    print(f"Fecha de emisión: {nueva_factura.fecha_emision}")
    print(f"Cliente: {usuario['nombre']} {usuario['apellidos']}")
    print(f"Descripción: {nueva_factura.descripcion}")
    print(f"Monto: ${nueva_factura.monto:.2f}")
    print(f"Estado: {nueva_factura.estado}")

def mostrar_facturas_de_usuario():
    print("=== FACTURAS POR USUARIO ===")
    email = input("Ingrese email del usuario: ").strip()
    usuarios = cargar_usuarios()
    usuario = next((u for u in usuarios if u["email"].lower() == email.lower()), None)

    if not usuario:
        print("Error: Usuario no encontrado.")
        return

    facturas = cargar_facturas()
    facturas_usuario = [f for f in facturas if f["email_usuario"].lower() == email.lower()]

    if not facturas_usuario:
        print(f"No hay facturas registradas para {usuario['nombre']} {usuario['apellidos']}.")
        return

    print(f"\n--- FACTURAS DE {usuario['nombre']} {usuario['apellidos']} ---")
    total = 0
    pendientes = 0

    for i, f in enumerate(facturas_usuario, start=1):
        print(f"\nFactura #{i}:")
        print(f"Número: {f['numero']}")
        print(f"Fecha: {f['fecha_emision']}")
        print(f"Descripción: {f['descripcion']}")
        print(f"Monto: ${f['monto']:.2f}")
        print(f"Estado: {f['estado']}")

        total += f["monto"]
        if f["estado"] == "Pendiente":
            pendientes += f["monto"]

    print(f"\nTotal de facturas: {len(facturas_usuario)}")
    print(f"Monto total facturado: ${total:.2f}")
    print(f"Monto pendiente: ${pendientes:.2f}")
