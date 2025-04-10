#include "matrix.hpp"
#include <iostream>
using namespace std;

int main()
{
    Matrix m1("matrix1L.txt");
    Matrix m2("matrix2.txt");
    Matrix m3("matrix1L.txt");
    Matrix m4("matrixLU.txt");
    Matrix m5("matrix1L.txt", "matrix1r.txt");
    Matrix m6("eqnmatrix.txt");
    Matrix result;

    // std::cout << "Matrix 1:" << std::endl;
    // m1.Display();

    // std::cout << "Matrix 2:" << std::endl;
    // m2.Display();

    // result = m1.Add(m2);
    // std::cout << "Result of addition:" << std::endl;
    // result.Display();

    // result = m1.Subtract(m2);
    // std::cout << "Result of subtraction:" << std::endl;
    // result.Display();

    // result = m1.Multiply(m2);
    // std::cout << "Result of multiplication:" << std::endl;
    // result.Display();

    // std::cout << (m1.isidentity() ? "Matrix 1 is an identity matrix." : "Matrix 1 is not an identity matrix.") << std::endl;
    // std::cout << (m1.isSymmetric() ? "Matrix 1 is symmetric." : "Matrix 1 is not symmetric.") << std::endl;

    // std::cout << "Augmented Matrix:" << std::endl;
    // m5.Display();

    Matrix solution1 = m5.Gauss_Elimination();
    std::cout << "Solution:" << std::endl;
    solution1.Display();

    // std::cout << "LU decomposition of the system:" << std::endl;
    // Matrix L(m4.rows, m4.cols), U(m4.rows, m4.cols);
    // m1.LU_Decomposition(L, U);

    // std::cout << "Lower triangular matrix L:" << std::endl;
    // L.Display();
    // std::cout << "Upper triangular matrix U:" << std::endl;
    // U.Display();

    // std::cout << "By Cholesky decomposition of the system:" << std::endl;
    // m4.Cholesky_Decomposition();
    Matrix solution = m5.Gauss_Seidel();

    std::cout << "Solution using Gauss-Seidel:\n";
    solution.Display(); // Print solution

    Matrix solution2 = m5.Gauss_Jacobi();
    std::cout << "Solution using Gauss-Jacobi:\n";
    solution2.Display(); // Print solution

    return 0;
}
