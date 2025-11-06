###from interpolation import *
# from Lagrange import *
# from numerical_diff import *
# from numerical_integration import *
from ODE import ODE
#from power_method import power_method
import matplotlib.pyplot as plt
import numpy as np



def main():
#     try:
#         with open('table.txt', 'r') as f:
#             x_data, y_data = zip(*(map(float, line.split()) for line in f))
#     except FileNotFoundError:
#         print("Error: table.txt not found.")
#         return

#     try:
#         x_val = float(input("Enter value of x to interpolate: "))
#     except ValueError:
#         print("Invalid input.")
#         return

   
#    # inter = Interpolation(np.array(x_data), np.array(y_data))
#    # inter.interpolate(x_val)

#     laginterp = Lagrange(x_data, y_data)
    
#     poly_str = laginterp.build_polynomial()

    # print("\nLagrange Polynomial:", poly_str)
    # print(f"Lagrange Interpolated value at x={x_val}: {laginterp.evaluate(x_val):.6f}")

    # x_diff = float(input("Enter value for differentiation: "))
    # print("\nNumerical Derivative at x =", x_diff)
    # derivative_calculated = Numerical_Diff(poly_str)
    
    # print("\nThe derivative of the polynomial is:")
    # print(derivative_calculated.derivative_expr)
    
    # estimated_derivative =  derivative_calculated.evaluate(x_val)
    # print(f"\nEstimated derivative: {estimated_derivative:.6f}")


    ###For Numerical Integration
    # a = float(input("Enter lower limit for integration: "))
    # b = float(input("Enter upper limit for integration: "))

    # n = int(input("Enter number of intervals: "))
    # eqn = sympify(poly_str)

    # num_integ = Numerical_Integration(a, b, n, eqn)
    # print("\nNumerical Integration Results:")
    # print(f"Trapezoidal Rule: {num_integ.Trapezoidal():.6f}")
    # if n % 2 == 0:
    #     print(f"Simpson's 1/3 Rule: {num_integ.Simpson13():.6f}")
    # else:
    #     print("Simpson's 1/3 Rule requires an even number of subintervals.")
    # if n % 3 == 0:
    #     print(f"Simpson's 3/8 Rule: {num_integ.Simpson38():.6f}")
    # else:
    #     print("Simpson's 3/8 Rule requires the number of subintervals to be a multiple of 3.")

    f_str = input("Enter dy/dx = (use x and y): ")   # e.g. y - x**2 + 1
    x0 = float(input("Enter initial x0: "))
    y0 = float(input("Enter initial y0: "))
    xn = float(input("Enter final x value xn: "))
    h = float(input("Enter step size h: "))

    ode = ODE(x0, y0, h, xn, f_str)

    # Numerical and analytical solutions
    x_euler, y_euler = ode.Euler()
    x_true, y_true = ode.analytical_solution()

    # Interpolate analytical y-values at Euler x-points
    y_true_interp = np.interp(x_euler, x_true, y_true)

    # Compute error at each iteration
    errors = np.abs(np.array(y_euler) - np.array(y_true_interp))

    # --- Print iteration details ---
    print("\nIteration-wise Error (Euler's Method):")
    print(" x\t\t y_numerical\t y_true\t\t |error|")
    print("-" * 50)
    for i in range(len(x_euler)):
        print(f"{x_euler[i]:.4f}\t {y_euler[i]:.6f}\t {y_true_interp[i]:.6f}\t {errors[i]:.6e}")

    # --- Plot error vs x ---
    plt.figure(figsize=(8, 5))
    plt.plot(x_euler, errors, 'o--', color='crimson', lw=2, ms=5)
    plt.title(f"Euler Method Error per Iteration (h = {h})", fontsize=13, fontweight='bold')
    plt.xlabel("x")
    plt.ylabel("Absolute Error |y_num - y_true|")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    # print("\nAnalytical Solution:")
    # x_analytical, y_analytical = ode.analytical_solution()
    # for i in range(len(x_analytical)):
    #     print(f"x = {x_analytical[i]:.4f}, y = {y_analytical[i]:.6f}")

    # print("\n--- Euler's Method ---")
    # x_euler, y_euler = ode.Euler()
    # for i in range(len(x_euler)):
    #     print(f"x = {x_euler[i]:.4f}, y = {y_euler[i]:.6f}")

    # print("\n--- Modified Euler's Method ---")
    # x_vals, y_vals = ode.Mod_Euler()
    # for i in range(len(x_vals)):
    #     print(f"x = {x_vals[i]:.4f}, y = {y_vals[i]:.6f}")

    # print("\n--- Runge-Kutta Method ---")
    # x_rk, y_rk = ode.RK()
    # for i in range(len(x_rk)):
    #     print(f"x = {x_rk[i]:.4f}, y = {y_rk[i]:.6f}")
    

    # plt.figure(figsize=(8, 6))
    # plt.plot(x_euler, y_euler, 'o--',ms=2, lw=0.5, alpha=0.8, label='Euler')
    # plt.plot(x_vals, y_vals, 's--',ms=2, lw=0.5, alpha=0.8, label='Modified Euler')
    # plt.plot(x_rk, y_rk, 'd--', ms=2, lw=0.5, alpha=0.8,label='Runge-Kutta (RK4)')
    # plt.plot(x_analytical, y_analytical, 'k-',ms=2, lw=0.5, alpha=0.8, label='Analytical Solution')
    # plt.title("Numerical Solutions of ODE")
    
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Analytical, Euler, Modified Euler, and Runge-Kutta Methods')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    # try:
    #     A = np.loadtxt('matrix.txt')
    #     x0 = np.loadtxt('intvec.txt')
    # except FileNotFoundError as e:
    #     print(f"Error: {e.filename} not found.")
    #     return
    
    # eigen = power_method(A, x0, tol=1e-6, max_iter=1000)
    # eigenvalue, eigenvector = eigen.power_fun()
    # print("\nPower Method Results:")
    # print(f"Dominant Eigenvalue: {eigenvalue:.6f}")
    # print(f"Corresponding Eigenvector: {eigenvector}")




if __name__ == "__main__":
    main()