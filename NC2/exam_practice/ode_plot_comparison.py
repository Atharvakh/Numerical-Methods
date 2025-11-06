import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

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
    
def main():
    print(f"Please Enter euquation dy/dx = f(x,y) in terms of x and y")
    f_str = input("Enter dy/dx = (use x and y): ")   # e.g. y - x**2 + 1
    x0 = float(input("Enter initial x0: "))
    y0 = float(input("Enter initial y0: "))
    xn = float(input("Enter final x value xn: "))
    h = float(input("Enter step size h: "))

    ode = ODE(x0, y0, h, xn, f_str)
    x_euler, y_euler = ode.Euler()
    x_true, y_true = ode.analytical_solution()
    print("\nAnalytical Solution:")
    for i in range(len(x_true)):
        print(f"x = {x_true[i]:.4f}, y = {y_true[i]:.6f}")
    print("\n--- Euler's Method ---")
    x_euler, y_euler = ode.Euler()
    for i in range(len(x_euler)):
        print(f"x = {x_euler[i]:.4f}, y = {y_euler[i]:.6f}")
    
    print("Error between Analytical and Euler's Method:")
    error_y = []
    for i in range(len(x_euler)):
        error = abs(y_euler[i] - np.interp(x_euler[i], x_true, y_true))
        error_y.append(error)
        print(f"x = {x_euler[i]:.4f}, |error| = {error:.6e}")

    plt.figure(figsize=(8, 6))
    plt.plot(x_euler, error_y, 'o--',ms=2, lw=0.5, alpha=0.8, label='Error (Euler vs Analytical) at each step')
    plt.title(f"Error between Euler's Method and Analytical Solution (h = {h})", fontsize=13, fontweight='bold')
    plt.xlabel("x")
    plt.ylabel("Absolute Error |y_euler - y_true|")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


    


if __name__ == "__main__":
    main()