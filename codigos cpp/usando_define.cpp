#include <iostream>
using namespace std;

// variavel CONSTANTE
#define pi 3.1415;

// usamos o #define para executar uma ação quando evocamos aprendendo dentro do código, 
//nesse caso quando a variavel aprendendo é evocada a frase é printada na tela

#define aprendendo cout << "\nAprendendo C++";

int main() {

// Podemos declarar as variaveis separadas:
//  int vidas;
// int tiros;
//  int life;


// podemos utilizar uma única linha para declarar as variaveis, declaração multipla.
  int vidas = 3, tiros = 500, life = 100;

  // printando pi
  cout << pi;
  //executando aprendendo
  aprendendo;

  return 0;

}