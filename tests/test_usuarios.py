import unittest
from utils.validaciones import email_valido, campos_obligatorios_completos

class TestValidacionesUsuario(unittest.TestCase):
    def test_email_valido(self):
        self.assertTrue(email_valido("test@email.com"))
        self.assertFalse(email_valido("correo_invalido"))

    def test_campos_obligatorios_completos(self):
        datos = {"nombre": "Ana", "apellidos": "López", "email": "ana@email.com"}
        campos = ["nombre", "apellidos", "email"]
        resultado, _ = campos_obligatorios_completos(datos, campos)
        self.assertTrue(resultado)

        datos_incompletos = {"nombre": "", "apellidos": "López", "email": ""}
        resultado, campo = campos_obligatorios_completos(datos_incompletos, campos)
        self.assertFalse(resultado)
        self.assertIn(campo, ["nombre", "email"])
