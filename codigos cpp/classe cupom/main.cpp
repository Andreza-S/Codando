//Crie uma Classe chamada Cupom que uma loja de suprimentos de informática possa utilizar para representar um cupom de um item vendido na loja. Um Cupom deve incluir quatro membros de dados - id (string), descrição (string), quantidade (int) e o preço do item (float). Sua Classe deve ter um construtor que inicializa os 4 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Além disso, forneça uma função-membro chamada de calculaCupom que calcula o valor total da nota e depois retorna esse valor. Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço do item não for positivo, ele deve ser configurado com 0. Escreva uma programa para ilustrar as capacidades de sua Classe Cupom.

#include "Cupom.h"
#include "Cupom.h"

using namespace std;


int main() {


  // Criando o objeto cupomChocolate

  Cupom cupomChocolate;
  
  cout << "\n\n----------IMPRESSAO DOS DADOS INICIALIZADOS PELO CONSTRUTOR------\n\n";
  cout << "Essa é a nota do cupom: \n";
  cout << cupomChocolate.getId() << "\n";
  cout << "Essa é a descricao: \n";
  cout << cupomChocolate.getDescricao() << "\n";
  cout << "Esse é a quantidade de itens: \n";
  cout << cupomChocolate.getQuantidade() << "\n";  
  cout << "Esse é o preco do item: \n";
  cout << cupomChocolate.getPrecoDoItem() << "\n";
  cout << "Esse é o valor final do cupom: " << cupomChocolate.calculaCupom();



  // alterando os dados através dos metodos
  cupomChocolate.setId("CupomChocolateShow");
  cupomChocolate.setDescricao("Esse cupom serve para você ter um descontão na compra de CHOCOLATES a sua escolha, aproveite!");
  cupomChocolate.setQuantidade(25); // valor > 0
  cupomChocolate.setPrecoDoItem(3.39); // valor > 0

  // impressao dos DADOS ATUALIZADOS
  
  cout << "\n\n----------IMPRESSAO DOS DADOS ATUALIZADOS 1------\n\n";
  cout << "Essa é a nota do cupom: \n";
  cout << cupomChocolate.getId() << "\n";
  cout << "Essa é a descricao: \n";
  cout << cupomChocolate.getDescricao() << "\n";
  cout << "Esse é a quantidade de itens: \n";
  cout << cupomChocolate.getQuantidade() << "\n";  
  cout << "Esse é o preco do item: \n";
  cout << cupomChocolate.getPrecoDoItem() << "\n";
  cout << "Esse é o valor final do cupom: " << cupomChocolate.calculaCupom();


  // impressão com os valores de quantidade e preco negativos
  
  cupomChocolate.setQuantidade(-25); // valor < 0
  cupomChocolate.setPrecoDoItem(-3.39); // valor < 0

  cout << "\n\n----------IMPRESSAO DOS DADOS ATUALIZADOS 2------\n\n";
  cout << "Essa é a nota do cupom: \n";
  cout << cupomChocolate.getId() << "\n";
  cout << "Essa é a descricao: \n";
  cout << cupomChocolate.getDescricao() << "\n";
  cout << "Esse é a quantidade de itens: \n";
  cout << cupomChocolate.getQuantidade() << "\n";  
  cout << "Esse é o preco do item: \n";
  cout << cupomChocolate.getPrecoDoItem() << "\n";
  cout << "Esse é o valor final do cupom: " << cupomChocolate.calculaCupom();
  
}