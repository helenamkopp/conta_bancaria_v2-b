import unittest
from main import Employee, Manager, Director, BonusControl, Client


class TestAbstract(unittest.TestCase):

    def setUp(self):
        self.manager_1 = Manager("Gabriela", "888.457.000-99", 6000.0, 4525, 4)
        self.manager_2 = Manager("Mariele", "147.354.025-55", 7000.0, 3654, 5)
        self.director_1 = Director("Marcia", "555.471.333-14", 4000.0)
        self.director_2 = Director("Vinicius", "333.014.982-00", 3000.0)

    def tearDown(self):
        pass

    def test_get_bonus(self):
        self.assertEqual(self.manager_1.get_bonus(), 1200)
        self.assertEqual(self.manager_2.get_bonus(), 1400)
        self.assertEqual(self.director_1.get_bonus(), 600)
        self.assertEqual(self.director_2.get_bonus(), 450)


if __name__ == "__main__":
    unittest.main()
