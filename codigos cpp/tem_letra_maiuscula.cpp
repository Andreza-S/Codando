//Escreva uma função que determina se uma string C++ contém alguma letra maiúscula.

#include <iostream>
#include <cctype>
using namespace std;


void verificaMaiuscula(string guardaString){
  bool temMaiuscula = false;
  
  for (int i = 0; i < guardaString.length(); i++){
    char caracter = guardaString[i];    
    if (isupper(caracter)){
      temMaiuscula = true;
    }
  }
  
  if (temMaiuscula == true){
    cout << "Essa palavra TEM letra maiuscula";
  } else {
    cout << "Essa palavra NÃO tem letra maiúscula";  
  }
} 

int main() {
  
  string guardaString;
  cout << "Digite uma frase ou palavra: ";
  cin >> guardaString;

  verificaMaiuscula(guardaString);

  
  return 0;
    
}