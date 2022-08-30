// imprime:
//*****
// ****
//  ***
//   **
//    *

#include <iostream>

int main() {
  int limite = 5;
  int contador;
  char asterisco = '*';

  int i;
  
  for (contador = 1; contador < limite+1; contador++){
    
    for (i = 0; i < contador; i++) {
      std::cout << asterisco;       
    }
    std::cout << '\n';

  }

}
#include <iostream>
using namespace std;
int main() {

  for(int i=1;i<=5;i++){
    for(int s=1;s < i; s++){
      cout << " "; 
    }
    
    for(int a=4;a >= i; a--){
      cout << "*"; 
    }
    
    cout << "*" << endl;
  }
  
  return 0;
}