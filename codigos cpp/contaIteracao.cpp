// Recebe o número de execuções do programa do usuário
// e imprime a contagem de cada interação

#include <iostream>
using namespace std;

int qtd_de_execoes;

int main(){

  cout << "Digite a quantidade de execuções: ";
  cin >> qtd_de_execoes;

  for (int i = 0; i < qtd_de_execoes; i++) {    
    cout << "Interação: " << i << "\n\n";  
  }
  return 0;
}

  