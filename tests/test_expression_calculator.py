import unittest

from calculator.expression_calculator import ExpressionCalculator


class TestExpressionCalculator(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_addition_of_digits(self):
        result = self.expression_calculator.addition(["1", "2", "3"])
        self.assertEqual(result, 6)

    def test_addition_of_expression(self):
        result = self.expression_calculator.addition(["1", "2", "(add 3 3)"])
        self.assertEqual(result, 9)

    def test_addition_of_mixed_expression(self):
        result = self.expression_calculator.addition(["1", "2", "(add 2 3)", "(multiply 2 3)"])
        self.assertEqual(result, 14)

    def test_multiplication_of_digits(self):
        result = self.expression_calculator.multiply(["1", "2", "3"])
        self.assertEqual(result, 6)

    def test_multiplication_of_expression(self):
        result = self.expression_calculator.multiply(["1", "2", "(multiply 3 3)"])
        self.assertEqual(result, 18)

    def test_multiplication_of_mixed_expression(self):
        result = self.expression_calculator.multiply(["1", "2", "(add 2 3)", "(multiply 2 3)"])
        self.assertEqual(result, 60)

    def test_calculation_of_addition(self):
        result = self.expression_calculator.calculate("(add 3 (add (add 3 3) 3))")
        self.assertEqual(result, 12)

    def test_calculation_of_multiply(self):
        result = self.expression_calculator.calculate("(multiply 3 (multiply (multiply 3 3) 3))")
        self.assertEqual(result, 81)

    def test_calculation_of_mixed_operation(self):
        result = self.expression_calculator.calculate("(multiply 2 (add (multiply 2 3) 8))")
        self.assertEqual(result, 28)
