#include "matrix.hpp"

int main()
{
    Matrix m1("matrix1L.txt");
    Matrix m2("matrix2.txt");
    Matrix m3("matrix1L.txt");
    Matrix m4("matrixLU.txt");
    Matrix m5("matrix1L.txt", "matrix1r.txt");
    Matrix m6("eqnmatrix.txt");
    Matrix result;

    cout << "Matrix 1:" << endl;
    m4.Display();

    cout << "Matrix 2:" << endl;
    m4.Display();

    result = m4.Add(m4);
    cout << "Result of addition:" << endl;
    result.Display();

    result = m4.Subtract(m4);
    cout << "Result of subtraction:" << endl;
    result.Display();

    result = m4.Multiply(m4);
    cout << "Result of multiplication:" << endl;
    result.Display();

    cout << (m4.isidentity() ? "Matrix 1 is an identity matrix." : "Matrix 1 is not an identity matrix.") << endl;
    cout << (m4.isSymmetric() ? "Matrix 1 is symmetric." : "Matrix 1 is not symmetric.") << endl;

    // cout << "Augmented Matrix:" << endl;
    // m5.Display();

    // Matrix solution1 = m5.Gauss_Elimination();
    // cout << "Solution:" << endl;
    // solution1.Display();

    // cout << "LU decomposition of the system:" << endl;
    // Matrix L(m4.rows, m4.cols), U(m4.rows, m4.cols);
    // m1.LU_Decomposition(L, U);

    // cout << "Lower triangular matrix L:" << endl;
    // L.Display();
    // cout << "Upper triangular matrix U:" << endl;
    // U.Display();

    // cout << "By Cholesky decomposition of the system:" << endl;
    // // m4.Cholesky_Decomposition();
    // Matrix solution = m5.Gauss_Seidel();

    // cout << "Solution using Gauss-Seidel:\n";
    // solution.Display(); // Print solution

    // Matrix solution2 = m5.Gauss_Jacobi();
    // cout << "Solution using Gauss-Jacobi:\n";
    // solution2.Display(); // Print solution

    double det = m4.Determinant();
    cout << "Determinant of Matrix is: " << det << endl;
    return 0;
}
