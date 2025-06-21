from services.gestor_usuarios import cargar_usuarios
from services.gestor_facturas import cargar_facturas

def resumen_financiero():
    print("=== RESUMEN FINANCIERO ===")

    usuarios = cargar_usuarios()
    facturas = cargar_facturas()

    total_usuarios = len(usuarios)
    total_facturas = len(facturas)
    total_ingresos = 0
    ingresos_pagados = 0
    ingresos_pendientes = 0

    for u in usuarios:
        email = u["email"]
        facturas_usuario = [f for f in facturas if f["email_usuario"].lower() == email.lower()]
        total_usuario = sum(f["monto"] for f in facturas_usuario)
        pagadas = sum(f["monto"] for f in facturas_usuario if f["estado"] == "Pagada")
        pendientes = sum(f["monto"] for f in facturas_usuario if f["estado"] == "Pendiente")

        total_ingresos += total_usuario
        ingresos_pagados += pagadas
        ingresos_pendientes += pendientes

        print(f"\nUsuario: {u['nombre']} {u['apellidos']} ({u['email']})")
        print(f"- Total facturas: {len(facturas_usuario)}")
        print(f"- Monto total: ${total_usuario:.2f}")
        print(f"- Facturas pagadas: ${pagadas:.2f}")
        print(f"- Facturas pendientes: ${pendientes:.2f}")

    print("\n--- RESUMEN GENERAL ---")
    print(f"Total usuarios: {total_usuarios}")
    print(f"Total facturas emitidas: {total_facturas}")
    print(f"Ingresos totales: ${total_ingresos:.2f}")
    print(f"Ingresos recibidos: ${ingresos_pagados:.2f}")
    print(f"Ingresos pendientes: ${ingresos_pendientes:.2f}")
