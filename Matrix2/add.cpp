#include <iostream>
#include "matrix.hpp"
#include "iomanip"
#ifdef _WIN32
#include <conio.h>
#endif
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

Matrix Matrix::Add(const Matrix &m) const
{
    if (this->rows != m.rows || this->cols != m.cols)
    {
        throw std::runtime_error("Matrix dimensions do not match for addition.");
    }

    Matrix result(this->rows, this->cols);
    for (int i = 0; i < this->rows; ++i)
    {
        for (int j = 0; j < this->cols; ++j)
        {
            result.mat[i][j] = this->mat[i][j] + m.mat[i][j];
        }
    }
    return result;
}

Matrix Matrix::Subtract(const Matrix &m) const
{
    if (this->rows != m.rows || this->cols != m.cols)
    {
        throw std::runtime_error("Matrix dimensions do not match for subtraction.");
    }

    Matrix result(this->rows, this->cols);
    for (int i = 0; i < this->rows; ++i)
    {
        for (int j = 0; j < this->cols; ++j)
        {
            result.mat[i][j] = this->mat[i][j] - m.mat[i][j];
        }
    }
    return result;
}

Matrix Matrix::Multiply(const Matrix &m) const
{
    if (this->cols != m.rows)
    {
        throw std::runtime_error("Matrix dimensions do not allow multiplication.");
    }

    Matrix result(this->rows, m.cols);
    for (int i = 0; i < this->rows; ++i)
    {
        for (int j = 0; j < m.cols; ++j)
        {
            result.mat[i][j] = 0;
            for (int k = 0; k < this->cols; ++k)
            {
                result.mat[i][j] += this->mat[i][k] * m.mat[k][j];
            }
        }
    }
    return result;
}

bool Matrix::isidentity() const
{
    if (rows != cols)
        return false;

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if ((i == j && mat[i][j] != 1) || (i != j && mat[i][j] != 0))
            {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isSymmetric() const
{
    if (rows != cols)
        return false;

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (mat[i][j] != mat[j][i])
            {
                return false;
            }
        }
    }
    return true;
}

Matrix::Matrix(const std::string &filename1, const std::string &filename2)
{
    std::ifstream file1(filename1);
    std::ifstream file2(filename2);
    if (!file1.is_open() || !file2.is_open())
    {
        throw std::runtime_error("Unable to open file(s).");
    }
    int r, c;
    file1 >> r >> c;
    this->rows = r;
    this->cols = c;
    mat = new double *[rows];
    for (int i = 0; i < rows; ++i)
    {
        mat[i] = new double[cols];
        for (int j = 0; j < cols; ++j)
        {
            if (j == cols - 1)
            {
                file2 >> mat[i][j];
            }
            else
            {
                file1 >> mat[i][j];
            }
        }
    }
    file1.close();
    file2.close();
}

Matrix Matrix::Gauss_Elimination()
{
    if (cols != rows + 1)
    {
        throw std::runtime_error("Matrix must be augmented (cols = rows + 1) for Gaussian elimination.");
    }

    Matrix result(*this);
    Matrix solution(rows, 1);

    // Forward Elimination with Basic Pivoting
    for (int m = 0; m < rows; m++)
    {
        // Basic Pivoting: Swap rows if diagonal element is zero
        if (result.mat[m][m] == 0)
        {
            for (int k = m + 1; k < rows; k++)
            {
                if (result.mat[k][m] != 0)
                {
                    std::swap(result.mat[m], result.mat[k]);
                    break;
                }
            }
        }

        double pivot = result.mat[m][m];
        if (pivot == 0)
        {
            throw std::runtime_error("Error: Zero pivot encountered after row swaps, cannot proceed.");
        }

        // Normalize the pivot row
        for (int n = m; n < cols; n++)
        {
            result.mat[m][n] /= pivot;
        }

        for (int m1 = m + 1; m1 < rows; m1++)
        {
            double factor = result.mat[m1][m];
            for (int n = m; n < cols; n++)
            {
                result.mat[m1][n] -= factor * result.mat[m][n];
            }
        }
    }
    cout << endl;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cout << " " << result.mat[i][j];
        }
        cout << endl;
    }

    // Back Substitution
    for (int m = rows - 1; m >= 0; m--)
    {
        solution.mat[m][0] = result.mat[m][cols - 1];
        for (int n = m + 1; n < rows; n++)
        {
            solution.mat[m][0] -= result.mat[m][n] * solution.mat[n][0];
        }
    }

    return solution;
}

void Matrix::LU_Decomposition(Matrix &L, Matrix &U) const
{
    if (this->rows != this->cols)
    {
        throw std::runtime_error("LU decomposition requires a square matrix.");
    }
    int n = this->rows;
    L = Matrix(n, n);
    U = Matrix(n, n);

    for (int i = 0; i < n; ++i)
    {
        L.mat[i][i] = 1.0;
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (i != j)
            {
                L.mat[i][j] = 0;
            }
            else
            {
                continue;
            }
        }
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            U.mat[i][j] = 0.0;
        }
    }

    for (int j = 0; j < n; ++j)
    {
        for (int i = j; i < n; ++i)
        {
            U.mat[j][i] = this->mat[j][i];
            for (int k = 0; k < j; ++k)
            {
                U.mat[j][i] -= L.mat[j][k] * U.mat[k][i];
            }
        }

        for (int i = j + 1; i < n; ++i)
        {
            if (i <= j)
                continue;

            if (U.mat[j][j] == 0.0)
            {
                throw std::runtime_error("Singular matrix detected.");
            }
            L.mat[i][j] = this->mat[i][j];
            for (int k = 0; k < j; ++k)
            {
                L.mat[i][j] -= L.mat[i][k] * U.mat[k][j];
            }
            L.mat[i][j] /= U.mat[j][j];
        }
    }
}

void Matrix::Cholesky_Decomposition()
{
    this->Display();
    if (this->rows != this->cols)
    {
        throw std::runtime_error("Cholesky decomposition requires a symmetric, positive-definite matrix.");
    }
    if (!isSymmetric())
    {
        throw std::runtime_error("Matrix is not symmetric.");
    }

    int n = this->rows;
    Matrix L(n, n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            L.mat[i][j] = 0;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j <= i; ++j)
        {
            double sum = 0;

            for (int k = 0; k < j; ++k)
            {
                sum += L.mat[i][k] * L.mat[j][k];
            }

            if (i == j)
            {
                L.mat[i][i] = sqrt(this->mat[i][i] - sum);
            }
            else
            {
                L.mat[i][j] = (this->mat[i][j] - sum) / L.mat[j][j];
            }
        }
        L.Display();
    }
}

bool Matrix::isDiagonallyDominant() const
{
    for (int i = 0; i < rows; i++)
    {
        double sum = 0.0;
        for (int j = 0; j < cols - 1; j++)
        {
            if (i != j)
            {
                sum += std::fabs(mat[i][j]); // Sum of non-diagonal elements
            }
        }

        if (std::fabs(mat[i][i]) < sum)
        {
            return false; // Not diagonally dominant
        }
    }
    return true; // It is diagonally dominant
}

Matrix Matrix::Gauss_Seidel(int maxIterations, double tolerance)
{
    if (cols != rows + 1)
    {
        throw std::runtime_error("Matrix must be augmented (cols = rows + 1) for Gauss-Seidel.");
    }

    // Ensure the matrix is diagonally dominant
    // if (!isDiagonallyDominant())
    // {
    //     std::cout << "Matrix is not diagonally dominant." << std::endl;
    //     return -1;
    // }

    // Solution vector as a single-column matrix
    Matrix x(rows, 1);
    Matrix old_x(rows, 1);

    // Initialize solution with zeros
    for (int i = 0; i < rows; i++)
    {
        x.mat[i][0] = 0.0;
        old_x.mat[i][0] = 0.0;
    }

    for (int iter = 0; iter < maxIterations; iter++)
    {
        for (int i = 0; i < rows; i++)
        {
            double sum = mat[i][cols - 1]; // Start with b[i]

            for (int j = 0; j < cols - 1; j++)
            {
                if (j != i)
                {
                    sum -= mat[i][j] * x.mat[j][0]; // Corrected element access
                }
            }

            x.mat[i][0] = sum / mat[i][i]; // Update variable
        }

        // Check for convergence
        double maxDiff = 0.0;
        for (int i = 0; i < rows; i++)
        {
            maxDiff = std::max(maxDiff, std::fabs(x.mat[i][0] - old_x.mat[i][0]));
        }

        if (maxDiff < tolerance)
        {
            std::cout << "Gauss-Seidel Converged in " << iter + 1 << " iterations.\n";
            return x;
        }

        old_x = x; // Store new values for next iteration
    }
}

Matrix Matrix::Gauss_Jacobi(int maxIterations, double tolerance)
{
    if (cols != rows + 1)
    {
        throw std::runtime_error("Matrix must be augmented (cols = rows + 1) for Gauss-Seidel.");
    }

    // Ensure the matrix is diagonally dominant
    // if (!isDiagonallyDominant())
    // {
    //     std::cout << "Matrix is not diagonally dominant." << std::endl;
    // }

    // Solution vector as a single-column matrix
    Matrix x(rows, 1);
    Matrix old_x(rows, 1);

    // Initialize solution with zeros
    for (int i = 0; i < rows; i++)
    {
        x.mat[i][0] = 0.0;
        old_x.mat[i][0] = 0.0;
    }

    for (int iter = 0; iter < maxIterations; iter++)
    {
        for (int i = 0; i < rows; i++)
        {
            double sum = mat[i][cols - 1]; // Start with b[i]

            for (int j = 0; j < cols - 1; j++)
            {
                if (j != i)
                {
                    sum -= mat[i][j] * old_x.mat[j][0]; // Corrected element access
                }
            }

            x.mat[i][0] = sum / mat[i][i]; // Update variable
        }

        // Check for convergence
        double maxDiff = 0.0;
        for (int i = 0; i < rows; i++)
        {
            maxDiff = std::max(maxDiff, std::fabs(x.mat[i][0] - old_x.mat[i][0]));
        }

        if (maxDiff < tolerance)
        {
            std::cout << "Gauss_Jacobi Converged in " << iter + 1 << " iterations.\n";
            return x;
        }

        old_x = x; // Store new values for next iteration
    }
}
