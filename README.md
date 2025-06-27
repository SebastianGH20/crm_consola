
# Sistema CRM por Consola

Este proyecto es una práctica final de la asignatura Tipología de Datos. Consiste en el desarrollo de un sistema básico de gestión de relaciones con clientes (CRM), ejecutado íntegramente desde consola usando Python.

## 📌 Funcionalidades

- Registrar nuevos usuarios con validación de campos y email único.
- Buscar usuarios por nombre o email.
- Crear facturas asociadas a usuarios existentes.
- Listar todos los usuarios registrados.
- Mostrar todas las facturas asociadas a un usuario específico.
- Generar un resumen financiero por usuario y resumen global.

## 🗂️ Estructura del Proyecto

```
crm_consola/
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── usuarios.json
│   └── facturas.json
│
├── models/
│   ├── usuario.py
│   └── factura.py
│
├── services/
│   ├── gestor_usuarios.py
│   ├── gestor_facturas.py
│   └── resumen_financiero.py
│
├── utils/
│   ├── helpers.py
│   └── validaciones.py
│
└── tests/
    ├── test_usuarios.py
    └── test_facturas.py
```

## 🧠 Tecnologías utilizadas

- Python 3.x
- JSON para persistencia
- Módulos estándar: `datetime`, `os`, `json`, `re`

## 🧪 Ejecución

Para ejecutar correctamente el proyecto:

Ingresa al directorio del repositorio clonado:

```bash
cd crm_consola
```

Asegúrate de tener Python instalado y ejecuta:

```bash
python main.py
```

## ✍️ Autor

Sebastián González Hincapié
