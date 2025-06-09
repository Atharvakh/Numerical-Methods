#include "rootFinding.hpp"
#include <cmath>
double rootFinding::Fixed_Point()
{
    double x = x0, prev;

    do
    {
        prev = x;
        x = f_x(x);

    } while (fabs(prev - x) > tol);

    return x;
}