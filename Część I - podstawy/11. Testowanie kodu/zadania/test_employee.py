import unittest
from z_11_3 import Employee


class TestEmployee(unittest.TestCase):
    """Test klasy Employee"""

    def setUp(self):
        first = 'janusz'
        last = 'nosacz'
        salary = 20000
        self.employee = Employee(first, last, salary)

    def test_give_default_raise(self):
        """Sprawdzenie przydzielania domyślnej podwyżki"""
        self.employee.give_raise()
        self.assertEqual(25000, self.employee.salary)

    def test_give_custom_raise(self):
        """Sprawdzanie przydzielania większej podwyżki"""
        self.employee.give_raise(10000)
        self.assertEqual(30000, self.employee.salary)


unittest.main()
