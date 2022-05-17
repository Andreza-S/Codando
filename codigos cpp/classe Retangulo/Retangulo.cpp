#include <iostream>
#include "Retangulo.h"
using namespace std;


// Construtor

Retangulo::Retangulo(double alt, double larg){
  
  altura = alt;
  largura = larg;
}


// Funcões Set

void Retangulo::setAltura(double alt){
  if (alt > 0 && alt < 20){
    altura = alt;
  }
  else{
    altura = 1;
  }
}

void Retangulo::setLargura(double larg){
  if (larg > 0 && larg < 20){
    largura = larg;
  }
  else{
    largura = 1; 
  }

}

//funções get
double Retangulo::getAltura(){
  return altura;
  
}
double Retangulo::getLargura(){
  return largura;
}

// Funcoes calcula Perimetro e Area

double Retangulo::calculaPerimetro(){
  double perimetro = 2*(getAltura() + getLargura());
  return perimetro;
}


double Retangulo::calculaAreaRetangulo(){
  double area = getAltura() * getLargura();
  return area;
}

