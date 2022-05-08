// Crie uma Classe Data que inclua 3 partes de informações como atributos - dia (int), mes (int) e ano (int). Sua Classe deve ter um construtor com três parâmetros que utilize os parâmetros para inicializar os 3 membros de dados. Para o propósito deste exercício, assuma que os valores fornecidos para o dia e ano estão corretos, mas certifique-se de que o valor do mês esteja no intervalo 1-12; se não estiver, configure o mês como 1. Forneça uma função set e uma função get para cada membro de dados. Forneça também uma função-membro mostrarData que exiba o dia, o mês e o ano separados por barras (/). Escreva um programa que demonstre as capacidades da sua Classe Date.

#include <iostream>
using namespace std;

#include "Data.h"

//Implementação

//construtor

Data::Data(int inicia_dia, int inicial_mes, int   inicia_ano)  
{
  dia = inicia_dia;
  mes = inicial_mes;
  ano = inicia_ano;
  
}

// metodos

//A função-membro setDia deve adicionar uma string passada como argumento ao dia.
void Data::setDia(int inicia_dia){
  dia = inicia_dia;
}


//A função-membro setMes adicionar uma string passada como argumento ao mes.
void Data::setMes(int inicia_mes){
  if ((inicia_mes >= 1) and (inicia_mes <= 12)){
    mes = inicia_mes;
  } else{
    mes = 1;
  }
}


//A função-membro setAno deve deve adicinar a quantia passada como argumento ao ano.
void Data::setAno(int inicia_ano){
  ano = inicia_ano;
}


//A função-membro getDia deve retornar o dia.
int Data::getDia(){
  return dia;
}

  
//A função-membro getMes deve retornar o mes.  
int Data::getMes(){
  return mes;
}

  
//A função-membro getAno deve retornar o ano.  
int Data::getAno(){
  return ano;
}


//Imprime na tela da data cmpleta com dia/mes/ano.
void Data::mostrarData(){
  cout << dia << "/" << mes << "/" << ano << "\n\n";
} 
  