//Crie uma Classe chamada Empregado que possui 3 membros de dados - um nome, um sobrenome e um salário mensal. Sua Classe deve ter um construtor que inicialize os 3 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Se o salário mensal não for positivo, configure-o como 0. Escreva um programa de teste que demonstre as capacidade da classe Empregado. Crie dois objetos Empregado e exiba seu salário mensal. Em seguida, dê um aumento de 10% para cada um dos empregados e exiba novamente o salário mensal.


#include <iostream>
using namespace std;

#include "Empregado.h"

//Implementação

//construtor

Empregado::Empregado()  
{
  nome = "PRECISO DE UM NOME";
  sobrenome = "PRECISO DE UM SOBRENOME";
  salario_mensal = 0;
  
}

  
// metodos


//A função-membro SetNome deve adicionar uma string passada como argumento ao nome.
void Empregado::setNome(string nome_inicia){
  nome = nome_inicia;
}


//A função-membro setSobrenome adicionar uma string passada como argumento ao sobrenome.

void Empregado::setSobrenome(string sobrenome_inicia){
  sobrenome = sobrenome_inicia;
}



//A função-membro setSalarioMensal deve deve adicinar a quantia passada como argumento ao salario_mensal
void Empregado::setSalarioMensal(double salario_mensal_inicia){
    if (salario_mensal_inicia < 0)
  {
    salario_mensal = 0;
  }
  else{
    salario_mensal = salario_mensal_inicia;
  }

}

//A função-membro getNome deve retornar o nome.
string Empregado::getNome(){
  return nome;
}



//A função-membro getSobrenome deve retornar o sobrenome.
string Empregado::getSobrenome(){
  return sobrenome;
}



//A função-membro getSalarioMensal deve retornar o salario_mensal.
double Empregado::getSalarioMensal(){
  return salario_mensal;
}