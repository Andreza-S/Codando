//Crie uma Classe chamada ContaBanco que um banco poderia utilizar para representar contas bancárias dos clientes. Sua classe deve incluir um membro de dados do tipo double para representar o saldo da conta. Sua Classe deve fornecer um construtor que recebe um saldo inicial e o utiliza para inicializar o membro de dados. O construtor deve validar o saldo inicial para assegurar que ele seja maior ou igual a zero. Caso seja menor que zero, o construtor simplesmente deverá setar o saldo para zero. A classe deve fornecer três funções-membro. A função-membro creditar deve adicionar uma quantia passada como argumento ao saldo atual. A função-membro debitar deve deve retirar a quantia passada como argumento da conta. Se houver tentativa de retirar um valor acima do saldo, então o saldo deverá permanecer inalterado e a função-membro deverá exibir uma mensagem de erro na tela. A função-membro getSaldo deve retornar o saldo atual. Escreva uma programa que cria dois objetos ContaBanco e testa suas funções-membro.

#include "ContaBanco.h"
#include "ContaBanco.h"
using namespace std;



int main() {
  
  cout << "-----------------------------\n\n";
  cout << "Essa é a execução do Objeto1 \n\n";
 
  //objeto1

  ContaBanco minhaContaBanco(200.00);
  
  minhaContaBanco.setCreditar(600.00);
  
  minhaContaBanco.setDebitar(50.00);
  
  minhaContaBanco.getSaldo();

  cout << "-----------------------------\n\n";
  cout << "Essa é a execução do Objeto2 \n\n";

  //objeto2
  ContaBanco minhaContaBanco2(-20);
  
  minhaContaBanco2.setCreditar(50);
  
  minhaContaBanco2.setDebitar(900);
  
  minhaContaBanco2.getSaldo();

  


  return 0;
}
