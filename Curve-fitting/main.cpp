#include "curve_fit.hpp"
#include <fstream>

int main()
{
    curve_fit C;
    curve_fit P;
    curve_fit E;

    ifstream file("table.txt");
    if (!file)
    {
        cerr << "Error: Unable to open data file!" << endl;
        return 1;
    }

    // Read data points from file
    while (file >> C.x_input >> C.y_input)
    {
        C.x.push_back(C.x_input);
        C.y.push_back(C.y_input);
    }
    file.close();

    // Copy data to P
    P.x = C.x;
    E.x = C.x;
    P.y = C.y;
    E.y = C.y;

    C.leastSquaresFit(C.x, C.y, C.a, C.b);

    C.parabolaFit(P.x, P.y, P.a, P.b, P.c);

    C.exponentialFit(E.x, E.y, E.A, E.B);

    double rms1 = C.calculateRMS(C.x, C.y, C.a, C.b);
    double rms2 = P.calculateRMS(P.x, P.y, P.a, P.b, P.c);
    double rms3 = E.calculateERMS(E.x, E.y, E.A, E.B);

    cout << "Best fit line: y = " << C.a << "x + " << C.b << endl;
    cout << "RMS Error: " << rms1 << endl;

    cout << "Best parabola fit: y = " << P.a << "x^2 + " << P.b << "x + " << P.c << endl;
    cout << "RMS Error: " << rms2 << endl;

    cout << "Best exponential fit: y = " << E.A << " * e^(" << E.B << " * x)" << endl;
    cout << "RMS Error: " << rms3 << endl;

    return 0;
}
