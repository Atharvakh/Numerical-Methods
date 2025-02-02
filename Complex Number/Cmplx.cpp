#include "Complex.hpp"
using namespace std;
int main()
{
    // Create
    Complex c1(5.0, 4.0); // 3 + 4i
    Complex c2(6.0, 2.0); // 1 + 2i
    cout << "Complex Number 1: " << c1;
    cout << "Complex Number 2: " << c2;

    // Add
    Complex sum = c1 + c2;
    cout << "Sum: " << sum;

    // Subtract
    Complex diff = c1 - c2;
    cout << "Difference: " << diff;

    // Multiply
    Complex prod = c1 * c2;
    cout << "Product: " << prod;

    Complex div = c1 % c2;
    cout << "Division: " << div;

    Complex conjugate1 = c1.conj();
    cout << "Conjugate of c1: " << conjugate1;

    Complex conjugate2 = c2.conj();
    cout << "Conjugate of c2: " << conjugate2;

    double norm1 = c1.norm();
    cout << "Norm of c1: " << norm1 << endl;

    double norm2 = c2.norm();
    cout << "Norm of c2: " << norm2;

    return 0;
}
