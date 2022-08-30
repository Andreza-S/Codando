#include <iostream>
#include <cmath>
using namespace std;

int main() {


  int palito_1;
  int palito_2;
  int palito_3;

  cout << " escreva o tamanho do palito 1 :";
  cin >> palito_1;
    cout << " escreva o tamanho do palito 2 :";
  cin >> palito_2;
    cout << " escreva o tamanho do palito 3 :";
  cin >> palito_3;

  if (palito_1 + palito_2 > palito_3){
    // eh triangulo
    cout << " É triangulo";
  }
 else if(palito_1 + palito_3 > palito_2){
  // eh triangulo
    cout << " É triangulo";  
  }
  else if(palito_2 + palito_3 > palito_1){
    // eh triangulo
    cout << " É triangulo";  
  }
  else{
    cout << " Não é triangulo";
  }


}