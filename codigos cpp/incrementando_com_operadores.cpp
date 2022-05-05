// Alterando os valores de variaveis através do incremento por operadores matematicos

#include <iostream>
using namespace std;

int main() {

  int n1,n2;

  n1=0;
  n2=10;

  cout << n1 << " Esse é o valor inicial\n\n";
  
//Incrementando dos valores das variaveis, realiza a operação matematica e guarda na propria variavel o valor final pós oeparacão
  
  n1 = n1+1;
  cout << n1 << " Esse valor é depois do incremento\n\n";

// essa forma é cumprimida de se fazer o incremento
  n1+=1;
  cout << n1 << " Esse valor é depois do incremento\n\n";


// podemos subtrair também
  n1-=1;
  cout << n1 << " Esse valor é depois do incremento\n\n";

// também podemos incrementar 1 dessa forma
  n1++;
  cout << n1 << " Esse valor é depois do incremento\n\n";

// também podemos incrementar 1 dessa forma
  n1--;
  cout << n1 << " Esse valor é depois do incremento\n\n";


// aqui se multiplica
  n1*=5;
  cout << n1 << " Esse valor é depois do incremento\n\n";


// aqui se divide
  n1/=2;
  cout << n1 << " Esse valor é depois do incremento\n\n";
  

// formas de incrementar no cout, há diferenças no valor impresso

  cout << n1++ <<" " <<  n1 <<" " << ++n1;
  
 return 0;
}