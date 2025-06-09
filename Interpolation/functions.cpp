#include <iomanip>
#include <sstream>
#include <cmath>
#include "main.hpp"

double Interpolation::lagrangeInterpolation(vector<double> &x_vals, vector<double> &y_vals, double x)
{
    int n = x_vals.size();
    double result = 0.0;

    for (int i = 0; i < n; i++)
    {
        double term = y_vals[i];
        for (int j = 0; j < n; j++)
        {
            if (i != j)
            {
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j]);
            }
        }
        result += term;
    }

    return result;
}