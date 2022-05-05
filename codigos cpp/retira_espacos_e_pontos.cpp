// manipulação de string, retira pontos e espaços em branco em uma frase

#include <iostream>
using namespace std;

int main() {
  
  string frase;
  getline(cin,frase);

  for(int a=0; a<frase.size(); a++){
    if(!ispunct(frase[a]) and (!isblank(frase[a]))){
      cout << frase[a];
    }
  }   
  
  return 0;
}