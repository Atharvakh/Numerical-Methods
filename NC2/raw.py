# # --------------------------------------------------------------------
# # Utility Functions
# # --------------------------------------------------------------------

# def divided_diff(x, y):
#     """Divided Difference Table for unequally spaced data."""
#     n = len(y)
#     table = np.zeros((n, n))
#     table[:, 0] = y
#     for j in range(1, n):
#         for i in range(n - j):
#             table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])
#     print("\nDivided Difference Table:\n", table)
#     return table[0, :]


# def forward_diff(y):
#     """Forward Difference Table for equally spaced data."""
#     n = len(y)
#     table = np.zeros((n, n))
#     table[:, 0] = y
#     for j in range(1, n):
#         for i in range(n - j):
#             table[i, j] = table[i + 1, j - 1] - table[i, j - 1]
#     print("\nForward Difference Table:\n", table)
#     return table


# # --------------------------------------------------------------------
# # Polynomial Builders
# # --------------------------------------------------------------------

# def build_divided_polynomial(x, coeffs):
#     """Newton’s divided difference polynomial (string)."""
#     terms = [f"{coeffs[0]:.6f}"]
#     for i in range(1, len(coeffs)):
#         term = f"{coeffs[i]:+.6f}"
#         if coeffs[i] == 0:
#             continue
#         for j in range(i):
#             term += f" * (x - {x[j]})"
#         terms.append(term)
#     return " ".join(terms)


# def build_forward_polynomial(x, forward_table):
#     """Newton’s forward polynomial (string)."""
#     h = x[1] - x[0]
#     coeffs = forward_table[0, :]
#     terms = [f"{coeffs[0]:.6f}"]
#     for i in range(1, len(coeffs)):
#         if coeffs[i] == 0:
#             continue
#         term = f"{coeffs[i]:+.6f} / {math.factorial(i)}"
#         for j in range(i):
#             term += f" * (u - {j})"
#         terms.append(term)
#     return " + ".join(terms).replace("+ -", "- ")


# def build_backward_polynomial(x, backward_table):
#     """Newton’s backward polynomial (string form)."""
#     coeffs = backward_table[0, :]
#     terms = [f"{coeffs[0]:.6f}"]
#     for i in range(1, len(coeffs)):
#         if coeffs[i] == 0:
#             continue
#         term = f"{coeffs[i]:+.6f} / {math.factorial(i)}"
#         for j in range(i):
#             term += f" * (u - {j})"
#         terms.append(term)
#     return " + ".join(terms).replace("+ -", "- ")



# def build_stirling_polynomial(x, forward_table):
#     """Stirling’s central interpolation polynomial (string)."""
#     n = len(x)
#     h = x[1] - x[0]
#     mid = (n - 1) // 2
#     poly_str = f"{forward_table[mid,0]:.6f}"
#     for j in range(1, n):
#         if j % 2 == 1:  # odd terms (average of central differences)
#             coeff = (forward_table[mid - (j - 1)//2 - 1, j] +
#                      forward_table[mid - (j - 1)//2, j]) / 2.0
#             if coeff == 0:
#                 continue
#         else:  # even terms
#             coeff = forward_table[mid - j//2, j]
#             if coeff == 0:
#                 continue
#         term = f"{coeff:+.6f} / {math.factorial(j)}"
#         for k in range(j):
#             term += f" * (x - {x[mid - j//2 + k]})"
#         poly_str += " " + term
#     return poly_str.replace("+ -", "- ")


# # --------------------------------------------------------------------
# # Polynomial Evaluators
# # --------------------------------------------------------------------

# def evaluate_divided_polynomial(x, coeffs, x_val):
#     """Evaluate Newton’s divided difference polynomial."""
#     n = len(coeffs)
#     result = coeffs[0]
#     for i in range(1, n):
#         term = coeffs[i]
#         for j in range(i):
#             term *= (x_val - x[j])
#         result += term
#     return result


# def evaluate_forward_polynomial(x, forward_table, x_val):
#     """Evaluate Newton’s forward interpolation."""
#     h = x[1] - x[0]
#     u = (x_val - x[0]) / h
#     coeffs = forward_table[0, :]
#     n = len(coeffs)
#     result = coeffs[0]
#     u_term = 1
#     for i in range(1, n):
#         u_term *= (u - (i - 1))
#         result += (u_term / math.factorial(i)) * coeffs[i]
#     return result


# def evaluate_backward_polynomial(x, backward_table, x_val):
#     """Evaluate Newton’s backward interpolation properly."""
#     h = x[1] - x[0]
#     u = (x_val - x[-1]) / h  # backward formula uses xn
#     coeffs = backward_table[0, :]
#     n = len(coeffs)
#     result = coeffs[0]
#     u_term = 1
#     for i in range(1, n):
#         u_term *= (u + (i - 1))
#         result += (u_term / math.factorial(i)) * coeffs[i]
#     return result



# def evaluate_stirling_polynomial(x, forward_table, x_val):
#     """Evaluate Stirling’s interpolation."""
#     n = len(x)
#     h = x[1] - x[0]
#     mid = (n - 1) // 2
#     u = (x_val - x[mid]) / h
#     result = forward_table[mid, 0]
#     u_term = 1
#     for j in range(1, n):
#         if j % 2 == 1:
#             coeff = (forward_table[mid - (j - 1)//2 - 1, j] +
#                      forward_table[mid - (j - 1)//2, j]) / 2.0
#         else:
#             coeff = forward_table[mid - j//2, j]
#         u_term *= (u - (j - 1)/2)
#         result += (u_term / math.factorial(j)) * coeff
#     return result




# def main():
#     x_data, y_data = [], []

#     try:
#         with open('table.txt', 'r') as f:
#             for line in f:
#                 x, y = map(float, line.split())
#                 x_data.append(x)
#                 y_data.append(y)
#     except FileNotFoundError:
#         print("Error: table.txt not found.")
#         return

#     x = np.array(x_data)
#     y = np.array(y_data)
#     print("x_data:", x)
#     print("y_data:", y)

#     try:
#         x_val = float(input("\nEnter value of x to interpolate: "))
#     except ValueError:
#         print("Invalid input.")
#         return

#     h = x[1] - x[0] if len(x) > 1 else None
#     equally_spaced = np.allclose(np.diff(x), h)

#     if not equally_spaced:
#         print("\nUnequally spaced → Divided Differences Method")
#         coeffs = divided_diff(x, y)
#         print("Polynomial: P(x) =", build_divided_polynomial(x, coeffs))
#         print(f"Interpolated value at x={x_val}: {evaluate_divided_polynomial(x, coeffs, x_val):.6f}")

#     else:
#         print("\nEqually spaced → Forward, Backward, Stirling Methods")

#         # Forward
#         forward_table = forward_diff(y)
#         print("Forward Polynomial: P(x) =", build_forward_polynomial(x, forward_table))
#         print(f"Value at x={x_val}: {evaluate_forward_polynomial(x, forward_table, x_val):.6f}")

#         # Backward
#         backward_table = forward_diff(y[::-1])   # build differences from reversed y
#         print("\nBackward Polynomial: P(x) =", build_backward_polynomial(x, backward_table))
#         print(f"Value at x={x_val}: {evaluate_backward_polynomial(x, backward_table, x_val):.6f}")

#         # Stirling (for odd number of points)
#         if len(x) % 2 == 1:
#             print("\nStirling Polynomial: P(x) =", build_stirling_polynomial(x, forward_table))
#             print(f"Value at x={x_val}: {evaluate_stirling_polynomial(x, forward_table, x_val):.6f}")


# if __name__ == "__main__":
#     main()