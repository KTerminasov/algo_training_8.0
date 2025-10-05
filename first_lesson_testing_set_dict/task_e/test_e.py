import unittest
from io import StringIO
import sys

from e import main 


class TestE(unittest.TestCase):
    def simulate_input(self, input_data):
        """Вспомогательная функция для симуляции ввода"""
        sys.stdin = StringIO(input_data)
        return main()

    def test_case_1(self):
        input_data = '1 10'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 44)

    def test_case_2(self):
        input_data = '5 1'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 10)
    
    def test_case_3(self):
        "5 → 10 → 10 → 10 = 10"
        input_data = '5 3'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 10)
    
    def test_case_4(self):
        ""
        input_data = '0 0'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 0)
    
    def test_case_5(self):
        "0 → 0 → ... → 0 = 0"
        input_data = '0 10'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 0)
    
    def test_case_6(self):
        "2→4→8→16→22→24→28→36→42→44→48 = 48"
        input_data = '2 10'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 48)
    
    def test_case_7(self):
        "123456789 + 9 = 123456798"
        input_data = '123456789 1'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 123456798)

    def test_case_8(self):
        "999999999 + 9 = 1 000 000 008"
        input_data = '999999999 1'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 1000000008)
    
    def test_case_9(self):
        "Большие числа"
        input_data = '51 926907757'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 4634538832)
    
    def test_case_10(self):
        "Проверка на 5"
        input_data = '12345 123'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 12350)

    def test_case_11(self):
        "Падал"
        input_data = '23 871471600'
        result = self.simulate_input(input_data)
        self.assertEqual(result, 4357358028)
  

