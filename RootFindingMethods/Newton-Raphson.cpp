#include "rootFinding.hpp"
// #include "rootFinding.cpp"
#include <cmath>
using namespace std;
double rootFinding::NewtRaphson(double a)
{
    double x = a;
    for (int i = 0; i < 100; i++) // do this with while loop
    {
        double fx = f(x);
        double f_prime = f_dash(x);
        if (fabs(f_prime) < tol)
            break;
        x = x - fx / f_prime;
    }
    return x;
}

// double rootFinding::NewtRaphson()
// {
//     return NewtRaphson(x0);
// }