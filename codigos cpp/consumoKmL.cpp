#include <iostream>
using namespace std;
int main() {
  
  int soma = 0, qtd_paradas=0;

    while(true){
    int km_pecorrido, qtd_litros; 
    cout << "Digite os km pecorridos: " ; 
    cin >> km_pecorrido;   
    if(km_pecorrido == -1) break; 
    cout << "Digite a quantidade de litros utilizada: ";
    cin >> qtd_litros;
      
    int consumo = km_pecorrido/qtd_litros;
    cout << "O consumo foi de: " << consumo <<"km/l" << endl;
      
    soma += qtd_litros;
    qtd_paradas += 1;
    cout << "Até a " << qtd_paradas << "a parada," <<"você consumiu um total de " << soma << " litros" << endl; 
  }
  
  return 0;
}