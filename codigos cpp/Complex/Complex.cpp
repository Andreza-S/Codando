#include <iostream>
using std::cout, std::endl;

#include "Complex.h"

void Complex::soma(const Complex &c)
{
  real += c.real;
  imaginaria += c.imaginaria;
}

void Complex::sub(const Complex &c)
{
  real -= c.real;
  imaginaria -= c.imaginaria;
}

void Complex::print()
{
  cout << real << (imaginaria >= 0 ? " +" : " ") << imaginaria << "*i" << endl;
}