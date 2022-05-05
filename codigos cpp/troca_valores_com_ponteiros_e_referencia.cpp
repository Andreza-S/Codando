// Usando ponteiros, escreva uma função chamada swap que troca os valores dos seus 2 parâmetros.

#include <iostream>
using namespace std;

void swap(int *p1, int *p2){ 

  int controle = *p1;
  *p1 = *p2;
  *p2 = controle;
  
  cout << *p1 << " Aqui na função o valor de entrada1 foi trocado pelo da entrada2\n";
  cout << *p2 << " Aqui na função o valor de entrada2 foi trocado pelo da entrada1\n";
}

int main() {

  int entrada1, entrada2;
  cout << "Escreva o valor (número inteiro) para a entrada1: "; 
  cin >> entrada1;
  cout << "\nEscreva o valor (número inteiro) para a entrada2: "; 
  cin >> entrada2;

  swap(&entrada1, &entrada2);
  
  cout << entrada1 << " O valor foi trocado na entrada1\n";
  cout << entrada2 << " O valor foi trocado na entrada1\n";

  
  return 0;

}

