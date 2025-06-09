#include "rootFinding.hpp"
// #include "rootFinding.cpp"
#include <ostream>
#include <iostream>
using namespace std;
int main()
{
    rootFinding f1(0.001);

    double root = f1.Bisection();
    cout << "Root using Bisection method :: " << root << endl;

    root = f1.NewtRaphson(1);
    cout << "Root using Newton-Raphson method :: " << root << endl;

    root = f1.Fixed_Point();
    cout << "Root using Fixed-Point method :: " << root << endl;
    return 0;
}