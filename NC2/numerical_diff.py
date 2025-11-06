from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, diff

class Numerical_Diff:
    def __init__(self, poly_str):
        self.poly_str = poly_str
        self.x = symbols('x')
        self.poly_expr = parse_expr(self.poly_str)
        self.derivative_expr = diff(self.poly_expr, self.x)

    def evaluate(self, x_val):
        """
        Evaluates the derivative at a specific point.
        """
        return self.derivative_expr.subs(self.x, x_val) #substitutes x with x_val and finds the value
    