import unittest
from panda import Panda
from panda import PandaSocialNetwork
from panda import PandaAlreadyThere


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_init(self):
        self.assertEqual(self.ivo._name, "Ivo")
        self.assertEqual(self.ivo._email, "ivo@pandamail.com")
        self.assertEqual(self.ivo._gender, "male")

    def test_str(self):
        result = "The panda name, email and gender are Ivo, ivo@pandamail.com and male"
        self.assertEqual(str(self.ivo), result)

    def test_equal(self):
        alf = Panda("Ivan", "Ceco@abv.bg", "male")
        self.assertTrue(self.ivo == self.ivo)
        self.assertFalse(self.ivo == alf)

    def test_email(self):
        with self.assertRaises(ValueError):
            self.ivo.set_email("123")

        self.ivo.set_email("asd@asd.bg")
        self.assertEqual(self.ivo._email, "asd@asd.bg")

    def test_isMale(self):
        self.assertEqual(self.ivo._gender, "male")

    def test_hash(self):
        result = self.ivo.__hash__()
        self.assertTrue(isinstance(result, int))


class TestPandaSocialNetwork(unittest.TestCase):

    def test_add_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.test_add_panda(panda)

if __name__ == '__main__':
    unittest.main()
