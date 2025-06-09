#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int rows, cols;
    ifstream file("matrix.txt"); // Replace "matrix.txt" with your file name

    // Read the dimensions of the matrix
    file >> rows >> cols;

    // Create a 2D vector to store the matrix
    vector<vector<double>> matrix(rows, vector<double>(cols));
    vector<double> ans(rows);

    // Read the matrix from the file
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            file >> matrix[i][j];
        }
    }

    file.close();

    // Traverse and print the matrix
    cout << "Matrix:" << endl;
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    // Triangulate the matrix
    for (int m = 0; m < rows; m++)
    {
        double pivot = matrix[m][m];
        if (pivot == 0) // Check for zero pivot element
        {
            cerr << "Error: Zero pivot encountered, cannot proceed." << endl;
            return 1;
        }

        for (int n = 0; n < cols; n++)
        {
            matrix[m][n] = matrix[m][n] / pivot;
        }

        for (int m1 = m + 1; m1 < rows; m1++)
        {
            double e = matrix[m1][m];
            for (int n = m; n < cols; n++)
            {
                matrix[m1][n] = matrix[m1][n] - e * matrix[m][n];
            }
        }
    }

    // Printing the triangular matrix
    cout << "Upper triangular matrix is" << endl;
    for (int m = 0; m < rows; m++)
    {
        for (int n = 0; n < cols; n++)
        {
            cout << matrix[m][n] << "\t";
        }
        cout << endl;
    }

    // Solving the system of equations using back substitution
    for (int m = rows - 1; m >= 0; m--)
    {
        ans[m] = matrix[m][cols - 1];
        for (int n = m + 1; n < rows; n++)
        {
            ans[m] = ans[m] - (matrix[m][n] * ans[n]);
        }
    }

    cout << "Solution of the system of equations is" << endl;
    for (int m = 0; m < rows; m++)
    {
        cout << "X" << m + 1 << " = " << ans[m] << endl;
    }

    return 0;
}
