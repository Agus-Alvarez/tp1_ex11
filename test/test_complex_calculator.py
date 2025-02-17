import sys
import os
import unittest
import logging

# Configuración básica del logger para pruebas
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# calculator_package/test/test_complex_calculator.py
from calculator.complex_calculator import SimpleComplexCalculator

class TestSimpleComplexCalculator(unittest.TestCase):
    """
    Pruebas unitarias para la calculadora de números complejos.
    Incluye pruebas de validación de tipos y manejo de errores.
    """
    
    def setUp(self):
        """Inicializa el ambiente de pruebas."""
        self.calc = SimpleComplexCalculator()
        # Números de prueba
        self.enteros1 = [4, 5]  # Números enteros
        self.enteros2 = [2, 3]
        self.flotantes1 = [4.67, 5.89]  # Números flotantes
        self.flotantes2 = [2.0, 3.0]
        self.mixtos1 = [1, 2.5]  # Mezcla de tipos
        self.mixtos2 = [3.5, 4]
    
    def test_operaciones_con_enteros(self):
        """Prueba las operaciones básicas con números enteros."""
        # Suma
        resultado = self.calc.sumar(self.enteros1, self.enteros2)
        self.assertEqual(resultado[0], 6)
        self.assertEqual(resultado[1], 8)
        
        # Resta
        resultado = self.calc.restar(self.enteros1, self.enteros2)
        self.assertEqual(resultado[0], 2)
        self.assertEqual(resultado[1], 2)
        
        # Multiplicación
        resultado = self.calc.multiplicar(self.enteros1, self.enteros2)
        self.assertEqual(resultado[0], -7)  # (4*2 - 5*3)
        self.assertEqual(resultado[1], 22)  # (4*3 + 5*2)
    
    def test_operaciones_con_flotantes(self):
        """Prueba las operaciones básicas con números flotantes."""
        # Suma
        resultado = self.calc.sumar(self.flotantes1, self.flotantes2)
        self.assertAlmostEqual(resultado[0], 6.67)
        self.assertAlmostEqual(resultado[1], 8.89)
        
        # Resta
        resultado = self.calc.restar(self.flotantes1, self.flotantes2)
        self.assertAlmostEqual(resultado[0], 2.67)
        self.assertAlmostEqual(resultado[1], 2.89)
    
    def test_operaciones_con_tipos_mixtos(self):
        """Prueba las operaciones con mezcla de enteros y flotantes."""
        resultado = self.calc.sumar(self.mixtos1, self.mixtos2)
        self.assertAlmostEqual(resultado[0], 4.5)
        self.assertAlmostEqual(resultado[1], 6.5)
    
    def test_division_por_cero(self):
        """Prueba la división por cero."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(self.enteros1, [0, 0])
    
    def test_entradas_invalidas(self):
        """Prueba el manejo de entradas inválidas."""
        # Entrada no es lista
        self.assertEqual(self.calc.sumar("no lista", self.enteros1), "ERROR")
        
        # Lista con elementos no numéricos
        self.assertEqual(self.calc.sumar([1, "a"], self.enteros1), "ERROR")
        
        # Lista con longitud incorrecta
        self.assertEqual(self.calc.sumar([1], self.enteros1), "ERROR")
    
    def test_formato_complejo(self):
        """Prueba el formateo de números complejos."""
        # Formato normal
        self.assertEqual(self.calc.formato_complejo([1.23, 4.56]), "1.23 + 4.56i")
        self.assertEqual(self.calc.formato_complejo([1.23, -4.56]), "1.23 - 4.56i")
        
        # Formato con entradas inválidas
        self.assertEqual(self.calc.formato_complejo([1, "a"]), "ERROR")
        self.assertEqual(self.calc.formato_complejo([1]), "ERROR")
        self.assertEqual(self.calc.formato_complejo("no lista"), "ERROR")
    
    def test_division_valida(self):
        """Prueba una división válida."""
        resultado = self.calc.dividir([1, 1], [1, 0])  # (1+i)/(1+0i)
        self.assertAlmostEqual(resultado[0], 1.0)
        self.assertAlmostEqual(resultado[1], 1.0)
    
    def test_validacion_tipos_especificos(self):
        """Prueba validaciones específicas de tipos."""
        # Lista con None
        self.assertEqual(self.calc.sumar([None, 1], self.enteros1), "ERROR")
        
        # Lista con booleanos
        self.assertEqual(self.calc.sumar([True, False], self.enteros1), "ERROR")
        
        # Lista con números complejos de Python
        self.assertEqual(self.calc.sumar([1+2j, 3], self.enteros1), "ERROR")
    
    def tearDown(self):
        """Al finalizar las pruebas, imprimimos los logs."""
        logger.info("Pruebas completadas.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
