#include "curve_fit.hpp"
#include "../Matrix2/matrix.hpp"

void curve_fit::leastSquaresFit(const vector<double> &x, const vector<double> &y, double &a, double &b)
{
    int n = x.size();
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

    for (int i = 0; i < n; ++i)
    {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
    }

    a = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    b = (sumY - a * sumX) / n;
}

void curve_fit::parabolaFit(const vector<double> &x, const vector<double> &y, double &a, double &b, double &c)
{
    int n = x.size();
    double Sx = 0, Sx2 = 0, Sx3 = 0, Sx4 = 0;
    double Sy = 0, Sxy = 0, Sx2y = 0;

    for (int i = 0; i < n; ++i)
    {
        double xi = x[i], yi = y[i];
        double xi2 = xi * xi;
        double xi3 = xi2 * xi;
        double xi4 = xi3 * xi;

        Sx += xi;
        Sx2 += xi2;
        Sx3 += xi3;
        Sx4 += xi4;
        Sy += yi;
        Sxy += xi * yi;
        Sx2y += xi2 * yi;
    }

    // Coefficient matrix A (3x4 augmented)
    Matrix A(3, 4);

    // Fill augmented matrix
    A.mat[2][0] = Sx2;
    A.mat[2][1] = Sx;
    A.mat[2][2] = n;
    A.mat[2][3] = Sy;
    A.mat[1][0] = Sx3;
    A.mat[1][1] = Sx2;
    A.mat[1][2] = Sx;
    A.mat[1][3] = Sxy;
    A.mat[0][0] = Sx4;
    A.mat[0][1] = Sx3;
    A.mat[0][2] = Sx2;
    A.mat[0][3] = Sx2y;

    // Solve using Gaussian Elimination
    Matrix result = A.Gauss_Elimination(); // Should store solution in result.solution
    // result.Display();
    //   Assign coefficients
    a = result.mat[0][0];
    b = result.mat[1][0];
    c = result.mat[2][0];
}

void curve_fit::exponentialFit(const vector<double> &x, const vector<double> &y, double &A, double &B)
{
    int n = x.size();
    double sumX = 0, sumLogY = 0, sumXLogY = 0, sumX2 = 0;

    for (int i = 0; i < n; ++i)
    {
        if (y[i] <= 0)
        {
            cerr << "Error: y[" << i << "] = " << y[i] << " is not > 0, cannot apply log.\n";
            return;
        }

        double logY = log(y[i]);
        sumX += x[i];
        sumLogY += logY;
        sumXLogY += x[i] * logY;
        sumX2 += x[i] * x[i];
    }

    double a = (n * sumXLogY - sumX * sumLogY) / (n * sumX2 - sumX * sumX);
    double b = (sumLogY - a * sumX) / n;

    B = a;
    A = exp(b);
}

double curve_fit::calculateRMS(const vector<double> &x, const vector<double> &y, double a, double b)
{
    int n = x.size();
    double sumSquaredError = 0;

    for (int i = 0; i < n; ++i)
    {
        double y_pred = a * x[i] + b;
        sumSquaredError += (y[i] - y_pred) * (y[i] - y_pred);
    }

    return sqrt(sumSquaredError / n);
}
double curve_fit::calculateRMS(const vector<double> &x, const vector<double> &y, double a, double b, double c)
{
    int n = x.size();
    double sumSquaredError = 0;

    for (int i = 0; i < n; ++i)
    {
        double y_pred = a * x[i] * x[i] + b * x[i] + c;
        sumSquaredError += (y[i] - y_pred) * (y[i] - y_pred);
    }

    return sqrt(sumSquaredError / n);
}
double curve_fit::calculateERMS(const vector<double> &x, const vector<double> &y, double A, double B)
{
    int n = x.size();
    double sumSquaredError = 0;

    for (int i = 0; i < n; ++i)
    {
        double y_pred = A * exp(B * x[i]);
        sumSquaredError += (y[i] - y_pred) * (y[i] - y_pred);
    }

    return sqrt(sumSquaredError / n);
}
