// Crie uma Classe Data que inclua 3 partes de informações como atributos - dia (int), mes (int) e ano (int). Sua Classe deve ter um construtor com três parâmetros que utilize os parâmetros para inicializar os 3 membros de dados. Para o propósito deste exercício, assuma que os valores fornecidos para o dia e ano estão corretos, mas certifique-se de que o valor do mês esteja no intervalo 1-12; se não estiver, configure o mês como 1. Forneça uma função set e uma função get para cada membro de dados. Forneça também uma função-membro mostrarData que exiba o dia, o mês e o ano separados por barras (/). Escreva um programa que demonstre as capacidades da sua Classe Date.

#ifndef DATA_H
#define DATA_H

#include <iostream>
using namespace std;

class Data
{

  public:

  //Construtor
    Data(int inicia_dia, int inicial_mes, int   inicia_ano);

  // metodos

    void setDia(int inicia_dia);//A função-membro setDia deve adicionar uma string passada como argumento ao dia.

    void setMes(int inicia_mes);//A função-membro setMes adicionar uma string passada como argumento ao mes.

    void setAno(int inicia_ano);//A função-membro setAno deve deve adicinar a quantia passada como argumento ao ano.

    int getDia();//A função-membro getDia deve retornar o dia.
    int getMes();//A função-membro getMes deve retornar o mes.
    int getAno();//A função-membro getAno deve retornar o ano.

    void mostrarData(); //Imprime na tela da data cmpleta com dia/mes/ano.
  
  private:
  // atributos
    int dia;
    int mes;
    int ano;

};

#endif