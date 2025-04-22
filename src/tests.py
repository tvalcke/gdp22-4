import unittest
from utils import calculer_moyenne

class TestCalculerMoyenne(unittest.TestCase):

    def test_moyenne_nombres_entiers(self):
        self.assertEqual(calculer_moyenne([2, 4, 6, 8]), 5.0)

    def test_moyenne_nombres_flottants(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5]), 2.5)

    def test_moyenne_melange_int_float(self):
        self.assertAlmostEqual(calculer_moyenne([1, 2.0, 3]), 2.0)

    def test_liste_vide(self):
        self.assertIsNone(calculer_moyenne([]))

    def test_element_non_numerique(self):
        with self.assertRaises(TypeError):
            calculer_moyenne([1, 'a', 3])

    def test_element_bool(self):
        self.assertEqual(calculer_moyenne([True, False, 1]), 2/3)  # True=1, False=0

if __name__ == '__main__':
    unittest.main()

#writted by chatGPT
