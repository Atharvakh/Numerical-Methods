#include "rootFinding.hpp"
#include <math.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

vector<double> rootFinding::get_interval()
{
    vector<double> interval(2);
    double x = 0, y = 1;
    while (x > -10 && y < 10)
    {
        if (f(x) * f(y) < 0)
        {
            interval[0] = x;
            interval[1] = y;
            return interval;
        }
        else
        {
            x--;
            y++;
        }
    }
    exit(1);
}

double rootFinding::Bisection(double a, double b)
{
    double m, prev_m = 0.0;
    // double m = 0.0;

    if (f(a) * f(b) >= 0) // if a and b have same signs
    {
        cout << "Incorrect a and b." << endl;
        return 0;
    }

    do
    {
        prev_m = m;
        m = (a + b) / 2;
        if (f(m) == 0)
        {

            break;
        }
        if (f(m) * f(a) < 0)
        {
            b = m;
        }
        else
        {
            a = m;
        }

    } while (fabs(m - prev_m) > tol);

    return m;
}

double rootFinding ::Bisection()
{
    vector<double> interval(2);
    interval = get_interval();
    a = interval[0];
    b = interval[1];
    return Bisection(a, b);
}