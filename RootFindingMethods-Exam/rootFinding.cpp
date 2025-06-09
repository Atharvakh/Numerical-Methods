#include "rootFinding.hpp"
rootFinding ::rootFinding(double tolerence)
{

    tol = tolerence;
}
double rootFinding::f(double x)
{
    return pow(x, 4) - 6 * pow(x, 3) + 11 * pow(x, 2) - 6 * x;
}

double rootFinding::f_x(double x)
{
    return (pow(x, 4) - 6 * pow(x, 3) + 11 * pow(x, 2)) / 6;
}
