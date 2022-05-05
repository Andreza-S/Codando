#include <iostream>
using namespace std;

// variaveis globais: podem ser acessadas em qualquer local do programa
int n1,n2;

int main() {

// Operadores Matemáticos: + - / * % ()

  int n3,n4; // variaveis locais: são acessadas somentes dnetro do escopo ao qual elas pertencem

  int res;

  n1= 11;
  n2= 3;
  n3= 5;
  n4= 2;

  res= n1+n2+n3+n4;

  cout << "Essa é a soma de todas as varaiveis: " << res << "\n";


  res = (n1+n2+n3+n4) - 10; 
  cout << "Essa é a subtração dos valores: " << res << "\n";


  res = n1+n2*n4;

  cout << "Essa é o resultado da operação de soma e multiplicação consecultivas dos valores: " << res << "\n";


  int res2 = n1/n2;
  int res3 = n1%n2;

  cout << "Essa é o resultado da operação de divisao dos valores: " << res2 << "\n";

  cout << "Essa é o resultado da operação de resto de uma divisao valores: " << res3 << "\n";

  
  
  

  
  return 0;
}