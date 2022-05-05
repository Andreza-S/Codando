// Usando comandos de decisão IF ELSE

#include <iostream>
using namespace std;

int main() {

  int num = 10;
  int num2 = 50;
  char opc = 's';

  //operadores de comparação: >(maior), <(menor), >=(maior ou igual), <=(menor ou igual), ==(igual), !=(diferente)
  
  //se o teste for verdadeiro(...) comparando com valor 10
  
  if (num > 10) {
    cout << "Valor de num é MAIOR que 10\n\n";
    
  }else if (num < 10) { //se o teste não for verdadeiro tente isso
    cout << "Valor de num é MENOR que 10\n\n";
  }else { // se os teste anteriores forem falso execute isso
    cout << "Valor de num é IGUAL a 10\n\n";
    
  }

  //exemplo 2, comparando com num2

  if (num>num2) {
    cout << "Valor de num é MAIOR que num2\n\n";
  }else if (num<num2){
    cout << "Valor de num é MENOR que num2\n\n";
  }else {
    cout << "Valor de num é IGUAL a num2\n\n";
  }

  
  return 0;
}