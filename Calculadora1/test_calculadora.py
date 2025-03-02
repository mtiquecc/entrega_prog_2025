import unittest
from unittest.mock import patch
from io import StringIO
from Calculadora1.main import calculadora  # Importamos la función desde el script original

"""
    Los test nos permite comprobar el buen funcionammiento de nuestro codigo
    los test unitario comprueba el funcionamiento por unidad como una clase, un modulo o una funcion
    nos permite la deteccion de errores y pone a prueba nuestro codigo
"""
class TestCalculadora(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "5", "3"])  # Simula elegir "sumar" y los números 5 y 3
    @patch("sys.stdout", new_callable=StringIO)  # Captura la salida en la consola
    
    #test para la opcion de suma 
    def test_suma(self, mock_stdout, mock_input):
        calculadora()
        resultado = mock_stdout.getvalue().strip()
        self.assertIn("Resultado: 5.0 + 3.0 = 8.0", resultado)

    @patch("builtins.input", side_effect=["4", "10", "0"])  # Simula elegir "dividir" y los números 10 y 0
    @patch("sys.stdout", new_callable=StringIO)
    def test_division_por_cero(self, mock_stdout, mock_input):
        calculadora()
        resultado = mock_stdout.getvalue().strip()
        self.assertIn("Error: No se puede dividir entre cero.", resultado)

if __name__ == "__main__":
    unittest.main()
