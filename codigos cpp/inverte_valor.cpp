// Invertendo um  valor de uma variavell int

#include <iostream>
using namespace std;


int main() {

  int num=10;
  cout << num << " VALOR ORIGINAL\n\n";


  //inventer o valor de uma variavel
  num = num * -1;
  cout << num << " Após a inversão\n\n";

  //outras maneiras
  
  //aqui nao inverte na variavel, apenas para impressao
    cout << -num << " Após a inversão\n\n";

  //para gravar na variavel
  num=-num;
  cout << num << " Após a inversão\n\n";
  
  

