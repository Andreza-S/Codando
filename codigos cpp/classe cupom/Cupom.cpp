//Crie uma Classe chamada Cupom que uma loja de suprimentos de informática possa utilizar para representar um cupom de um item vendido na loja. Um Cupom deve incluir quatro membros de dados - id (string), descrição (string), quantidade (int) e o preço do item (float). Sua Classe deve ter um construtor que inicializa os 4 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Além disso, forneça uma função-membro chamada de calculaCupom que calcula o valor total da nota e depois retorna esse valor. Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço do item não for positivo, ele deve ser configurado com 0. Escreva uma programa para ilustrar as capacidades de sua Classe Cupom.


#include <iostream>
using namespace std;

#include "Cupom.h"

//Implementação

//construtor

Cupom::Cupom(){
  id = "Preciso de uma ID";
  descricao = "Preciso da descricao do cupom";
  quantidade = 0;
  precoDoItem = 0;  
}


// metodos

//A função-membro setId deve adicionar uma string passada como argumento ao id.
void Cupom::setId(string id_inicia){
  id = id_inicia;
}


//A função-membro setDescricao adicionar uma string passada como argumento a descricao.
void Cupom::setDescricao(string descricao_inicia){
  descricao = descricao_inicia;
}


//A função-membro setQuantidade deve deve adicinar a quantia passada como argumento a quantidade.
void Cupom::setQuantidade(int quantidade_inicia){
  if (quantidade_inicia > 0){
      quantidade = quantidade_inicia;
  }else {
    quantidade = 0;
  }
  
}


//A função-membro setPrecoDoItem deve deve adicinar a quantia passada como argumento ao precoDoItem.
void Cupom::setPrecoDoItem(float precoDoItem_inicia){
  if (precoDoItem_inicia > 0){
      precoDoItem = precoDoItem_inicia;
  }else {
    precoDoItem = 0;
  }
}

//A função-membro getId deve retornar o id.
string Cupom::getId(){
  return id;
}

//A função-membro getDescricao deve retornar a descricao.
string Cupom::getDescricao(){
  return descricao;
}

//A função-membro getQuantidade deve retornar o quantidade.
int Cupom::getQuantidade(){
  return quantidade;
}

//A função-membro getPrecoDoItem deve retornar o precoDoItem.
float Cupom::getPrecoDoItem(){
  return precoDoItem;
} 

//retorna o calculo do valor do cupom total
float Cupom::calculaCupom(){

  // Se a quantidade não for positiva, ela deve ser configurada como 0.
  if (quantidade < 0){
    quantidade = 0;
  }

  //Se o preço do item não for positivo, ele deve ser configurado com 0.
  if (precoDoItem < 0){
    precoDoItem = 0;  
  }
  
  //calcula o valor total da nota e depois retorna esse valor.
  float valor = quantidade * precoDoItem;

  return valor;
  
}