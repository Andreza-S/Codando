#include <iostream>
using namespace std;

int main()
{
    string nomeAluno;  
    double nota1, nota2, nota3, media;

    cout << "Primeiro nome do aluno: ";
    cin >> nomeAluno;
  
    cout << "Nota 1: ";
    cin >> nota1;

    cout << "Nota 2: ";
    cin >> nota2;

    cout << "Nota 3: ";
    cin >> nota3;

    int peso1=3, peso2=4, peso3=5, divisor =         peso1+peso2+peso3;

    media = ((peso1*nota1) + (peso2*nota2) + (peso3*nota3))/divisor;

    cout << "A Média Ponderada de " << nomeAluno << " é : " << media;

    return 0;
}