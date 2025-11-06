# # import numpy as np
# # import matplotlib.pyplot as plt
# # from ODE import ODE
# # import sympy as sp

# # class ODEErrorAnalysis:
# #     def __init__(self, x0, y0, xn, f_str, analytical_solution=None):
# #         self.x0 = x0
# #         self.y0 = y0
# #         self.xn = xn
# #         self.f_str = f_str
# #         self.analytical_solution = analytical_solution
    
# #     def get_analytical_solution(self, x_vals):
# #         """Get analytical solution values at given x points"""
# #         if self.analytical_solution:
# #             x_sym = sp.Symbol('x')
# #             analytical_func = sp.lambdify(x_sym, self.analytical_solution, 'numpy')
# #             return analytical_func(x_vals)
# #         else:
# #             # Use scipy's solve_ivp as reference "true" solution with very small step size
# #             ode_ref = ODE(self.x0, self.y0, 0.001, self.xn, self.f_str)
# #             x_ref, y_ref = ode_ref.analytical_solution()
# #             # Interpolate to get values at requested x points
# #             return np.interp(x_vals, x_ref, y_ref)
    
# #     def calculate_errors(self, step_sizes):
# #         """Calculate errors for different step sizes using all three methods"""
# #         errors_euler = []
# #         errors_modified_euler = []
# #         errors_rk4 = []
        
# #         for h in step_sizes:
# #             # Solve ODE with current step size
# #             ode = ODE(self.x0, self.y0, h, self.xn, self.f_str)
            
# #             # Get numerical solutions
# #             x_euler, y_euler = ode.Euler()
# #             x_mod, y_mod = ode.Mod_Euler()
# #             x_rk, y_rk = ode.RK()
            
# #             # Get analytical solution at the same x points
# #             # Use RK4 points as reference since they're most accurate
# #             y_true = self.get_analytical_solution(x_rk)
            
# #             # Interpolate numerical solutions to common x points (RK4 points)
# #             y_euler_interp = np.interp(x_rk, x_euler, y_euler)
# #             y_mod_interp = np.interp(x_rk, x_mod, y_mod)
            
# #             # Calculate maximum absolute error
# #             error_euler = np.max(np.abs(y_euler_interp - y_true))
# #             error_mod = np.max(np.abs(y_mod_interp - y_true))
# #             error_rk = np.max(np.abs(y_rk - y_true))
            
# #             errors_euler.append(error_euler)
# #             errors_modified_euler.append(error_mod)
# #             errors_rk4.append(error_rk)
            
# #             print(f"Step size: {h:.4f}, Errors - Euler: {error_euler:.6f}, Mod Euler: {error_mod:.6f}, RK4: {error_rk:.6f}")
        
# #         return errors_euler, errors_modified_euler, errors_rk4
    
# #     def plot_step_size_vs_error(self, step_sizes, errors_euler, errors_mod_euler, errors_rk4):
# #         """Plot step size vs error for all three methods"""
# #         plt.figure(figsize=(12, 8))
        
# #         # Plot errors
# #         plt.loglog(step_sizes, errors_euler, 'o-', linewidth=2, markersize=8, 
# #                   label='Euler Method', color='red')
# #         plt.loglog(step_sizes, errors_mod_euler, 's-', linewidth=2, markersize=8, 
# #                   label='Modified Euler', color='blue')
# #         plt.loglog(step_sizes, errors_rk4, '^-', linewidth=2, markersize=8, 
# #                   label='RK4 Method', color='green')
        
# #         # Add reference lines for theoretical convergence rates
# #         x_ref = np.array(step_sizes)
# #         h1_ref = 0.1 * x_ref  # O(h) reference
# #         h2_ref = 0.01 * x_ref**2  # O(h²) reference  
# #         h4_ref = 0.001 * x_ref**4  # O(h⁴) reference
        
# #         plt.loglog(x_ref, h1_ref, '--', color='red', alpha=0.5, label='O(h) reference')
# #         plt.loglog(x_ref, h2_ref, '--', color='blue', alpha=0.5, label='O(h²) reference')
# #         plt.loglog(x_ref, h4_ref, '--', color='green', alpha=0.5, label='O(h⁴) reference')
        
# #         plt.xlabel('Step Size (h)', fontsize=12, fontweight='bold')
# #         plt.ylabel('Maximum Absolute Error', fontsize=12, fontweight='bold')
# #         plt.title('Step Size vs Error for Different ODE Methods', fontsize=14, fontweight='bold')
# #         plt.legend(fontsize=10)
# #         plt.grid(True, which='both', linestyle='--', alpha=0.7)
# #         plt.tight_layout()
        
# #         return plt
    
# #     def plot_convergence_rates(self, step_sizes, errors_euler, errors_mod_euler, errors_rk4):
# #         """Plot to visualize convergence rates"""
# #         plt.figure(figsize=(12, 8))
        
# #         # Calculate convergence rates
# #         rates_euler = []
# #         rates_mod_euler = []
# #         rates_rk4 = []
        
# #         for i in range(1, len(step_sizes)):
# #             rate_euler = np.log(errors_euler[i-1] / errors_euler[i]) / np.log(step_sizes[i-1] / step_sizes[i])
# #             rate_mod = np.log(errors_mod_euler[i-1] / errors_mod_euler[i]) / np.log(step_sizes[i-1] / step_sizes[i])
# #             rate_rk = np.log(errors_rk4[i-1] / errors_rk4[i]) / np.log(step_sizes[i-1] / step_sizes[i])
            
# #             rates_euler.append(rate_euler)
# #             rates_mod_euler.append(rate_mod)
# #             rates_rk4.append(rate_rk)
        
# #         # Plot convergence rates
# #         x_positions = range(len(rates_euler))
# #         width = 0.25
        
# #         plt.bar([x - width for x in x_positions], rates_euler, width, label='Euler', alpha=0.7, color='red')
# #         plt.bar(x_positions, rates_mod_euler, width, label='Modified Euler', alpha=0.7, color='blue')
# #         plt.bar([x + width for x in x_positions], rates_rk4, width, label='RK4', alpha=0.7, color='green')
        
# #         # Add theoretical convergence lines
# #         plt.axhline(y=1, color='red', linestyle='--', alpha=0.5, label='Theoretical Euler (O(h))')
# #         plt.axhline(y=2, color='blue', linestyle='--', alpha=0.5, label='Theoretical Mod Euler (O(h²))')
# #         plt.axhline(y=4, color='green', linestyle='--', alpha=0.5, label='Theoretical RK4 (O(h⁴))')
        
# #         plt.xlabel('Step Size Comparison Index', fontsize=12, fontweight='bold')
# #         plt.ylabel('Experimental Convergence Rate', fontsize=12, fontweight='bold')
# #         plt.title('Experimental Convergence Rates of ODE Methods', fontsize=14, fontweight='bold')
# #         plt.legend(fontsize=10)
# #         plt.grid(True, alpha=0.3)
# #         plt.xticks(x_positions, [f'h{i+1}/h{i+2}' for i in range(len(rates_euler))])
# #         plt.tight_layout()
        
# #         return plt

# # # Example usage and test cases
# # def main():
# #     print("ODE Step Size vs Error Analysis")
# #     print("=" * 50)
    
# #     # Test Case 1: Simple exponential ODE
# #     print("\nTest Case 1: dy/dx = y, y(0) = 1")
# #     print("Analytical solution: y = e^x")
    
# #     # Define analytical solution using sympy
# #     x_sym = sp.Symbol('x')
# #     analytical_sol1 = sp.exp(x_sym)
    
# #     analyzer1 = ODEErrorAnalysis(
# #         x0=0, y0=1, xn=2, 
# #         f_str="y", 
# #         analytical_solution=analytical_sol1
# #     )
    
# #     # Test different step sizes
# #     step_sizes = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    
# #     errors_euler1, errors_mod_euler1, errors_rk41 = analyzer1.calculate_errors(step_sizes)
    
# #     # Plot results
# #     plt1 = analyzer1.plot_step_size_vs_error(step_sizes, errors_euler1, errors_mod_euler1, errors_rk41)
# #     plt1.savefig('ode_error_analysis_exp.png', dpi=300, bbox_inches='tight')
# #     plt1.show()
    
# #     # Plot convergence rates
# #     plt2 = analyzer1.plot_convergence_rates(step_sizes, errors_euler1, errors_mod_euler1, errors_rk41)
# #     plt2.savefig('convergence_rates_exp.png', dpi=300, bbox_inches='tight')
# #     plt2.show()
    
# #     # Test Case 2: More complex ODE
# #     print("\n" + "="*50)
# #     print("Test Case 2: dy/dx = y - x^2 + 1, y(0) = 0.5")
# #     print("Analytical solution: y = (x+1)^2 - 0.5*e^x")
    
# #     analytical_sol2 = (x_sym + 1)**2 - 0.5*sp.exp(x_sym)
    
# #     analyzer2 = ODEErrorAnalysis(
# #         x0=0, y0=0.5, xn=2,
# #         f_str="y - x**2 + 1",
# #         analytical_solution=analytical_sol2
# #     )
    
# #     errors_euler2, errors_mod_euler2, errors_rk42 = analyzer2.calculate_errors(step_sizes)
    
# #     # Plot results for second test case
# #     plt3 = analyzer2.plot_step_size_vs_error(step_sizes, errors_euler2, errors_mod_euler2, errors_rk42)
# #     plt3.savefig('ode_error_analysis_complex.png', dpi=300, bbox_inches='tight')
# #     plt3.show()
    
# #     plt4 = analyzer2.plot_convergence_rates(step_sizes, errors_euler2, errors_mod_euler2, errors_rk42)
# #     plt4.savefig('convergence_rates_complex.png', dpi=300, bbox_inches='tight')
# #     plt4.show()
    
# #     # Print summary table
# #     print("\n" + "="*50)
# #     print("SUMMARY: Final Errors for Smallest Step Size (h=0.01)")
# #     print("="*50)
# #     print(f"{'Method':<15} {'Test 1 Error':<15} {'Test 2 Error':<15}")
# #     print(f"{'-'*15:<15} {'-'*15:<15} {'-'*15:<15}")
# #     print(f"{'Euler':<15} {errors_euler1[-1]:<15.6e} {errors_euler2[-1]:<15.6e}")
# #     print(f"{'Mod Euler':<15} {errors_mod_euler1[-1]:<15.6e} {errors_mod_euler2[-1]:<15.6e}")
# #     print(f"{'RK4':<15} {errors_rk41[-1]:<15.6e} {errors_rk42[-1]:<15.6e}")

# # # Additional function to compare solutions visually
# # def plot_solution_comparison():
# #     """Plot numerical solutions for a specific step size to show accuracy differences"""
# #     # Use a moderate step size to see differences clearly
# #     h = 0.2
# #     ode = ODE(x0=0, y0=1, h=h, xn=2, f_str="y")
    
# #     # Get all solutions
# #     x_euler, y_euler = ode.Euler()
# #     x_mod, y_mod = ode.Mod_Euler()
# #     x_rk, y_rk = ode.RK()
# #     x_true, y_true = ode.analytical_solution()
    
# #     plt.figure(figsize=(12, 8))
    
# #     # Plot solutions
# #     plt.plot(x_euler, y_euler, 'o-', label=f'Euler (h={h})', markersize=4, color='red')
# #     plt.plot(x_mod, y_mod, 's-', label=f'Modified Euler (h={h})', markersize=4, color='blue')
# #     plt.plot(x_rk, y_rk, '^-', label=f'RK4 (h={h})', markersize=4, color='green')
# #     plt.plot(x_true, y_true, 'k-', label='Analytical Solution', linewidth=2)
    
# #     plt.xlabel('x')
# #     plt.ylabel('y')
# #     plt.title(f'Comparison of ODE Methods (dy/dx = y, y(0)=1)')
# #     plt.legend()
# #     plt.grid(True, alpha=0.3)
# #     plt.savefig('ode_methods_comparison.png', dpi=300, bbox_inches='tight')
# #     plt.show()
    
# #     # Print errors at final point
# #     final_error_euler = abs(y_euler[-1] - y_true[-1])
# #     final_error_mod = abs(y_mod[-1] - y_true[-1]) 
# #     final_error_rk = abs(y_rk[-1] - y_true[-1])
    
# #     print(f"\nFinal Point Errors (x={x_true[-1]}):")
# #     print(f"Euler: {final_error_euler:.6f}")
# #     print(f"Modified Euler: {final_error_mod:.6f}")
# #     print(f"RK4: {final_error_rk:.6f}")
# #     print(f"Analytical: {y_true[-1]:.6f}")

# # if __name__ == "__main__":
# #     main()
# #     plot_solution_comparison()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import solve_ivp

# class ODE:
#     def __init__(self, x0, y0, h, xn, f_str):
#         self.x0 = x0
#         self.y0 = y0
#         self.h = h
#         self.xn = xn
#         self.f_str = f_str

#     def df(self, x, y):
#         return eval(self.f_str, {"x": x, "y": y, **np.__dict__})
    
#     def Euler(self):
#         x_vals = np.arange(self.x0, self.xn + self.h, self.h)
#         y_vals = [self.y0]
#         n = int((self.xn - self.x0) / self.h)

#         x = self.x0
#         y = self.y0

#         for i in range(n):
#             y_next = y + self.h * self.df(x, y)
#             y_vals.append(y_next)
#             x += self.h
#             y = y_next

#         return x_vals, y_vals

#     def Mod_Euler(self):
#         x_vals = np.arange(self.x0, self.xn + self.h, self.h)
#         y_vals = [self.y0]
#         n = int((self.xn - self.x0) / self.h)

#         x = self.x0
#         y = self.y0

#         for i in range(n):
#             y_p = y + self.h * self.df(x, y)
#             y_c = y + (self.h / 2) * (self.df(x, y) + self.df(x + self.h, y_p))
#             y_vals.append(y_c)
#             x += self.h
#             y = y_c

#         return x_vals, y_vals

#     def RK(self):
#         x_vals = np.arange(self.x0, self.xn + self.h, self.h)
#         y_vals = [self.y0]
#         n = int((self.xn - self.x0) / self.h)

#         x = self.x0
#         y = self.y0

#         for i in range(n):
#             k1 = self.h * self.df(x, y)
#             k2 = self.h * self.df(x + self.h / 2, y + k1 / 2)
#             k3 = self.h * self.df(x + self.h / 2, y + k2 / 2)
#             k4 = self.h * self.df(x + self.h, y + k3)

#             y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
#             y_vals.append(y_next)
#             x += self.h
#             y = y_next

#         return x_vals, y_vals
    
#     def analytical_solution(self):
#         solution = solve_ivp(self.df, [self.x0, self.xn], [self.y0], 
#                            t_eval=np.arange(self.x0, self.xn + self.h, self.h))
#         return solution.t, solution.y[0]

# def analyze_ode_methods():
#     # Parameters
#     x0 = 0
#     y0 = 1
#     xn = 0.8
#     f_str = "x + y"
    
#     # Different step sizes to test
#     h_values = [0.1, 0.05, 0.025, 0.0125,0.001,0.0001,0.00001]
    
#     # Store errors and results
#     euler_errors = []
#     mod_euler_errors = []
#     rk_errors = []
#     results = {}
    
#     print("ODE Analysis: dy/dx = x + y, y(0) = 1, x in [0, 0.8]")
#     print("="*60)
    
#     for h in h_values:
#         # Create ODE solver instance
#         ode_solver = ODE(x0, y0, h, xn, f_str)
        
#         # Get analytical solution
#         x_analytical, y_analytical = ode_solver.analytical_solution()
        
#         # Get numerical solutions
#         x_euler, y_euler = ode_solver.Euler()
#         x_mod_euler, y_mod_euler = ode_solver.Mod_Euler()
#         x_rk, y_rk = ode_solver.RK()
        
#         # Calculate errors at x = 0.8
#         final_idx = len(x_analytical) - 1
        
#         euler_error = abs(y_euler[final_idx] - y_analytical[final_idx])
#         mod_euler_error = abs(y_mod_euler[final_idx] - y_analytical[final_idx])
#         rk_error = abs(y_rk[final_idx] - y_analytical[final_idx])
        
#         euler_errors.append(euler_error)
#         mod_euler_errors.append(mod_euler_error)
#         rk_errors.append(rk_error)
        
#         # Store results
#         results[h] = {
#             'analytical': (x_analytical, y_analytical),
#             'euler': (x_euler, y_euler),
#             'mod_euler': (x_mod_euler, y_mod_euler),
#             'rk': (x_rk, y_rk)
#         }
        
#         # Print results
#         print(f"\nStep size h = {h}:")
#         print(f"Analytical solution at x = {xn}: {y_analytical[final_idx]:.8f}")
#         print(f"Euler method: {y_euler[final_idx]:.8f}, Error: {euler_error:.8f}")
#         print(f"Modified Euler: {y_mod_euler[final_idx]:.8f}, Error: {mod_euler_error:.8f}")
#         print(f"Runge-Kutta: {y_rk[final_idx]:.8f}, Error: {rk_error:.8f}")
    
#     return h_values, euler_errors, mod_euler_errors, rk_errors, results

# def plot_linear_comparisons(h_values, euler_errors, mod_euler_errors, rk_errors, results):
#     # Create a comprehensive figure with multiple subplots
#     fig = plt.figure(figsize=(16, 12))
    
#     # Plot 1: Error vs Step Size (Linear scale)
#     ax1 = plt.subplot(2, 2, 1)
#     ax1.plot(h_values, euler_errors, 'ro-', linewidth=3, markersize=10, label='Euler Method', markerfacecolor='red')
#     ax1.plot(h_values, mod_euler_errors, 'go-', linewidth=3, markersize=10, label='Modified Euler', markerfacecolor='green')
#     ax1.plot(h_values, rk_errors, 'bo-', linewidth=3, markersize=10, label='Runge-Kutta', markerfacecolor='blue')
    
#     ax1.set_xlabel('Step Size (h)', fontsize=12, fontweight='bold')
#     ax1.set_ylabel('Absolute Error at x = 0.8', fontsize=12, fontweight='bold')
#     ax1.set_title('Error vs Step Size (Linear Scale)', fontsize=14, fontweight='bold')
#     ax1.legend(fontsize=11)
#     ax1.grid(True, alpha=0.3)
#     ax1.set_xticks(h_values)
    
#     # Add error values as text annotations
#     for i, h in enumerate(h_values):
#         ax1.text(h, euler_errors[i] + 0.0001, f'{euler_errors[i]:.6f}', 
#                 ha='center', va='bottom', fontsize=9, color='red')
#         ax1.text(h, mod_euler_errors[i] + 0.0001, f'{mod_euler_errors[i]:.6f}', 
#                 ha='center', va='bottom', fontsize=9, color='green')
#         ax1.text(h, rk_errors[i] - 0.0002, f'{rk_errors[i]:.6f}', 
#                 ha='center', va='top', fontsize=9, color='blue')
    
#     # Plot 2: Solutions comparison for h = 0.1
#     ax2 = plt.subplot(2, 2, 2)
#     h_example = 0.1
#     if h_example in results:
#         data = results[h_example]
#         ax2.plot(data['analytical'][0], data['analytical'][1], 'k-', linewidth=3, label='Analytical Solution')
#         ax2.plot(data['euler'][0], data['euler'][1], 'ro--', linewidth=2, markersize=6, label='Euler Method')
#         ax2.plot(data['mod_euler'][0], data['mod_euler'][1], 'go--', linewidth=2, markersize=6, label='Modified Euler')
#         ax2.plot(data['rk'][0], data['rk'][1], 'bo--', linewidth=2, markersize=6, label='Runge-Kutta')
        
#         ax2.set_xlabel('x', fontsize=12, fontweight='bold')
#         ax2.set_ylabel('y(x)', fontsize=12, fontweight='bold')
#         ax2.set_title(f'Numerical Solutions vs Analytical (h = {h_example})', fontsize=14, fontweight='bold')
#         ax2.legend(fontsize=11)
#         ax2.grid(True, alpha=0.3)
    
#     # Plot 3: Bar chart of errors for all step sizes
#     ax3 = plt.subplot(2, 2, 3)
#     x_pos = np.arange(len(h_values))
#     width = 0.25
    
#     bars1 = ax3.bar(x_pos - width, euler_errors, width, label='Euler', color='red', alpha=0.7)
#     bars2 = ax3.bar(x_pos, mod_euler_errors, width, label='Modified Euler', color='green', alpha=0.7)
#     bars3 = ax3.bar(x_pos + width, rk_errors, width, label='Runge-Kutta', color='blue', alpha=0.7)
    
#     ax3.set_xlabel('Step Size (h)', fontsize=12, fontweight='bold')
#     ax3.set_ylabel('Absolute Error at x = 0.8', fontsize=12, fontweight='bold')
#     ax3.set_title('Error Comparison for Different Step Sizes', fontsize=14, fontweight='bold')
#     ax3.set_xticks(x_pos)
#     ax3.set_xticklabels([f'{h}' for h in h_values])
#     ax3.legend(fontsize=11)
#     ax3.grid(True, alpha=0.3)
    
#     # Add values on bars
#     for bars in [bars1, bars2, bars3]:
#         for bar in bars:
#             height = bar.get_height()
#             ax3.text(bar.get_x() + bar.get_width()/2., height,
#                     f'{height:.6f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
#     # Plot 4: Error reduction comparison
#     ax4 = plt.subplot(2, 2, 4)
#     # Calculate error ratios relative to largest step size
#     base_euler = euler_errors[0]
#     base_mod_euler = mod_euler_errors[0]
#     base_rk = rk_errors[0]
    
#     euler_ratio = [error/base_euler for error in euler_errors]
#     mod_euler_ratio = [error/base_mod_euler for error in mod_euler_errors]
#     rk_ratio = [error/base_rk for error in rk_errors]
    
#     ax4.plot(h_values, euler_ratio, 'ro-', linewidth=3, markersize=8, label='Euler Method')
#     ax4.plot(h_values, mod_euler_ratio, 'go-', linewidth=3, markersize=8, label='Modified Euler')
#     ax4.plot(h_values, rk_ratio, 'bo-', linewidth=3, markersize=8, label='Runge-Kutta')
    
#     ax4.set_xlabel('Step Size (h)', fontsize=12, fontweight='bold')
#     ax4.set_ylabel('Error Ratio (Relative to h=0.1)', fontsize=12, fontweight='bold')
#     ax4.set_title('Error Reduction with Decreasing Step Size', fontsize=14, fontweight='bold')
#     ax4.legend(fontsize=11)
#     ax4.grid(True, alpha=0.3)
#     ax4.set_xticks(h_values)
    
#     plt.tight_layout()
#     plt.show()

# def print_convergence_summary(h_values, euler_errors, mod_euler_errors, rk_errors):
#     print("\n" + "="*60)
#     print("CONVERGENCE SUMMARY")
#     print("="*60)
    
#     print(f"\n{'Step Size':<10} {'Euler Error':<15} {'Mod Euler Error':<18} {'RK Error':<15} {'Euler Improvement':<18} {'Mod Euler Improvement':<20} {'RK Improvement':<15}")
#     print("-"*110)
    
#     for i in range(len(h_values)):
#         if i == 0:
#             euler_improv = "-"
#             mod_euler_improv = "-"
#             rk_improv = "-"
#         else:
#             euler_improv = f"{euler_errors[i-1]/euler_errors[i]:.2f}x"
#             mod_euler_improv = f"{mod_euler_errors[i-1]/mod_euler_errors[i]:.2f}x"
#             rk_improv = f"{rk_errors[i-1]/rk_errors[i]:.2f}x"
        
#         print(f"{h_values[i]:<10} {euler_errors[i]:<15.6f} {mod_euler_errors[i]:<18.6f} {rk_errors[i]:<15.6f} {euler_improv:<18} {mod_euler_improv:<20} {rk_improv:<15}")

# # Main execution
# if __name__ == "__main__":
#     h_values, euler_errors, mod_euler_errors, rk_errors, results = analyze_ode_methods()
#     plot_linear_comparisons(h_values, euler_errors, mod_euler_errors, rk_errors, results)
#     print_convergence_summary(h_values, euler_errors, mod_euler_errors, rk_errors)


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import solve_ivp

# class ODE:
#     def __init__(self, x0, y0, h, xn, f_str):
#         self.x0 = x0
#         self.y0 = y0
#         self.h = h
#         self.xn = xn
#         self.f_str = f_str

#     def df(self, x, y):
#         return eval(self.f_str, {"x": x, "y": y, **np.__dict__})
    
#     def Euler(self):
#         x_vals = np.arange(self.x0, self.xn + self.h, self.h)
#         y_vals = [self.y0]
#         n = int((self.xn - self.x0) / self.h)

#         x = self.x0
#         y = self.y0

#         for i in range(n):
#             y_next = y + self.h * self.df(x, y)
#             y_vals.append(y_next)
#             x += self.h
#             y = y_next

#         return x_vals, y_vals

#     def RK(self):
#         x_vals = np.arange(self.x0, self.xn + self.h, self.h)
#         y_vals = [self.y0]
#         n = int((self.xn - self.x0) / self.h)

#         x = self.x0
#         y = self.y0

#         for i in range(n):
#             k1 = self.h * self.df(x, y)
#             k2 = self.h * self.df(x + self.h / 2, y + k1 / 2)
#             k3 = self.h * self.df(x + self.h / 2, y + k2 / 2)
#             k4 = self.h * self.df(x + self.h, y + k3)

#             y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
#             y_vals.append(y_next)
#             x += self.h
#             y = y_next

#         return x_vals, y_vals

# # Parameters
# x0, y0, xn = 0, 1, 0.8
# f_str = "x + y"

# # Test step sizes - including very small ones where error increases
# h_values = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.006, 0.003, 0.001, 0.0005, 0.0002, 0.0001]

# euler_errors = []
# rk_errors = []

# print("Step Size vs Error Analysis")
# print("="*40)

# for h in h_values:
#     ode_solver = ODE(x0, y0, h, xn, f_str)
    
#     # Use scipy for accurate analytical solution
#     sol = solve_ivp(ode_solver.df, [x0, xn], [y0], t_eval=[xn], rtol=1e-12, atol=1e-14)
#     y_exact = sol.y[0][0]
    
#     # Get numerical solutions
#     x_euler, y_euler = ode_solver.Euler()
#     x_rk, y_rk = ode_solver.RK()
    
#     # Calculate errors at x = 0.8
#     euler_error = abs(y_euler[-1] - y_exact)
#     rk_error = abs(y_rk[-1] - y_exact)
    
#     euler_errors.append(euler_error)
#     rk_errors.append(rk_error)
    
#     print(f"h = {h:.5f}: Euler Error = {euler_error:.8f}, RK Error = {rk_error:.8f}")

# # Create the single linear plot
# plt.figure(figsize=(12, 8))
# plt.plot(h_values, euler_errors, 'ro-', linewidth=3, markersize=8, label='Euler Method', markerfacecolor='red')
# plt.plot(h_values, rk_errors, 'bo-', linewidth=3, markersize=8, label='Runge-Kutta Method', markerfacecolor='blue')

# plt.xlabel('Step Size (h)', fontsize=14, fontweight='bold')
# plt.ylabel('Absolute Error at x = 0.8', fontsize=14, fontweight='bold')
# plt.title('Error Increases When Step Size Becomes Too Small\n(Round-off Error Dominance)', 
#           fontsize=16, fontweight='bold')

# plt.grid(True, alpha=0.3)
# plt.legend(fontsize=12)

# # Mark the optimal regions
# min_rk_idx = np.argmin(rk_errors)
# min_euler_idx = np.argmin(euler_errors)

# plt.axvline(x=h_values[min_rk_idx], color='blue', linestyle='--', alpha=0.7, 
#             label=f'Optimal h for RK ≈ {h_values[min_rk_idx]:.4f}')
# plt.axvline(x=h_values[min_euler_idx], color='red', linestyle='--', alpha=0.7, 
#             label=f'Optimal h for Euler ≈ {h_values[min_euler_idx]:.4f}')

# # Add annotations
# # #plt.annotate('Error decreases as h decreases\n(Truncation error dominates)', 
# #              xy=(0.05, euler_errors[2]), 
# #              xytext=(0.08, euler_errors[2]),
# #              arrowprops=dict(arrowstyle='->', color='black'),
# #              fontsize=11, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# # #plt.annotate('Error INCREASES as h decreases further!\n(Round-off error dominates)', 
# #              xy=(0.001, rk_errors[-4]), 
# #              xytext=(0.02, rk_errors[-4]),
# #              arrowprops=dict(arrowstyle='->', color='black'),
# #              fontsize=11, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="orange", alpha=0.7))

# # Add error values for key points
# for i, h in enumerate(h_values):
#     if i in [0, min_rk_idx, -1]:  # First, optimal, and last points
#         plt.text(h, rk_errors[i] + 0.0001, f'{rk_errors[i]:.6f}', 
#                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='blue')
#         plt.text(h, euler_errors[i] + 0.0001, f'{euler_errors[i]:.6f}', 
#                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='red')

# plt.tight_layout()
# plt.show()

# # Print the key findings
# print("\n" + "="*60)
# print("KEY OBSERVATIONS:")
# print("="*60)
# print(f"1. Optimal step size for Euler method: h ≈ {h_values[min_euler_idx]:.5f}")
# print(f"   Minimum Euler error: {euler_errors[min_euler_idx]:.8f}")
# print(f"2. Optimal step size for RK method: h ≈ {h_values[min_rk_idx]:.5f}")
# print(f"   Minimum RK error: {rk_errors[min_rk_idx]:.8f}")
# print(f"3. With very small h (0.0001):")
# print(f"   Euler error increases to: {euler_errors[-1]:.8f}")
# print(f"   RK error increases to: {rk_errors[-1]:.8f}")
# print("\n4. This demonstrates: TOO SMALL step sizes cause INCREASED errors!")
# print("   Due to accumulated round-off errors in finite precision arithmetic")

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class ODE:
    def __init__(self, x0, y0, x_end, f_str, actual_solution=None):
        self.x0 = x0
        self.y0 = y0
        self.x_end = x_end
        self.f_str = f_str
        self.actual_solution = actual_solution

    def df(self, x, y):
        return eval(self.f_str, {"x": x, "y": y, **np.__dict__})
    
    def f_actual(self, x):
        """Actual solution function - you can provide this or use numerical reference"""
        if self.actual_solution:
            return eval(self.actual_solution, {"x": x, "np": np})
        else:
            # Use scipy's high-accuracy solution as reference
            sol = solve_ivp(self.df, [self.x0, x], [self.y0], t_eval=[x], rtol=1e-12, atol=1e-14)
            return sol.y[0][0]
    
    def eulers_method(self, h):
        x_vals = np.arange(self.x0, self.x_end + h, h)
        y_vals = [self.y0]
        n = int((self.x_end - self.x0) / h)

        x = self.x0
        y = self.y0

        for i in range(n):
            y_next = y + h * self.df(x, y)
            y_vals.append(y_next)
            x += h
            y = y_next

        return x_vals, y_vals

    def modified_euler_method(self, h):
        x_vals = np.arange(self.x0, self.x_end + h, h)
        y_vals = [self.y0]
        n = int((self.x_end - self.x0) / h)

        x = self.x0
        y = self.y0

        for i in range(n):
            y_p = y + h * self.df(x, y)
            y_c = y + (h / 2) * (self.df(x, y) + self.df(x + h, y_p))
            y_vals.append(y_c)
            x += h
            y = y_c

        return x_vals, y_vals

    def rk4(self, h):
        x_vals = np.arange(self.x0, self.x_end + h, h)
        y_vals = [self.y0]
        n = int((self.x_end - self.x0) / h)

        x = self.x0
        y = self.y0

        for i in range(n):
            k1 = h * self.df(x, y)
            k2 = h * self.df(x + h / 2, y + k1 / 2)
            k3 = h * self.df(x + h / 2, y + k2 / 2)
            k4 = h * self.df(x + h, y + k3)

            y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y_vals.append(y_next)
            x += h
            y = y_next

        return x_vals, y_vals

    def compare_error(self, method="Eulers"):
        h_values = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]
        errors = []

        for h in h_values:
            if method == "Eulers":
                x, y = self.eulers_method(h)
            elif method == "Modified_Eulers":
                x, y = self.modified_euler_method(h)
            elif method == "RK4":
                x, y = self.rk4(h)
            else:
                print("Please enter a valid method.")
                return
            
            actual_value = self.f_actual(self.x_end)  
            err = abs(y[-1] - actual_value)
            errors.append(err)

        # SIMPLE LINEAR PLOT (no log-log)
        plt.figure(figsize=(10, 6))
        plt.plot(h_values, errors, 'bo-', linewidth=2, markersize=6)
        plt.title(f"Error vs Step Size ({method} Method)")
        plt.xlabel("Step size (h)")
        plt.ylabel(f"Absolute error at x = {self.x_end}")
        plt.grid(True, alpha=0.3)
        
        # Add value labels for some points
        for i, (h, err) in enumerate(zip(h_values, errors)):
            if i % 2 == 0:  # Label every other point to avoid clutter
                plt.text(h, err, f'{err:.2e}', ha='center', va='bottom', fontsize=8)
        
        plt.show()

        print(f"\nError Analysis for {method} Method:")
        print("="*50)
        for h_val, err in zip(h_values, errors):
            print(f"h = {h_val:.5f}, Error = {err:.8f}")

# Example usage:
if __name__ == "__main__":
    # For dy/dx = x + y, with y(0) = 1
    # Actual solution: y(x) = 2e^x - x - 1
    ode_solver = ODE(x0=0, y0=1, x_end=0.8, 
                    f_str="x + y", 
                    actual_solution="2*np.exp(x) - x - 1")
    
    # Compare errors for each method
    ode_solver.compare_error(method="Eulers")
    ode_solver.compare_error(method="Modified_Eulers") 
    ode_solver.compare_error(method="RK4")