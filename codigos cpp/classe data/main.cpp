//Crie uma Classe Data que inclua 3 partes de informações como atributos - dia (int), mes (int) e ano (int). Sua Classe deve ter um construtor com três parâmetros que utilize os parâmetros para inicializar os 3 membros de dados. Para o propósito deste exercício, assuma que os valores fornecidos para o dia e ano estão corretos, mas certifique-se de que o valor do mês esteja no intervalo 1-12; se não estiver, configure o mês como 1. Forneça uma função set e uma função get para cada membro de dados. Forneça também uma função-membro mostrarData que exiba o dia, o mês e o ano separados por barras (/). Escreva um programa que demonstre as capacidades da sua Classe Date.




#include "Data.h"
#include "Data.h"

using namespace std;


int main() {

  // objeto

  Data objeto(12,1,1990); // mes igual a 1

  cout << objeto.getDia() << "\n";
  cout << objeto.getMes() << "\n";
  cout << objeto.getAno() << "\n";

  objeto.mostrarData();

  // modificando valores de objeto_1 pelos metodos

  objeto.setDia(31);
  cout << objeto.getDia() << "\n";

  objeto.setMes(50); // mes é maior que 12
  cout << objeto.getMes() << "\n";

  objeto.setMes(-23);// mes é menor que 1
  cout << objeto.getMes() << "\n";
  
  objeto.setMes(12); // mes é igual a 12
  cout << objeto.getMes() << "\n";
 
  objeto.setAno(2022);
  cout << objeto.getAno() << "\n";

  objeto.mostrarData();


}