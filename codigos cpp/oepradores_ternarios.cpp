// Operadores Terniários "? :"

#include <iostream>
using namespace std;


int main() {
  // (expressao) ? valor1 : valor2;

  int n1, n2, nota;
  string res;

  cout << "Digite aprimeira nota: ";
  cin >> n1;
  cout << "Digite a segunda nota: ";
  cin >> n2;


  nota = n1+n2;

  // >_60 APROVADO
  // < 60 REPROVADO

  (nota >= 60) ? res="Aprovado" : res="Reprovado"; // aplicacao dos aproreadores ternarios que servem como uma forma de condicionar

  cout << "\nSituacao do aluno: " << res << "\n";

  return 0;
  
}