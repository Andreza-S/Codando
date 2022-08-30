#include <string>
#include <iostream>

using std::cin, std::cout, std::endl;

#include <fstream>
using std::ofstream, std::ifstream;

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


void salvar_dados(string& p, string& v) {
	ofstream dados("guardaDados.dat", ios::out);

	if (!dados) {
		cout << "DEU ERRADO A GRAVACAO";
	}

	dados << p << " " << v << endl;

	dados.close();
}


void ler_dados(string& pontosDoJogo, string& vidasDoJogo) {
	ifstream arqDados("guardaDados.dat", ios::in);


	if (!arqDados) {
		cout << "DEU ERRADO A LEITURA";
	}

	while (arqDados >> pontosDoJogo >> vidasDoJogo) {

	}

	arqDados.close();


}


int main() {

	string pontos, vidas;

	pontos = "11111";
	vidas = "23";
	cout << "Valores que devem ser gravados" << endl;
	cout << "Pontos: " + pontos << endl;
	cout << "Vidas: " + vidas << endl;
	salvar_dados(pontos, vidas);

	pontos = "0";
	vidas = "0";
	cout << "Variaveis resetadas" << endl;
	cout << "Pontos: " + pontos << endl;
	cout << "Vidas: " + vidas << endl;

	ler_dados(pontos, vidas);
	cout << "Valores lidos e gravados" << endl;
	cout << "Pontos: " + pontos << endl;
	cout << "Vidas: " + vidas << endl;


}