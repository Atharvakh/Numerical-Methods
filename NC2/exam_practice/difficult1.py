import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, diff
from sympy import sympify

class ODE:
    def __init__(self, x0, y0, h, xn, f_str):
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.xn = xn
        self.f_str = f_str

    
    def df(self,x, y):
        return eval(self.f_str, {"x": x, "y": y, **np.__dict__})
    
    
    # --- Euler’s Method ---
    def Euler(self):
        x_vals = np.arange(self.x0, self.xn + self.h, self.h)
        y_vals = [self.y0]
        n = int((self.xn - self.x0) / self.h)

        x = self.x0
        y = self.y0

        for i in range(n):
            y_next = y + self.h * self.df(x, y)
            y_vals.append(y_next)
            x += self.h
            y = y_next

        return x_vals, y_vals
    
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
    print("Please enter equation in dy/dx form ")
    f_str = input("dy/dx = ")
    x0 = float(input("Enter initial x value (x0): "))
    y0 = float(input("Enter initial y value (y0): "))
    h = float(input("Enter step size (h): "))
    xn = float(input("Enter final x value (xn): "))
    ode = ODE(x0, y0, h, xn, f_str)
    x_euler, y_euler = ode.Euler()
    print(x_euler)
    print(y_euler)
    lag = Lagrange(x_euler,y_euler)
    poly = lag.build_polynomial()
    print("\nLagrange Interpolating Polynomial:")
    poly = sympify(poly)
    print(poly)
    numdiff = Numerical_Diff(str(poly))
    print(numdiff)
    print("\nNumerical Derivative Expression:")
    diffval = numdiff.evaluate(0.4)
    print(diffval)



if __name__ == "__main__":
    main()