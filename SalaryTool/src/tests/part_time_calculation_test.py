import unittest
from calculations.part_time_calculation import PartTimeCalculator

class TestPartTimeCalculator(unittest.TestCase):

    def setUp(self):
        self.monthly_salary = 1000
        self.key = 80


    def test_calculate_part_time_salary(self):
        self.assertEqual(PartTimeCalculator.calculate_part_time_salary(self,self.key),800)


    def test_class_init_value(self):
        o = PartTimeCalculator(self.monthly_salary).__init__(333)
        self.assertEqual(PartTimeCalculator(self.monthly_salary).__init__(333),o)
        