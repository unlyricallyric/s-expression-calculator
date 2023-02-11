import sys

from calculator.expression_calculator import ExpressionCalculator

if __name__ == "__main__":
    args = sys.argv

    try:
        expressionCalculator = ExpressionCalculator()
        result = expressionCalculator.calculate(args[1])
        print(result)

    except Exception as e:
        print(e)

