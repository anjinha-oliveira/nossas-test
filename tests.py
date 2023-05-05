import unittest
from main import contem_duplicados

class TestArrayDistinto(unittest.TestCase):
    def test_array_numeros_duplicados(self):
        self.assertEqual(contem_duplicados([1, 2, 3, 3]), True)

    def test_array_sem_numeros_duplicados(self):
        self.assertEqual(contem_duplicados([1, 2, 3]), False)  

    def test_array_vazio(self):
        self.assertEqual(contem_duplicados([]), False)

    def test_array_com_mais_de_um_numero_duplicado(self):
        self.assertEqual(contem_duplicados([1, 2, 3, 1, 5, 6, 6]), True)


if __name__ == '__main__':
    unittest.main()