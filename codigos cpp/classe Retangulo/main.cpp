#include <iostream>
#include "Retangulo.h"
using namespace std;


int main(){
  Retangulo objeto; // sem argumentos

  cout << "Essa é a altura por default do objeto: " << objeto.getAltura() << "\n";
  cout << "Essa é a largura por default do objeto: " << objeto.getLargura() << "\n\n";


  // agora testando os sets com as condções solicitadas

  objeto.setAltura(599); // maior que 20
  objeto.setLargura(78); // maior que 20

  cout << "Essa é a altura dada pelas condições do set objeto: " << objeto.getAltura() << "\n";
  cout << "Essa é a largura dada pelas condições do set do objeto: " << objeto.getLargura() << "\n\n";
  

// vamos colocar os sets menores que 0

  objeto.setAltura(-56); // menor que 0
  objeto.setLargura(-82); // menor que 0

  cout << "Essa é a altura dada pelas condições do set objeto: " << objeto.getAltura() << "\n";
  cout << "Essa é a largura dada pelas condições do set do objeto: " << objeto.getLargura() << "\n\n";


// valores que entre 0 e 20
  objeto.setAltura(5); // menor que 0
  objeto.setLargura(19); // menor que 0
  
  cout << "Essa é a altura dada pelas condições do set objeto: " << objeto.getAltura() << "\n";
  cout << "Essa é a largura dada pelas condições do set do objeto: " << objeto.getLargura() << "\n\n";


// calculando o Perimetro e a Area do objeto

  cout << "Esse é o perimeto do objeto: " << objeto.calculaPerimetro() << "\n";
  cout << "Essa é a area do objeto: " << objeto.calculaAreaRetangulo() << "\n\n";
  
  
}