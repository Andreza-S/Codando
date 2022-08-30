#include "Funcionario.h"

Funcionario::Funcionario(std::string n, int cp,int mat, int sala) : PessoaFisica (n, cp) {
  matricula = mat;
  salario = sala;
}

void Funcionario::setMatricula(int mat) {
  matricula = mat;
}
int Funcionario::getMatricula() {
  return matricula;
}

void Funcionario::setSalario(int sal) {
  salario = sal;
}
int Funcionario::getSalario() {
  return salario;
}