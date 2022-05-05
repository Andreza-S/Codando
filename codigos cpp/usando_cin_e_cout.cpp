// Programa para manipulação de variaveis e utilização de cout e cin


#include <iostream>

using namespace std;

int main() {

  // as variaveis foram defenidas
  int vidas;//10,15,2
  char letra; //'B'
  double decimal; //2.4999999999999
  float decimal2; //2.5
  bool vivo; //true ou false
  string nome;//"Vavava"


  // as variaveis foram declaradas e inicializadas

  vidas = 0;
  letra = 'B';
  decimal = 5.2;
  decimal2 = 5.2;
  vivo = true;
  nome = "Vava";


  cout << vidas << "\n";
  cout << letra << "\n";
  cout << decimal << "\n";
  cout << decimal2 << "\n";
  cout << vivo << "\n";
  cout << nome << "\n";


  // usando o cin e cout para receber dados e atribuir   os valores as variaveis

  cout << "Digite o número de vidas: ";
  cin >> vidas;

  cout << "Digite uma letra: ";
  cin >> letra;

  cout << "Digite o valor em dinheiro: ";
  cin >> decimal;

  cout << "Digite novamente o valor eme dinheiro: ";
  cin >> decimal2;


  
  cout << "Digite seu nome: ";
  cin >> nome;
  

  cout << vidas << "\n";
  cout << letra << "\n";
  cout << decimal << "\n";
  cout << decimal2 << "\n";
  cout << vivo << "\n";
  cout << nome << "\n";
  
}