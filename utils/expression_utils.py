from enums.operation import Operation
import re


def has_special_characters(string):
    pattern = re.compile("[!@#$%^&*,.?\":{}|<>]")
    return pattern.search(string) is not None


def is_parentheses_balanced(expr):
    stack = []

    for x in expr:
        if x == "(":
            stack.append(x)
        elif x == ")" and len(stack) != 0:
            stack.pop()
        elif len(stack) == 0 and x == ")":
            return False

    return len(stack) == 0


def is_digit_positive(expr):
    return "-" not in expr


def is_operation_supported(expr):
    replace_list = [("(", ""), (")", "")]
    for char, empty in replace_list:
        expr = expr.replace(char, empty)

    for x in expr.split(" "):
        if not x.isdigit() and x != Operation.Add.value and x != Operation.Multiply.value:
            return False

    return True


def is_expression_valid(expr):
    if not is_parentheses_balanced(expr):
        raise Exception("Please verify that the parentheses are balanced")
        return False

    if not is_digit_positive(expr):
        raise Exception("Please verify that all digits are positive")
        return False

    if has_special_characters(expr):
        raise Exception("Please verify there is no special characters in the expressions")
        return False

    if not is_operation_supported(expr):
        raise Exception("Please verify that the provided operation is supported")
        return False

    return True


def get_args(expr):
    func = ""
    expressions = []

    if has_parentheses(expr):
        expr = trim_outer_parentheses(expr)

    if has_parentheses(expr):
        complex_expression = extract_expression(expr)
        expressions.append(complex_expression)
        complex_expression_index = expr.index(complex_expression)
        remaining_args = expr[0:complex_expression_index].strip() + expr[complex_expression_index + len(
            complex_expression):len(expr)]
    else:
        remaining_args = expr

    for x in remaining_args.split(" "):
        if x == Operation.Add.value or x == Operation.Multiply.value:
            func = x
        else:
            expressions.append(x)

    return func, expressions


def extract_expression(expr):
    stack = []
    if "(" not in expr:
        return expr

    start = expr.index("(")

    for x in range(start, len(expr)):
        if expr[x] == "(":
            stack.append("(")
        elif expr[x] == ")" and stack[-1] == "(":
            stack.pop()

        if len(stack) == 0:
            return expr[start:x + 1]


def trim_outer_parentheses(expr):
    start = expr.index("(")
    end = expr.rindex(")")
    return expr[start + 1:end]


def is_all_digit(expr):
    for x in expr:
        if not x.isdigit():
            return False
    return True


def has_parentheses(expr):
    return "(" in expr and ")" in expr;
