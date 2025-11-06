import numpy as np
from sympy import symbols, sympify

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









