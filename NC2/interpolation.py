import numpy as np
import math

class Interpolator:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    def build_polynomial(self):
        raise NotImplementedError

    def evaluate(self, x_val):
        raise NotImplementedError

class DividedDifference(Interpolator):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.coeffs = self.divided_diff()

    def divided_diff(self):
        n = len(self.y)
        table = np.zeros((n, n))
        table[:, 0] = self.y
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (self.x[i + j] - self.x[i])
        print("\nDivided Difference Table:\n", table)
        return table[0, :]

    def build_polynomial(self):
        terms = [f"{self.coeffs[0]:.6f}"]
        for i in range(1, len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue
            term = f"{self.coeffs[i]:+.6f}"
            for j in range(i):
                term += f" * (x - {self.x[j]})"
            terms.append(term)
        return " + ".join(terms).replace("+ -", "- ")

    def evaluate(self, x_val):
        result = self.coeffs[0]
        for i in range(1, len(self.coeffs)):
            term = self.coeffs[i]
            for j in range(i):
                term *= (x_val - self.x[j])
            result += term
        return result
    


class ForwardDifference(Interpolator):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.h = self.x[1] - self.x[0]
        self.table = self.forward_diff()

    def forward_diff(self):
        n = len(self.y)
        table = np.zeros((n, n))
        table[:, 0] = self.y
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = table[i + 1, j - 1] - table[i, j - 1]
        print("\nForward Difference Table:\n", table)
        return table

    def build_polynomial(self):
        coeffs = self.table[0, :]
        terms = [f"{coeffs[0]:.6f}"]
        for i in range(1, len(coeffs)):
            if coeffs[i] == 0:
                continue
            term = f"{coeffs[i]:+.6f} / {math.factorial(i)}"
            for j in range(i):
                term += f" * (u - {j})"
            terms.append(term)
        return " + ".join(terms).replace("+ -", "- ")

    def evaluate(self, x_val):
        u = (x_val - self.x[0]) / self.h
        coeffs = self.table[0, :]
        result = coeffs[0]
        u_term = 1
        for i in range(1, len(coeffs)):
            u_term *= (u - (i - 1))
            result += (u_term / math.factorial(i)) * coeffs[i]
        return result

class BackwardDifference(Interpolator):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.reversed_x = self.x[::-1]
        self.reversed_y = self.y[::-1]
        self.h = self.reversed_x[1] - self.reversed_x[0]
        self.table = self.backward_diff()

    def backward_diff(self):
        n = len(self.reversed_y)
        table = np.zeros((n, n))
        table[:, 0] = self.reversed_y
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = table[i + 1, j - 1] - table[i, j - 1]
        print("\nBackward Difference Table:\n", table)
        return table

    def build_polynomial(self):
        coeffs = self.table[0, :]
        terms = [f"{coeffs[0]:.6f}"]
        for i in range(1, len(coeffs)):
            if coeffs[i] == 0:
                continue
            term = f"{coeffs[i]:+.6f} / {math.factorial(i)}"
            for j in range(i):
                term += f" * (u + {j})"
            terms.append(term)
        return " + ".join(terms).replace("+ -", "- ")

    def evaluate(self, x_val):
        u = (x_val - self.reversed_x[0]) / self.h
        coeffs = self.table[0, :]
        result = coeffs[0]
        u_term = 1
        for i in range(1, len(coeffs)):
            u_term *= (u + (i - 1))
            result += (u_term / math.factorial(i)) * coeffs[i]
        return result
    
class StirlingInterpolation(Interpolator):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.h = self.x[1] - self.x[0]
        self.table = self.forward_diff()
        self.mid_index = (len(self.x) - 1) // 2
        self.mid_x = self.x[self.mid_index]

    def forward_diff(self):
        n = len(self.y)
        table = np.zeros((n, n))
        table[:, 0] = self.y
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = table[i + 1, j - 1] - table[i, j - 1]
        print("\nStirling Forward Difference Table:\n", table)
        return table

    def build_polynomial(self):
        poly_str = f"{self.table[self.mid_index, 0]:.6f}"
        for j in range(1, len(self.x)):
            if j % 2 == 1:
                coeff = (self.table[self.mid_index - (j - 1)//2 - 1, j] +
                         self.table[self.mid_index - (j - 1)//2, j]) / 2.0
            else:
                coeff = self.table[self.mid_index - j//2, j]
            if coeff == 0:
                continue
            term = f"{coeff:+.6f} / {math.factorial(j)}"
            for k in range(j):
                term += f" * (u - {k})"
            poly_str += " + " + term
        return poly_str.replace("+ -", "- ")

    def evaluate(self, x_val):
        u = (x_val - self.mid_x) / self.h
        result = self.table[self.mid_index, 0]
        u_term = 1
        for j in range(1, len(self.x)):
            if j % 2 == 1:
                coeff = (self.table[self.mid_index - (j - 1)//2 - 1, j] +
                         self.table[self.mid_index - (j - 1)//2, j]) / 2.0
            else:
                coeff = self.table[self.mid_index - j//2, j]
            u_term *= (u - (j - 1)/2)
            result += (u_term / math.factorial(j)) * coeff
        return result

class Interpolation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = x[1] - x[0] if len(x) > 1 else None
        self.equally_spaced = np.allclose(np.diff(x), self.h)

    def interpolate(self, x_val):
        if not self.equally_spaced:
            print("\nUsing Divided Differences")
            interp = DividedDifference(self.x, self.y)

        else:
            n = len(self.x)
            mid_index = (n - 1) // 2
            mid_x = self.x[mid_index]
            start_x = self.x[0]
            end_x = self.x[-1]

            # Heuristic thresholds
            range_x = end_x - start_x
            near_start = (x_val - start_x) < 0.25 * range_x
            near_end = (end_x - x_val) < 0.25 * range_x
            near_middle = abs(x_val - mid_x) < 0.2 * range_x


            if len(self.x) % 2 == 1 and near_middle:
                print("\nUsing Stirling’s Central Difference")
                interp = StirlingInterpolation(self.x, self.y)
            elif near_start:
                print("\nUsing Forward Difference")
                interp = ForwardDifference(self.x, self.y)
            else:
                print("\nUsing Backward Difference")
                interp = BackwardDifference(self.x, self.y)

        print("Polynomial:", interp.build_polynomial())
        print(f"Interpolated value at x={x_val}: {interp.evaluate(x_val):.6f}")

