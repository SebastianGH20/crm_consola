import json
import os
from models.usuario import Usuario
from utils.validaciones import email_valido, campos_obligatorios_completos
from utils.helpers import generar_id

RUTA_USUARIOS = "data/usuarios.json"

def cargar_usuarios():
    if not os.path.exists(RUTA_USUARIOS):
        return []
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_usuarios(lista_usuarios):
    with open(RUTA_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)

def registrar_usuario():
    print("=== REGISTRO DE NUEVO USUARIO ===")
    nombre = input("Ingrese nombre: ").strip()
    apellidos = input("Ingrese apellidos: ").strip()
    email = input("Ingrese email: ").strip()
    telefono = input("Ingrese teléfono (opcional): ").strip()
    direccion = input("Ingrese dirección (opcional): ").strip()

    datos = {"nombre": nombre, "apellidos": apellidos, "email": email}
    completos, campo_faltante = campos_obligatorios_completos(datos, ["nombre", "apellidos", "email"])
    if not completos:
        print(f"Error: El campo '{campo_faltante}' es obligatorio.")
        return

    if not email_valido(email):
        print("Error: El email no tiene un formato válido.")
        return

    usuarios = cargar_usuarios()
    if any(u["email"] == email for u in usuarios):
        print("Error: Ya existe un usuario con ese email.")
        return

    nuevo_usuario = Usuario(nombre, apellidos, email, telefono, direccion)
    nuevo_usuario.id = generar_id("USR", RUTA_USUARIOS)

    # Convertimos el usuario a dict para guardar
    usuarios.append({
        "id": nuevo_usuario.id,
        "nombre": nuevo_usuario.nombre,
        "apellidos": nuevo_usuario.apellidos,
        "email": nuevo_usuario.email,
        "telefono": nuevo_usuario.telefono,
        "direccion": nuevo_usuario.direccion,
        "fecha_registro": nuevo_usuario.fecha_registro
    })

    guardar_usuarios(usuarios)

    print("\nUsuario registrado exitosamente!")
    print(f"ID asignado: {nuevo_usuario.id}")
    print(f"Fecha de registro: {nuevo_usuario.fecha_registro}")

def buscar_usuario():
    print("=== BUSCAR USUARIO ===")
    print("1. Buscar por email")
    print("2. Buscar por nombre")
    opcion = input("Seleccione método de búsqueda: ")

    usuarios = cargar_usuarios()

    if opcion == "1":
        email = input("Ingrese email: ").strip()
        encontrados = [u for u in usuarios if u["email"].lower() == email.lower()]
    elif opcion == "2":
        nombre = input("Ingrese nombre: ").strip()
        encontrados = [u for u in usuarios if nombre.lower() in u["nombre"].lower()]
    else:
        print("Opción no válida.")
        return

    if not encontrados:
        print("No se encontraron usuarios.")
        return

    for u in encontrados:
        print("\n--- USUARIO ENCONTRADO ---")
        print(f"ID: {u['id']}")
        print(f"Nombre: {u['nombre']} {u['apellidos']}")
        print(f"Email: {u['email']}")
        print(f"Teléfono: {u.get('telefono', 'No especificado')}")
        print(f"Dirección: {u.get('direccion', 'No especificada')}")
        print(f"Fecha de registro: {u['fecha_registro']}")

def mostrar_todos_los_usuarios():
    print("=== LISTA DE USUARIOS ===")
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for i, u in enumerate(usuarios, start=1):
        print(f"\nUsuario #{i}:")
        print(f"ID: {u['id']}")
        print(f"Nombre: {u['nombre']} {u['apellidos']}")
        print(f"Email: {u['email']}")
        print(f"Teléfono: {u.get('telefono', 'No especificado')}")
        print(f"Fecha de registro: {u['fecha_registro']}")

    print(f"\nTotal de usuarios registrados: {len(usuarios)}")
