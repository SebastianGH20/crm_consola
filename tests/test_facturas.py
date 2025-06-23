import unittest
from utils.validaciones import monto_valido

class TestValidacionesFactura(unittest.TestCase):
    def test_monto_valido(self):
        self.assertTrue(monto_valido("100.50"))
        self.assertFalse(monto_valido("-45"))
        self.assertFalse(monto_valido("abc"))
