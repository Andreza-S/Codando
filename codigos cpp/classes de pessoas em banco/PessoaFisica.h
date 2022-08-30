#ifndef PESSOA_FISICA_H
#define PESSOA_FISICA_H

#include "Pessoa.h"

#include <string>

class PessoaFisica : public Pessoa {

public:
  PessoaFisica(std::string, int);


  void setCPF(int);
  int getCPF();

protected:
  int cpf;
};
#endif