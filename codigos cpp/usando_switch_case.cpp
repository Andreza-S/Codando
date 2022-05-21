// Switch/Case

#include <iostream>
using namespace std;

int main() {
  /*
  SINTAXE

  switch (expressao) {
    case const1;
      comandos;
      break;
    case const1;
      comandos;
      break;
    default:
      comandos;
  }
  */

  int val;

  cout << "Selecione um cor:\n";
  cout << "1- Verde, 2- Azul, 3- Vermelho\n";
 
  cin >> val;

  switch(val) {
    case 1:
      cout << "Cor selecionada: Verde\n";
      break;
    case 2:
      cout << "Cor selecionada: Azul\n";
      break;
    case 3:
      cout << "Cor selecionada: Vermelho\n";
      break;
    default:
      cout << "Cor selecionada é inválida\n";
  }

  cout << "\nPrograma1 finalizado\n";


  // outra forma
  cout << "\n\nSelecione um cor:\n";
  cout << "1,2 ou 3 para Verde; 4,5 ou 6 para Vermelho\n";
 
  cin >> val;

  switch(val) {
    case 1:
    case 2:
    case 3:
      cout << "Cor selecionada: Verde\n";
      break;
    case 4:
    case 5:
    case 6:
      cout << "Cor selecionada: Vermelho\n";
      break;
    default:
      cout << "Cor selecionada é inválida\n";
  }

  cout << "\nPrograma2 finalizado\n\n";


  // aninhamento


  cout << "\n\nSelecione um transporte:\n";
  cout << "1 - Carro , 2 - Moto , 3 - Aviao, 4 - Helicoptero\n";
 
  cin >> val;

  switch(val) {
    case 1:
    case 2:
      cout << "Transporte do tipo terrestre\n";
      switch(val) {
        case1:
          cout << "Carro selecionado";
          break;
        case2:
          cout << "Moto selecionada";
          break;
      }
    case 3:
    case 4:
      cout << "Transporte aereo\n";
      switch (val) {
        case3:
          cout << "Aviao selecionado";
          break;
        case4:
          cout << "Helicoptero selecionado";
          break;
      }
      
    default:
      cout << "Transporte selecionado é inválido\n";
  }

  cout << "\nPrograma3 finalizado\n\n";

  

  
  
  return 0;
  
}