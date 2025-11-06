from interpolation import *
class Lagrange(Interpolator):
    def __init__(self, x, y):
        super().__init__(x, y)

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
    
