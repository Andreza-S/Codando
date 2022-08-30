#ifndef FUNCIONAIRO_H
#define FUNCIONAIRO_H

#include "PessoaFisica.h"

#include <string>

class Funcionario : public PessoaFisica {

public:
  Funcionario(std::string, int,int, int );

  void setMatricula(int);
  int getMatricula();

  void setSalario(int);
  int getSalario();

protected:
  int matricula, salario;
};
#endif