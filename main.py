from services.gestor_usuarios import (
    registrar_usuario,
    buscar_usuario,
    mostrar_todos_los_usuarios
)

from services.gestor_facturas import (
    crear_factura,
    mostrar_facturas_de_usuario
)

from services.resumen_financiero import resumen_financiero

def mostrar_menu():
    print("\n=== SISTEMA CRM ===")
    print("1. Registrar nuevo usuario")
    print("2. Buscar usuario")
    print("3. Crear factura para usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Mostrar facturas de un usuario")
    print("6. Resumen financiero por usuario")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            crear_factura()
        elif opcion == "4":
            mostrar_todos_los_usuarios()
        elif opcion == "5":
            mostrar_facturas_de_usuario()
        elif opcion == "6":
            resumen_financiero()
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
