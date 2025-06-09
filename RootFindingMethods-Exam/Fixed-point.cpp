#include "rootFinding.hpp"
#include <iostream>
#include <cmath>
using namespace std;

double rootFinding::Fixed_Point(double x0)
{
    double x = x0, prev;

    do
    {
        prev = x;
        x = f_x(x);
    } while (fabs(prev - x) > tol);

    return x;
}

double rootFinding::Bisection(double a, double b, double tol)
{
    if (f(a) * f(b) >= 0)
    {
        cerr << "Invalid interval: No sign change between " << a << " and " << b << endl;
        return NAN;
    }

    double c;
    while ((b - a) >= tol)
    {
        c = (a + b) / 2;

        if (fabs(f(c)) < tol)
            return c;

        if (f(c) * f(a) < 0)
            b = c;
        else
            a = c;
    }

    return c;
}
