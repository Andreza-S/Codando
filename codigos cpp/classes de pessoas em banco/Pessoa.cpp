#include "Pessoa.h"


Pessoa::Pessoa(std::string n) {
  nome = n;
}

void Pessoa::setNome(std::string n){
  nome = n;
}

std::string Pessoa::getNome() {
  return nome;
}