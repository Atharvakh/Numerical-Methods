#include "Complex.hpp"
#include <cmath>

Complex::Complex() : real(0.0), imag(0.0) {}
Complex::Complex(const double x, const double y) : real(x), imag(y) {}
Complex::Complex(const Complex &c) : real(c.getReal()), imag(c.getImag()) {}
double Complex::getReal() const
{
    return real;
}

double Complex::getImag() const
{
    return imag;
}

Complex Complex::operator+(const Complex &c) const
{
    return Complex(real + c.getReal(), imag + c.getImag());
}
Complex Complex::operator-(const Complex &c) const
{
    return Complex(real - c.getReal(), imag - c.getImag());
}
Complex Complex::operator*(const Complex &c) const
{
    double x = (real * c.getReal()) - (imag * c.getImag());
    double y = (real * c.getImag()) + (imag * c.getReal());
    return Complex(x, y);
}

Complex Complex::operator%(const Complex &c) const
{
    double denominator = c.getReal() * c.getReal() + c.getImag() * c.getImag();
    double x = (real * c.getReal() + imag * c.getImag()) / denominator;
    double y = (imag * c.getReal() - real * c.getImag()) / denominator;
    return Complex(x, y);
}
std::ostream &operator<<(std::ostream &os, const Complex &c)
{
    os << c.getReal() << " + i (" << c.getImag() << ")" << std::endl;
    return os;
}
Complex Complex::conj() const
{
    return Complex(real, -imag);
}
double Complex::norm() const
{
    return sqrt(real * real + imag * imag);
}
