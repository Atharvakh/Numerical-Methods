import numpy as np
from sympy import symbols, sympify
class Lagrange:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
    
class Numerical_Integration:
    def __init__(self,a,b,n,equation):
        self.x = symbols('x')
        self.a = a
        self.b = b
        self.n = n
        self.y = equation
    
    def Trapezoidal(self):
        h = (self.b-self.a)/self.n
        integral = (self.y.subs(self.x,self.a) + self.y.subs(self.x,self.b))/2
        for i in range(1,self.n):
            integral += self.y.subs(self.x,self.a + i*h)
        integral *= h
        return integral
    
    def Simpson13(self):
        h = (self.b-self.a)/self.n
        integral = self.y.subs(self.x,self.a) + self.y.subs(self.x,self.b)
        for i in range(1,self.n,2):
            integral += 4*self.y.subs(self.x,self.a + i*h)
        for i in range(2,self.n-1,2):
            integral += 2*self.y.subs(self.x,self.a + i*h)
        integral *= h/3
        return integral
    
    def Simpson38(self):
        h = (self.b-self.a)/self.n
        integral = self.y.subs(self.x,self.a) + self.y.subs(self.x,self.b)
        for i in range(1,self.n,3):
            integral += 3*self.y.subs(self.x,self.a + i*h)
        for i in range(2,self.n,3):
            integral += 3*self.y.subs(self.x,self.a + i*h)
        for i in range(3,self.n-2,3):
            integral += 2*self.y.subs(self.x,self.a + i*h)
        integral *= 3*h/8
        return integral
    

def main():
    try:
        with open('data.txt', 'r') as f:
            x_data, y_data = zip(*(map(float, line.split()) for line in f))
    except FileNotFoundError:
        print("Error: table.txt not found.")
        return
    
    laginterp = Lagrange(x_data, y_data)
    poly_str = laginterp.build_polynomial()
   # print("\nLagrange Polynomial:", poly_str)
    a = float(input("Enter lower limit for integration: "))
    b = float(input("Enter upper limit for integration: "))
    n = int(input("Enter number of intervals: "))
    eqn = sympify(poly_str)
    print(f"equation is {eqn}")
    num_integ = Numerical_Integration(a, b, n, eqn)
    print("\nNumerical Integration Results:")
    print(f"Trapezoidal Rule: {num_integ.Trapezoidal():.6f}")
    if n % 2 == 0:
        print(f"Simpson's 1/3 Rule: {num_integ.Simpson13():.6f}")
    else:
        print("Simpson's 1/3 Rule requires an even number of subintervals.")
    if n % 3 == 0:
        print(f"Simpson's 3/8 Rule: {num_integ.Simpson38():.6f}")
    else:
        print("Simpson's 3/8 Rule requires the number of subintervals to be a multiple of 3.")
if __name__ == "__main__":
    main()