from desviacionEstandar import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular
import unittest
import math


# Pruebas unitarias
class TestPromedio(unittest.TestCase):
    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_un_elemento(self):
        self.assertEqual(calcular_promedio([5]), 5)

    def test_dos_elementos(self):
        self.assertEqual(calcular_promedio([5, 10]), 7.5)

    def test_n_elementos_positivos(self):
        self.assertEqual(calcular_promedio([1, 2, 3, 4, 5]), 3)

    def test_todos_ceros(self):
        self.assertEqual(calcular_promedio([0, 0, 0, 0]), 0)

    def test_n_elementos_positivos_negativos(self):
        self.assertEqual(calcular_promedio([1, -1, 2, -2, 3, -3]), 0)

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_promedio([1, 'a', 3])


class TestDesviacionEstandar(unittest.TestCase):
    def test_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

    def test_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([5, 10]), 2.5)

    def test_n_elementos_positivos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), math.sqrt(2))

    def test_todos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0, 0]), 0)

    def test_n_elementos_positivos_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, -1, 2, -2, 3, -3]), math.sqrt(4))

    def test_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([1, 'a', 3])


if __name__ == '__main__':
    unittest.main()
