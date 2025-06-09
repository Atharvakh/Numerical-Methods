#include <cmath>
#include <vector>
using namespace std;
class rootFinding
{
    double a, b, x0;
    double tol;

public:
    // rootFinding();           // Default constructor
    rootFinding(double tol); // Parameterized constructor
    double f(double x);      // Function
    double f_dash(double x); // Function derivative
    double f_x(double x);    // Function for fixed point

    vector<double> get_interval();
    double Bisection(double a, double b);
    double Bisection();
    double NewtRaphson(double x);
    // double NewtRaphson();
    double Fixed_Point();
};