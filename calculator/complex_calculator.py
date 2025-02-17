# calculator_package/
# ├── calculator/
# │   ├── __init__.py
# │   └── complex_calculator.py
# └── test/
#     ├── __init__.py
#     └── test_complex_calculator.py

import logging

# Configuración básica del logger
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class SimpleComplexCalculator:
    """
    Calculadora de números complejos que realiza operaciones aritméticas básicas.
    Incluye validaciones de tipo y manejo de errores.
    """
    
    def __init__(self):
        pass
    
    def _validar_numeros(self, c1: list, c2: list) -> None:
        """
        Valida que las entradas sean listas de dos números.
        
        Args:
            c1, c2: Números complejos en formato [real, imaginario]
            
        Raises:
            TypeError: Si los argumentos no son del tipo correcto
            ValueError: Si las listas no tienen el formato correcto
        """
        if not isinstance(c1, list) or not isinstance(c2, list):
            logger.error("Los argumentos deben ser listas, pero se recibieron tipos incorrectos.")
            raise TypeError("Los argumentos deben ser listas")
        if len(c1) != 2 or len(c2) != 2:
            logger.error("Los números complejos deben ser listas de dos elementos.")
            raise ValueError("Los números complejos deben ser listas de dos elementos")
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in c1 + c2):
            logger.error("Todos los elementos deben ser números enteros o flotantes.")
            raise TypeError("Todos los elementos deben ser números enteros o flotantes")
    
    def sumar(self, c1: list, c2: list) -> list:
        """
        Suma dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            resultado = [c1[0] + c2[0], c1[1] + c2[1]]
            logger.info(f"Suma exitosa: {c1} + {c2} = {resultado}")
            return resultado
        except (TypeError, ValueError) as e:
            logger.error(f"Error al sumar {c1} y {c2}: {e}")
            return "ERROR"
    
    def restar(self, c1: list, c2: list) -> list:
        """
        Resta dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            resultado = [c1[0] - c2[0], c1[1] - c2[1]]
            logger.info(f"Resta exitosa: {c1} - {c2} = {resultado}")
            return resultado
        except (TypeError, ValueError) as e:
            logger.error(f"Error al restar {c1} y {c2}: {e}")
            return "ERROR"
    
    def multiplicar(self, c1: list, c2: list) -> list:
        """
        Multiplica dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            real = c1[0] * c2[0] - c1[1] * c2[1]
            imaginario = c1[0] * c2[1] + c1[1] * c2[0]
            resultado = [real, imaginario]
            logger.info(f"Multiplicación exitosa: {c1} * {c2} = {resultado}")
            return resultado
        except (TypeError, ValueError) as e:
            logger.error(f"Error al multiplicar {c1} y {c2}: {e}")
            return "ERROR"
    
    def dividir(self, c1: list, c2: list) -> list:
        """
        Divide dos números complejos con validación.
        
        Raises:
            ZeroDivisionError: Si el denominador es cero
        """
        try:
            self._validar_numeros(c1, c2)
            denominador = c2[0]**2 + c2[1]**2
            if denominador == 0:
                logger.error("Error de división: El denominador es cero.")
                raise ZeroDivisionError("No se puede dividir por cero")
            
            real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominador
            imaginario = (c1[1] * c2[0] - c1[0] * c2[1]) / denominador
            resultado = [real, imaginario]
            logger.info(f"División exitosa: {c1} / {c2} = {resultado}")
            return resultado
        except ZeroDivisionError as e:
            logger.error(f"Error de división: {e}")
            raise e
        except (TypeError, ValueError) as e:
            logger.error(f"Error al dividir {c1} y {c2}: {e}")
            return "ERROR"
    
    @staticmethod
    def formato_complejo(c: list) -> str:
        """
        Formatea un número complejo como string.
        """
        try:
            if not isinstance(c, list) or len(c) != 2:
                logger.error(f"Formato inválido para número complejo: {c}")
                return "ERROR"
            if not all(isinstance(x, (int, float)) for x in c):
                logger.error(f"Los elementos de {c} deben ser números enteros o flotantes.")
                return "ERROR"
            if c[1] >= 0:
                return f"{c[0]:.2f} + {c[1]:.2f}i"
            return f"{c[0]:.2f} - {abs(c[1]):.2f}i"
        except Exception as e:
            logger.error(f"Error al formatear número complejo {c}: {e}")
            return "ERROR"
