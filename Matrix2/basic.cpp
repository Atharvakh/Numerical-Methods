#include "matrix.hpp"
#include <fstream>
#include <stdexcept>

Matrix::Matrix() : rows(0), cols(0), mat(nullptr) {}

Matrix::Matrix(int rows, int cols)
{
    this->rows = rows;
    this->cols = cols;
    mat = new double *[rows];
    for (int i = 0; i < rows; ++i)
    {
        mat[i] = new double[cols];
    }
}

Matrix::~Matrix()
{
    for (int i = 0; i < rows; ++i)
    {
        delete[] mat[i];
    }
    delete[] mat;
}

Matrix::Matrix(const string &filename)
{
    ifstream file(filename);
    if (!file.is_open())
    {
        throw runtime_error("Unable to open file.");
    }

    file >> rows >> cols;
    mat = new double *[rows];
    for (int i = 0; i < rows; ++i)
    {
        mat[i] = new double[cols];
        for (int j = 0; j < cols; ++j)
        {
            file >> mat[i][j];
        }
    }
    file.close();
}

Matrix::Matrix(const Matrix &m) : rows(m.rows), cols(m.cols) // copy constructor definition
{
    mat = new double *[rows];
    for (int i = 0; i < rows; ++i)
    {
        mat[i] = new double[cols];
        for (int j = 0; j < cols; ++j)
        {
            mat[i][j] = m.mat[i][j];
        }
    }
}
void Matrix::Display() const
{
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}
Matrix &Matrix::operator=(const Matrix &m)
{
    if (this != &m)
    {

        for (int i = 0; i < rows; ++i)
        {
            delete[] mat[i];
        }
        delete[] mat;

        rows = m.rows;
        cols = m.cols;
        mat = new double *[rows];
        for (int i = 0; i < rows; ++i)
        {
            mat[i] = new double[cols];
            for (int j = 0; j < cols; ++j)
            {
                mat[i][j] = m.mat[i][j];
            }
        }
    }
    return *this;
}
