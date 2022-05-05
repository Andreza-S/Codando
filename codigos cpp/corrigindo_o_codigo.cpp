
// Existe algum problema com o código? Que comportamento esperar? Se houver algum erro, corrija. 

//void print(const int ia[10])
//{
// for (int i = 0; i != 10; i++)
//   cout << ia[i] << endl;
//}


// correção do código e aplicação

#include <iostream>
using namespace std;

// na função original estavam faltando as chaves {} após o for,
//dessa forma daria erro, pois os números inseridos dentro do array não seriam impressos
//de forma ordenada como é o intuito da função criada. 

void print(const int ia[10]){
  for (int i = 0; i != 10; i++){
   cout << ia[i] << endl;
  }
}

int main() {
  int k []= {1,2,3,4,5,6,7,8,9,10,8,5,8,6,9,8,7};
  
  print(k);
  
  return 0;  
}