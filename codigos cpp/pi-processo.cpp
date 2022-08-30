#include <iostream>
#include <cmath>
using namespace std;


int main() {
  double divisor = 3;
  double pi = 4;

  for (int i = 0; i < 10; i++){
    if (i == 0){
      cout << "Execução " << i << "\n" << " e o valor de pi é: " << pi << "\n";
    }
    else if (i % 2 == 0) {
    divisor += 2;
    pi = pi + (4/divisor);
    cout << "Execução " << i << "\n" << " e o valor de pi é: " << pi << "\n"; 
    } else{
    divisor += 2;
    pi = pi - (4/divisor);
    cout << "Execução " << i << "\n" << " e o valor de pi é: " << pi << "\n"; 
    }
  }
}