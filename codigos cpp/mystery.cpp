// O que faz o programa a seguir?

#include <iostream>

using std::cout, std::cin, std::endl;

int mystery(int, int);

int main()
{
 int x, y;

 cout << "Entre com dois inteiros: ";
 cin >> x >> y;
 cout << "Resultado: " << mystery(x, y) << endl;
 return 0;
}

//O parâmetro b deve ser um inteiro positivo
int mystery(int a, int b)
{
 if (b == 1)
   return a;
 else
   return a + mystery(a, b - 1);
}


// Reposta:
//Através da recursividade a função cria um tipo de loop onde b serve como uma espécie de contador, quando b for igual a 1 a chamada de recursividade e suas operações são encerradas retornando a. Quanto a função é evocada através da recursividade o valor de a é somado b vezes e no final é printado na tela o valor final da soma.

