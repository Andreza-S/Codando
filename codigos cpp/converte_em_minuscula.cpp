//Escreva uma função que receba uma string C++ e converta cada letra para minúscula.

#include <iostream>
#include <cctype>
using namespace std;

void palavraMaiuscula (string palavraRecebida){

  string palavraFinal;

  for (int i =0; i < palavraRecebida.length(); i++){
    char caracter = palavraRecebida[i];

    if (islower(caracter)){ // Caso a letra seja minuscula
      palavraFinal += toupper(caracter); // Converte para maiuscula e atribui a variavel final
    }else{ // caso a letra seja maiuscula
      palavraFinal += caracter; // adiciona diretamete na variavel final
    }
  }
  
  cout << "É assim que a palavra final fica: " << palavraFinal;
  
}

int main() {


  string palavraRecebida;
  cout << "Escreva uma palavra sem espaços: ";
  cin >> palavraRecebida;

  palavraMaiuscula(palavraRecebida);
  
  return 0;
    
}