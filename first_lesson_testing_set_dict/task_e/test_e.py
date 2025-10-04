import unittest
from io import StringIO
import sys

from e import main 


class TestE(unittest.TestCase):
    def simulate_input(self, input_data):
        """Вспомогательная функция для симуляции ввода"""
        sys.stdin = StringIO(input_data)
        return main()