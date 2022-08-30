#ifndef CLIENTE_H
#define CLIENTE_H

#include "PessoaFisica.h"

#include <string>

class Cliente : public PessoaFisica {

public:
  Cliente(std::string n, int cp,int tele, std::string ende);

  void setTelefone(int);
  int getTelefone();

  void setEndereco(std::string);
  std::string getEndereco();

protected:
  int telefone;
  std::string endereco;
};
#endif