//Crie uma Classe chamada Cupom que uma loja de suprimentos de informática possa utilizar para representar um cupom de um item vendido na loja. Um Cupom deve incluir quatro membros de dados - id (string), descrição (string), quantidade (int) e o preço do item (float). Sua Classe deve ter um construtor que inicializa os 4 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Além disso, forneça uma função-membro chamada de calculaCupom que calcula o valor total da nota e depois retorna esse valor. Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço do item não for positivo, ele deve ser configurado com 0. Escreva uma programa para ilustrar as capacidades de sua Classe Cupom.

#ifndef CUPOM_H
#define CUPOM_H

#include <iostream>
using namespace std;

class Cupom
{

  public:

  //Construtor
    Cupom();

  // metodos

    void setId(string id_inicia);//A função-membro setId deve adicionar uma string passada como argumento ao id.

    void setDescricao(string descricao_inicia);//A função-membro setDescricao adicionar uma string passada como argumento a descricao.

    void setQuantidade(int quantidade_inicia);//A função-membro setQuantidade deve deve adicinar a quantia passada como argumento a quantidade.

    void setPrecoDoItem(float precoDoItem_inicia);//A função-membro setPrecoDoItem deve deve adicinar a quantia passada como argumento ao precoDoItem.

    string getId();//A função-membro getId deve retornar o id.
    string getDescricao();//A função-membro getDescricao deve retornar a descricao.
    int getQuantidade();//A função-membro getQuantidade deve retornar o quantidade.

    float getPrecoDoItem(); //A função-membro getPrecoDoItem deve retornar o precoDoItem.

  float calculaCupom(); //retorna o calculo do valor do cupom total
  
  private:
  // atributos
    string id;
    string descricao;
    int quantidade;
    float precoDoItem;
};

#endif