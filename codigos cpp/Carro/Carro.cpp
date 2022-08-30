#include <iostream>
using std::cout, std::endl;

#include "Carro.h"
//Implementação

Carro::Carro(string nome, int ano)
{
  marca = nome;
  anoCarro = ano;
  
}

void Carro::setMarca(string nome)
{
  marca = nome;
}

void Carro::setAno(int ano) // set ano
{
  anoCarro = ano;
}

string Carro::getMarca()
{
  return marca;
}

int Carro::getAno() // get ano
{
  return anoCarro;
}


void Carro::displayMessage()
{
  std::cout << "Olá, eu sou um carro da marca " << getMarca() << " e sou do ano de " << getAno();
}
