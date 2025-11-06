import numpy as np
import math
#from interpolation import *
class Lagrange:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    def build_polynomial(self):
        terms = []
        n = len(self.x)
        for i in range(n):
            term = f"{self.y[i]:.6f}"
            for j in range(n):
                if j != i:
                    term += f" * (x - {self.x[j]}) / ({self.x[i]} - {self.x[j]})"
            terms.append(term)
        return " + ".join(terms).replace("+ -", "- ")


    def evaluate(self, x_val):
        n = len(self.x)
        result = 0
        for i in range(n):
            term = self.y[i]
            for j in range(n):
                if j != i:
                    term *= (x_val - self.x[j]) / (self.x[i] - self.x[j])
            result += term
        return result

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

def main():
    x_data, y_data = [], []

    try:
        with open('data.txt', 'r') as f:
            for line in f:
                x, y = map(float, line.split())
                x_data.append(x)
                y_data.append(y)
    except FileNotFoundError:
        print("Error: table.txt not found.")
        return

    x = np.array(x_data)
    y = np.array(y_data)
    print("x_data:", x)
    print("y_data:", y)

    try:
        x_val = float(input("\nEnter value of x to interpolate: "))
    except ValueError:
        print("Invalid input.")
        return
    
    lagrange = Lagrange(x, y)

    poly = lagrange.build_polynomial()  
    print("\nLagrange Interpolating Polynomial:")
    print("P(x) =", poly)
    interpolated_value = lagrange.evaluate(x_val)
    print(f"Interpolated value at x={x_val}: {interpolated_value:.6f}")

    numerical_diff = Numerical_Diff(poly)
    derivative_value = numerical_diff.evaluate(x_val)
    print(f"Derivative at x={x_val}: {derivative_value:.6f}")
    
if __name__ == "__main__":
    main()