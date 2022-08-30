#include "Cliente.h"


  Cliente::Cliente(std::string n, int cp,int tele, std::string ende): PessoaFisica (n, cp) {
    telefone = tele;
    endereco = ende;
  }

  void Cliente::setTelefone(int tele) {
    telefone = tele;
  }
  int Cliente::getTelefone() {
    return telefone;
  }

  void Cliente::setEndereco(std::string ende) {
    endereco = ende;
    
  }
  std::string Cliente::getEndereco() {
    return endereco;
  }

