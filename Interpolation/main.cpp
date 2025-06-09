#include "main.hpp"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <limits>

using namespace std;

int main()
{
    const int n = 12;
    const double PI = acos(-1.0);
    ofstream cheb_nodes("nodes.txt"); // we are writing nodes of cheby chev to the file

    if (!cheb_nodes)
    {
        cerr << "Error: Unable to create nodes.txt!" << endl;
        return 1;
    }

    cheb_nodes << fixed << setprecision(6);
    for (int j = 0; j < n; ++j)
    {
        double xj = cos((2.0 * j + 1) * PI / (2.0 * n)); // cheby chev nodes
        double yj = 1.0 / (1 + 12 * xj * xj);            // values for that nodes through function provided
        cheb_nodes << xj << " " << yj << endl;
    }
    cheb_nodes.close();
    cout << "Chebyshev nodes written to 'nodes.txt'\n"
         << endl; // nodes written

    // === Interpolation ===
    Interpolation uniformInterp; // Giving sample data and interpolating each point between -1 to 1 with 0.01 increment

    ifstream file1("table.txt");
    if (!file1)
    {
        cerr << "Error: Unable to open table.txt!" << endl;
        return 1;
    }

    while (file1 >> uniformInterp.x_input >> uniformInterp.y_input)
    {
        uniformInterp.x_vals.push_back(uniformInterp.x_input);
        uniformInterp.y_vals.push_back(uniformInterp.y_input);
    }
    file1.close();

    ofstream out1("interpolated.txt");
    if (!out1)
    {
        cerr << "Error: Unable to create interpolated.txt!" << endl;
        return 1;
    }

    out1 << fixed << setprecision(6);
    for (double xi = -1.0; xi <= 1.0; xi += 0.01)
    {
        double yi = uniformInterp.lagrangeInterpolation(uniformInterp.x_vals, uniformInterp.y_vals, xi);
        out1 << xi << " " << yi << endl;
    }
    out1.close();
    cout << "Interpolated values saved to 'interpolated.txt'\n";

    // === Chebyshev Interpolation ===
    Interpolation chebInterp;
    ifstream file2("nodes.txt");
    if (!file2)
    {
        cerr << "Error: Unable to open nodes.txt!" << endl;
        return 1;
    }

    while (file2 >> chebInterp.x_input >> chebInterp.y_input)
    {
        chebInterp.x_vals.push_back(chebInterp.x_input);
        chebInterp.y_vals.push_back(chebInterp.y_input);
    }
    file2.close();

    ofstream out2("interpolated2.txt");
    if (!out2)
    {
        cerr << "Error: Unable to create interpolated2.txt!" << endl;
        return 1;
    }

    out2 << fixed << setprecision(6);
    for (double xi = -1.0; xi <= 1.0; xi += 0.01)
    {
        double yi = chebInterp.lagrangeInterpolation(chebInterp.x_vals, chebInterp.y_vals, xi);

        // Protect against numerical explosion
        if (isnan(yi) || isinf(yi))
            yi = 0.0;

        out2 << xi << " " << yi << endl;
    }
    out2.close();
    cout << "Chebyshev interpolated values saved to 'interpolated2.txt'\n";

    return 0;
}
