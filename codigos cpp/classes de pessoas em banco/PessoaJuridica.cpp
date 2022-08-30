#include "PessoaJuridica.h"

PessoaJuridica::PessoaJuridica(std::string n, std::string nf, std::string rz, int cn) : Pessoa (n) {
  nomeFantasia = nf;
  razaoSocial = rz;
  cnpj = cn;
}

void PessoaJuridica::setNomeFantasia(std::string n) {
  nomeFantasia = n;
}
std::string PessoaJuridica::getNomeFantasia() {
  return nomeFantasia;
}

void PessoaJuridica::setRazaoSocial(std::string rz){
  razaoSocial = rz;
}
std::string PessoaJuridica::getRazaoSocial() {
  return razaoSocial;
}

void PessoaJuridica::setCnpj(int cn) {
  cnpj = cn;
}


int PessoaJuridica::getCnpj() {
  return cnpj;
}