//Crie uma Classe chamada Empregado que possui 3 membros de dados - um nome, um sobrenome e um salário mensal. Sua Classe deve ter um construtor que inicialize os 3 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Se o salário mensal não for positivo, configure-o como 0. Escreva um programa de teste que demonstre as capacidade da classe Empregado. Crie dois objetos Empregado e exiba seu salário mensal. Em seguida, dê um aumento de 10% para cada um dos empregados e exiba novamente o salário mensal.


#ifndef EMPREGADO_H
#define EMPREGADO_H

#include <iostream>
using namespace std;

class Empregado
{

  public:

  //Construtor
    Empregado();

  // metodos

    void setNome(string nome);//A função-membro SetNome deve adicionar uma string passada como argumento ao nome.

    void setSobrenome(string sobrenome);//A função-membro setSobrenome adicionar uma string passada como argumento ao sobrenome.

    void setSalarioMensal(double salario_mensal);//A função-membro setSalarioMensal deve deve adicinar a quantia passada como argumento ao salario_mensal

    string getNome();//A função-membro getNome deve retornar o nome.
    string getSobrenome();//A função-membro getSobrenome deve retornar o sobrenome.
    double getSalarioMensal();//A função-membro getSalarioMensal deve retornar o salario_mensal.

  private:
  // atributos
    string nome;
    string sobrenome;
    double salario_mensal;

};

#endif