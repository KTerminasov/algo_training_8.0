import unittest
from io import StringIO
import sys

from first import main


class TestFirst(unittest.TestCase):
    """Тестирование задачи А. Дележ грибов"""

    def simulate_input(self, input_data):
        """Вспомогательная функция для симуляции ввода"""
        sys.stdin = StringIO(input_data)
        return main()

    def test_case_1(self):
        """1 тест из условия."""
        input_data = "2\n1 2"
        result = self.simulate_input(input_data)
        self.assertEqual(result, 1)

    def test_case_2(self):
        """2 тест из условия."""
        input_data = "3\n 2 2 2"
        result = self.simulate_input(input_data)
        self.assertEqual(result, 2)
    
    def test_case_3(self):
        """3 тест из условия."""
        input_data = "11\n4 10 7 5 4 5 3 8 3 2 5"
        result = self.simulate_input(input_data)
        self.assertEqual(result, 10)
