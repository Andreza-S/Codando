#ifndef CARRO_H
#define CARRO_H

#include <string>
using std::string;

//Interface
class Carro
{

public:

  Carro(string nome);

  void setMarca(string nome);

  string getMarca();

  void displayMessage();

private:
  string marca;
};

#endif