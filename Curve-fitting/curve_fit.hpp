#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class curve_fit
{
public:
    double a = 0, b = 0, c = 0, A = 0, B = 0, rms;
    vector<double> x, y;
    double x_input, y_input;

    void leastSquaresFit(const vector<double> &x, const vector<double> &y, double &a, double &b); // linear fit
    void parabolaFit(const vector<double> &x, const vector<double> &y, double &a, double &b, double &c);
    void exponentialFit(const vector<double> &x, const vector<double> &y, double &A, double &B);
    double calculateRMS(const vector<double> &x, const vector<double> &y, double a, double b);
    double calculateRMS(const vector<double> &x, const vector<double> &y, double a, double b, double c);
    double calculateERMS(const vector<double> &x, const vector<double> &y, double A, double B);
};

// g++ main.cpp curve_fit.cpp  ../Matrix2/add.cpp ../Matrix2/basic.cpp -I ../Matrix2/ -o rms t run the code