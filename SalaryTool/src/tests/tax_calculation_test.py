import unittest
from calculations.tax_calculation import TaxCalculator


class TestTaxCalculation(unittest.TestCase):

    def setUp(self):
        self.number = 1                           # default validation test value

        self.mo_salary = int(1000)
        self.monthly_salary = int(1000)
        self.tax = float(20)
        self.tax_percentage = float(20)
        self.tcalculate = TaxCalculator(self)

    # to validate that something is working
    def test_validation(self):
        x = int(self.number)
        self.assertEqual(int(self.number), 1 * x)

    def test_tax_calculation(self):               # income - tax
        income_after_tax = TaxCalculator.calculate_income_after_tax(self)
        self.assertEqual(income_after_tax, 800)

    # no tax deducted with 0 tax percentage
    def test_tax_calculation_with_0_tax(self):
        self.tax = float(0)
        income_after_tax = TaxCalculator.calculate_income_after_tax(self)
        self.assertEqual(income_after_tax, 1000)
