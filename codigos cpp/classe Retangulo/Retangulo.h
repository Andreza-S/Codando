//impede que múltiplas inclusões ocorram
#ifndef RETANGULO_H
#define RETANGULO_H

class Retangulo 
{
public:
  Retangulo(double = 1.0, double = 1.0 ); 

  //funções set
  void setAltura(double);
  void setLargura(double);
  double calculaPerimetro();
  double calculaAreaRetangulo();


  //funções get
  double getAltura();
  double getLargura();


private:
double altura;
double largura;

};

#endif