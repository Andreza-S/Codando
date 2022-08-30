#ifndef COMPLEX_H
#define COMPLEX_H

class Complex 
{
public:
  Complex( int a = 0, int b = 0)
  {
    real = a;
    imaginaria = b;
  }

  void soma(const Complex &);

  void sub(const Complex &);

  void print();

private:
  double real;
  double imaginaria;
};

#endif