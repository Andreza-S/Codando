// Usando comando de decisão IF ELSE com GOTO


// Desenvolver um program que receba notas e retorne a situação do aluno. Seguindo as condições:

//Nota maior ou igual a 60 o aluno será aprovado, nota entre 40 e 59 o aluno ficará de recuperação, aluno com nota menor que 40 o aluno será reprovado.


#include <iostream>
#include <cstdlib> // para executar o comandosystem ("cls") 

using namespace std;


int main() {
  
  int n1, n2, res;
  char opc;

  cout << "\nDIgite o valor da nota 1: ";
  cin >> n1;
  cout << "\nDIgite o valor da nota 2: ";
  cin >> n2;

  res = n1 +n2;

  if (res >= 60){
    cout << "\nAluno aprovado";   
  }else if(res >= 40){
    cout << "\nAluno em recuperação";
  }else{
    cout <<"\nAluno reprovado";

  }

  cout << "\n\n-------------------------------------";
  cout << "\nExecutamos o programa sem GOTO,\no programa foi executado somente uma única vez,\nagora vamos receber varias notas enquanto o usuario\ndesejar inserir notas\n";
 cout << "-------------------------------------\n\n";

  //usando o GOTO

  inicio:
  
  system("cls"); // para limpar a tela
  
  int nota1, nota2, notafinal;
  char operadorContinuarOuParar;

  cout << "\nDIgite o valor da nota 1: ";
  cin >> nota1;
  cout << "\nDIgite o valor da nota 2: ";
  cin >> nota2;

  notafinal = nota1 +nota2;

  if (notafinal >= 60){
    cout << "\nAluno aprovado\n\n";   
  }else if(notafinal >= 40){
    cout << "\nAluno em recuperação\n\n";
  }else{
    cout <<"\nAluno reprovado\n\n";
  }

  cout <<"\nDigitar outras notas? [s/n]: ";
  cin >> operadorContinuarOuParar;

  if (operadorContinuarOuParar == 's' or operadorContinuarOuParar == 'S'){
    goto inicio; // quando o usuario decidir continuar inserindo notas o programa voltará a ser executado a partir de inicio ou será encerrado caso o usuario deseje não insereir mais notas
  }
  
  return 0;
}