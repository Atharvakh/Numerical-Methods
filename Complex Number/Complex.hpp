#include <iostream>
#include <complex>

class Complex
{
private:
    double real, imag;

public:
    Complex();
    Complex(const double x, const double y);
    Complex(const Complex &c);
    double getReal() const;
    double getImag() const;
    void set(const double x, const double y);
    Complex operator+(const Complex &c) const;
    Complex operator-(const Complex &c) const;
    Complex operator*(const Complex &c) const;
    Complex operator%(const Complex &c) const;
    Complex conj() const;
    double norm() const;
    friend std::ostream &operator<<(std::ostream &os, const Complex &c);
};