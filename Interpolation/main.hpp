#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Interpolation
{
public:
    vector<double> x_vals, y_vals;
    double x_input, y_input;
    double lagrangeInterpolation(vector<double> &x_vals, vector<double> &y_vals, double x);
};