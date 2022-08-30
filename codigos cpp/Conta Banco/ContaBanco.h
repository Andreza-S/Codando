//Crie uma Classe chamada ContaBanco que um banco poderia utilizar para representar contas bancárias dos clientes. Sua classe deve incluir um membro de dados do tipo double para representar o saldo da conta. Sua Classe deve fornecer um construtor que recebe um saldo inicial e o utiliza para inicializar o membro de dados. O construtor deve validar o saldo inicial para assegurar que ele seja maior ou igual a zero. Caso seja menor que zero, o construtor simplesmente deverá setar o saldo para zero. A classe deve fornecer três funções-membro. A função-membro creditar deve adicionar uma quantia passada como argumento ao saldo atual. A função-membro debitar deve deve retirar a quantia passada como argumento da conta. Se houver tentativa de retirar um valor acima do saldo, então o saldo deverá permanecer inalterado e a função-membro deverá exibir uma mensagem de erro na tela. A função-membro getSaldo deve retornar o saldo atual. Escreva uma programa que cria dois objetos ContaBanco e testa suas funções-membro.
#ifndef CONTABANCO_H
#define CONTABANCO_H

#include <iostream>
using namespace std;

class ContaBanco
{

  public:

  //Construtor
  ContaBanco(double saldoInicial);

  // metodos

    void setCreditar(double creditar);//A função-membro creditar deve adicionar uma quantia passada como argumento ao saldo atual.

    void setDebitar(double debitar);//A função-membro debitar deve deve retirar a quantia passada como argumento da conta

    double getSaldo();//A função-membro getSaldo deve retornar o saldo atual.

  private:
  // atributos
    double saldoConta;

};

#endif