import numpy as np
from scipy.integrate import solve_ivp

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

    def Mod_Euler(self):
        x_vals = np.arange(self.x0, self.xn + self.h, self.h)
        y_vals = [self.y0]
        n = int((self.xn - self.x0) / self.h)

        x = self.x0
        y = self.y0

        for i in range(n):
            y_p = y + self.h * self.df(x, y)
            y_c = y + (self.h / 2) * (self.df(x, y) + self.df(x + self.h, y_p))
            y_vals.append(y_c)
            x += self.h
            y = y_c

        return x_vals, y_vals

    def RK(self):
        x_vals = np.arange(self.x0, self.xn + self.h, self.h)
        y_vals = [self.y0]
        n = int((self.xn - self.x0) / self.h)

        x = self.x0
        y = self.y0

        for i in range(n):
            k1 = self.h * self.df(x, y)
            k2 = self.h * self.df(x + self.h / 2, y + k1 / 2)
            k3 = self.h * self.df(x + self.h / 2, y + k2 / 2)
            k4 = self.h * self.df(x + self.h, y + k3)

            y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y_vals.append(y_next)
            x += self.h
            y = y_next

        return x_vals, y_vals
    
    def analytical_solution(self):
        solution = solve_ivp(self.df, [self.x0, self.xn], [self.y0], t_eval=np.arange(self.x0, self.xn + self.h, self.h))
        return solution.t, solution.y[0]