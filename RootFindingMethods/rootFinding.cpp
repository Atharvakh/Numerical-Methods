#include "rootFinding.hpp"
rootFinding ::rootFinding(double tolerence)
{
    a = b = 0.0;
    tol = 0.0001;
    x0 = 1.0;
}
double rootFinding::f(double x)
{
    return (x * x) - (5 * x) + 5;
}
double rootFinding::f_dash(double x)
{
    return (2 * x - 5);
}

double rootFinding::f_x(double x)
{
    return ((x * x + 5) / 5);
}