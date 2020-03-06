import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'name_function.py'."""

    def test_first_last_name(self):
        """Czy dane w postaci 'Janusz Nosacz' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name('janusz', 'nosacz')
        self.assertEqual(formatted_name, 'Janusz Nosacz')

    def test_first_middle_last_name(self):
        """Czy dane w postaci 'Pjoter Sebastian Nosacz' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name(
            'pjoter', 'nosacz', 'sebastian'
        )
        self.assertEqual(formatted_name, 'Pjoter Sebastian Nosacz')


unittest.main()
