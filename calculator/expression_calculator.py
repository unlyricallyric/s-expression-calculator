from calculator.calculator import Calculator
from enums.operation import Operation
from utils.expression_utils import get_args, is_expression_valid


class ExpressionCalculator(Calculator):
    def addition(self, expr):
        result = 0
        for expression in expr:
            if expression.isdigit():
                result += int(expression)
            else:
                result += self.calculate(expression)
        return result

    def multiply(self, expr):
        result = 1
        for expression in expr:
            if expression.isdigit():
                result *= int(expression)
            else:
                result *= self.calculate(expression)
        return result

    def calculate(self, expr):
        if is_expression_valid(expr) is True:
            [func, expressions] = get_args(expr)

            if func == Operation.Add.value:
                return self.addition(expressions)
            elif func == Operation.Multiply.value:
                return self.multiply(expressions)
