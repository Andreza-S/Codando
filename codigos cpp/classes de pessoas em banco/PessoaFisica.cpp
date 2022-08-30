#include "PessoaFisica.h"

PessoaFisica::PessoaFisica(std::string n, int c) : Pessoa (n) {
  
}

void PessoaFisica::setCPF(int c) {
  cpf = c;
}
int PessoaFisica::getCPF() {
  return cpf;
}
