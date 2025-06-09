#include "rootFinding.hpp"
// #include "rootFinding.cpp"
#include <ostream>
#include <iostream>
using namespace std;
int main()
{
    rootFinding f1(0.001);

    // double root = f1.Bisection();
    // cout << "Root using Bisection method :: " << root << endl;

    // root = f1.NewtRaphson(1);
    // cout << "Root using Newton-Raphson method :: " << root << endl;
    double root0 = f1.Bisection(-0.5, 0.5, 0.001);
    cout << "Root in (-0.5,0.5): " << root0 << endl;

    double root1 = f1.Bisection(0.5, 1.5, 0.001);
    cout << "Root in (0,1): " << root1 << endl;

    double root2 = f1.Bisection(1.5, 2.5, 0.001);
    cout << "Root in (1,2): " << root2 << endl;

    double root3 = f1.Bisection(2.5, 3.5, 0.001);
    cout << "Root in (2,3): " << root3 << endl;

    double root4 = f1.Bisection(3.5, 4.5, 0.001);
    cout << "Root in (3,4): " << root4 << endl;

    double root = f1.Fixed_Point(root1);
    cout << "Root using Fixed-Point method :: " << root << endl;

    double root5 = f1.Fixed_Point(root2);
    cout << "Root using Fixed-Point method :: " << root5 << endl;

    return 0;
}