import numpy as np
class power_method:
    def __init__(self, A, x0, tol, max_iter):
        self.A = A
        self.x0 = x0
        self.tol = tol
        self.max_iter = max_iter
        
    def power_fun(self):
        n, m = self.A.shape
        if n != m:
            raise ValueError("Matrix must be square")

        eigenvalue_old = 0
        x = self.x0
        for i in range(self.max_iter):
            # Multiply matrix with vector
            x_new = np.dot(self.A, x)

            # Get dominant eigenvalue (approx)
            eigenvalue_new = np.max(np.abs(x_new))

            # Normalize the vector
            x = x_new / eigenvalue_new

            # Check for convergence
            if np.abs(eigenvalue_new - eigenvalue_old) < self.tol:
                print(f"Converged in {i+1} iterations.")
                break

            eigenvalue_old = eigenvalue_new

        return eigenvalue_new, x