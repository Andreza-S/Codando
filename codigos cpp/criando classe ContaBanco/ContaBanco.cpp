//Crie uma Classe chamada ContaBanco que um banco poderia utilizar para representar contas bancárias dos clientes. Sua classe deve incluir um membro de dados do tipo double para representar o saldo da conta. Sua Classe deve fornecer um construtor que recebe um saldo inicial e o utiliza para inicializar o membro de dados.


//O construtor deve validar o saldo inicial para assegurar que ele seja maior ou igual a zero. Caso seja menor que zero, o construtor simplesmente deverá setar o saldo para zero. 

// A classe deve fornecer três funções-membro. A função-membro creditar deve adicionar uma quantia passada como argumento ao saldo atual. A função-membro debitar deve deve retirar a quantia passada como argumento da conta.

//Se houver tentativa de retirar um valor acima do saldo, então o saldo deverá permanecer inalterado e a função-membro deverá exibir uma mensagem de erro na tela. A função-membro getSaldo deve retornar o saldo atual. Escreva uma programa que cria dois objetos ContaBanco e testa suas funções-membro.

#include <iostream>
using namespace std;

#include "ContaBanco.h"

//Implementação

//construtor

ContaBanco::ContaBanco(double saldoInicial)  
{

  if (saldoInicial >= 0)
  {
  saldoConta = saldoInicial;
  }
  else{
    saldoConta = 0;
  }

}

//metodos


//A função-membro creditar deve adicionar uma quantia passada como argumento ao saldo atual.
void ContaBanco::setCreditar(double creditar)
{
  saldoConta += creditar;
}

//A função-membro debitar deve deve retirar a quantia passada como argumento da conta saldo deverá permanecer inalterado e a função-membro deverá exibir uma mensagem de erro na tela.
void ContaBanco::setDebitar(double debitar)
{
  if (debitar > saldoConta)
  {
    cout << "Essa é uma mensagem de erro porque você tentou retirar um valor maior que o saldo atual da conta \n\n";
  }
  else
  {
    saldoConta -= debitar;
  }
}

//A função-membro getSaldo deve retornar o saldo atual.
double ContaBanco::getSaldo()
{
  cout << "Esse é o saldo da conta " << saldoConta << "\n\n";
  
  return saldoConta;
}

