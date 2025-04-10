#include <string>
#include <vector>
#include <iostream>

class Matrix
{
public:
    int rows, cols;
    double **mat;
    std::vector<double> solution;

    Matrix();                            // Default constructor
    Matrix(int, int);                    // Parameterized constructor
    ~Matrix();                           // Destructor
    Matrix(const std::string &filename); // File constructor
    Matrix(const Matrix &m);             // Copy constructor
    Matrix &operator=(const Matrix &m);
    Matrix(const std::string &filename1, const std::string &filename2);

    void Display() const;
    Matrix Add(const Matrix &m) const;      // const correctness
    Matrix Subtract(const Matrix &m) const; // const correctness
    Matrix Multiply(const Matrix &m) const; // Matrix multiplication function

    bool isidentity() const;  // Identity matrix check
    bool isSymmetric() const; // Symmetry check
    Matrix Augment() const;   // Augment matrix
    Matrix Gauss_Elimination();
    void LU_Decomposition(Matrix &L, Matrix &U) const;
    void Cholesky_Decomposition();
    bool isDiagonallyDominant() const;
    Matrix Gauss_Seidel(int maxIterations = 100, double tolerance = 0.000001);
    Matrix Gauss_Jacobi(int maxIterations = 100, double tolerance = 0.000001);
};
