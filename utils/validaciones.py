import re

def email_valido(email):
    """
    Verifica que el email tenga un formato válido.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, email) is not None

def campos_obligatorios_completos(datos, campos_obligatorios):
    """
    Verifica que todos los campos obligatorios no estén vacíos.
    `datos` es un diccionario con los datos del formulario.
    """
    for campo in campos_obligatorios:
        valor = datos.get(campo, "").strip()
        if not valor:
            return False, campo
    return True, None

def monto_valido(monto_str):
    """
    Verifica que el monto ingresado sea un número positivo.
    """
    try:
        monto = float(monto_str)
        return monto > 0
    except ValueError:
        return False
