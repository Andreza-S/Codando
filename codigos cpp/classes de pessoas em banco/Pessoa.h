#ifndef PESSOA_H
#define PESSOA_H

#include <string>

class Pessoa {

public:
  Pessoa(std::string);

  void setNome(std::string);
  std::string getNome();

protected:
   std::string nome;
};


#endif