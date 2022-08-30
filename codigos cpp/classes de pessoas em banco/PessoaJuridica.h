#ifndef PESSOA_JURIDICA_H
#define PESSOA_JURIDICA_H

#include "Pessoa.h"

#include <string>

class PessoaJuridica : public Pessoa {

public:
  PessoaJuridica(std::string, std::string, std::string, int);

  void setNomeFantasia(std::string);
  std::string getNomeFantasia();

  void setRazaoSocial(std::string);
  std::string getRazaoSocial();

  void setCnpj(int);
  int getCnpj();

private:
  std::string nomeFantasia;
  std::string razaoSocial;
  int cnpj;
};
#endif