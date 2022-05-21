// Manipulando condicões

#include <iostream>
using namespace std;

int main() {
  int num;

  /*
  1 2 3 4 5 6 7 8 9 10

  >4 e 7 <*/

  // && - and
  num = 5;
  if (num < 3 && num > 8) {
  cout << "\nValor aceito\n";
  } else {
    cout <<"\n\n Não aceito\n";
  }

  // || - or
  num = 5;
  if (num < 3 || num > 8) {
  cout << "\nValor aceito\n";
  } else {
    cout <<"\n\n Não aceito\n";
  }

  return 0;
}