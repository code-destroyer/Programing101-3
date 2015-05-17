import unittest
from panda import Panda
from panda import PandaSocialNetwork
# from panda import PandaAlreadyThere


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_init(self):
        self.assertEqual(self.ivo.name, "Ivo")
        self.assertEqual(self.ivo.email, "ivo@pandamail.com")
        self.assertEqual(self.ivo.gender, "male")

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
        self.assertEqual(self.ivo.email, "asd@asd.bg")

    def test_isMale(self):
        self.assertEqual(self.ivo.gender, "male")

    def test_isMale(self):
        self.assertNotEqual(self.ivo.gender, "female")

    def test_hash(self):
        result = self.ivo.__hash__()
        self.assertTrue(isinstance(result, int))


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.network = PandaSocialNetwork()
        self.panda = Panda("iva", "iva1@abv.bg", "female")
        self.other_panda = Panda("ivan", "iiivvan@abv.bg", "male")

    def test_add_panda(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.ivo in self.network.network_pandas)

    def test_has_panda(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.network.has_panda(self.ivo))
        self.assertFalse(self.network.has_panda(self.panda))

    def test_are_friends(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.panda)
        self.network.add_panda(self.other_panda)
        self.network.make_friends(self.ivo, self.panda)
        self.assertTrue(self.network.are_friends(self.ivo, self.panda))
        self.assertFalse(self.network.are_friends(self.ivo, self.other_panda))

    def test_make_friends(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.panda)
        self.assertTrue(self.network.has_panda(self.ivo))
        self.assertTrue(self.network.has_panda(self.panda))
        self.network.make_friends(self.ivo, self.panda)
        result = {self.ivo: [self.panda],
                  self.panda: [self.ivo]}
        self.assertEqual(self.network.network_pandas, result)

    def test_friends_of(self):
        self.assertFalse(self.network.friends_of(self.ivo))

    def test_connection_level(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.panda)
        self.assertEqual(self.network.connection_level(self.ivo, self.panda), 0)

    def test_are_connected(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.panda)
        self.assertFalse(self.network.are_connected(self.ivo, self.panda))

    def test_how_many_genders_in_network(self):
        self.network.make_friends(self.ivo, self.panda)
        self.network.make_friends(self.ivo, self.other_panda)
        self.assertEqual(self.network.how_many_genders_in_network(1, self.ivo, "male"), 1)

if __name__ == '__main__':
    unittest.main()
