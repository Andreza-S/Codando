//Crie uma Classe chamada Empregado que possui 3 membros de dados - um nome, um sobrenome e um salário mensal. Sua Classe deve ter um construtor que inicialize os 3 membros de dados. Forneça uma função set e uma função get para cada membro de dados. Se o salário mensal não for positivo, configure-o como 0. Escreva um programa de teste que demonstre as capacidade da classe Empregado. Crie dois objetos Empregado e exiba seu salário mensal. Em seguida, dê um aumento de 10% para cada um dos empregados e exiba novamente o salário mensal.


#include "Empregado.h"
#include "Empregado.h"

using namespace std;


int main() {

  // demonstração dos valores iniciados pelo construtor
  Empregado objeto_construtor;
  
  cout << "\n\nAqui serão apresentados os valores inicados pelo construtor:\n"<< "--------------INICIO-----------------\n\n";
  
  cout << objeto_construtor.getNome() << "\n\n";
  cout <<objeto_construtor.getSobrenome() << "\n\n";
  cout <<"Esse é meu salario mensal: R$ " << objeto_construtor.getSalarioMensal() << "\n\n";


  cout << "--------------FIM-----------------\n\n";

  //objeto_1
  Empregado objeto_1;
  
    cout << "\n\nAqui serão apresentados os dados do objeto_1:\n"<< "--------------INICIO-----------------\n\n";

  objeto_1.setNome("Zezinho");
  objeto_1.setSobrenome("Sobre");
  objeto_1.setSalarioMensal(200.00); // salario > 0
    
  cout << objeto_1.getNome() << "\n\n";
  cout <<objeto_1.getSobrenome() << "\n\n";
  cout <<"Esse é meu salario mensal: R$ " << objeto_1.getSalarioMensal() << "\n\n";

  cout << "--------------FIM-----------------\n\n";



  //Objeto_2
    Empregado objeto_2;
  
    cout << "\n\nAqui serão apresentados os dados do objeto_2:\n"<< "--------------INICIO-----------------\n\n";

  objeto_2.setNome("Aninha");
  objeto_2.setSobrenome("Sobré");
  objeto_2.setSalarioMensal(-500.53); // salario < 0
    
  cout << objeto_2.getNome() << "\n\n";
  cout <<objeto_2.getSobrenome() << "\n\n";
  cout <<"Esse é meu salario mensal: R$ " << objeto_2.getSalarioMensal() << "\n\n";

  cout << "--------------FIM-----------------\n\n\n";

  
  //Agora será acrescentado um aumento de 10% nos salraios dos funcionarios
    
  //Objeto_1
    objeto_1.setSalarioMensal(objeto_1.getSalarioMensal() * 0.10 + objeto_1.getSalarioMensal());
    
  //Objeto_2
    objeto_2.setSalarioMensal(objeto_2.getSalarioMensal() * 0.10 + objeto_2.getSalarioMensal());


  
  //REIMPRESSAO DOS DADOS

  cout << "\n\n|||||||||||||||||||||||||||||||||||||||||||||||\n\nSALARIOS ATUALIZADOS:";

  //objeto_1
 
    cout << "\n\nAqui serão apresentados os dados do objeto_1:\n"<< "--------------INICIO-----------------\n\n";
    
  cout << objeto_1.getNome() << "\n\n";
  cout <<objeto_1.getSobrenome() << "\n\n";
  cout <<"Esse é meu salario mensal: R$ " << objeto_1.getSalarioMensal() << "\n\n";

  cout << "--------------FIM-----------------\n\n";


  //Objeto_2
  
    cout << "\n\nAqui serão apresentados os dados do objeto_2:\n"<< "--------------INICIO-----------------\n\n";
   
  cout << objeto_2.getNome() << "\n\n";
  cout <<objeto_2.getSobrenome() << "\n\n";
  cout <<"Esse é meu salario mensal: R$ " << objeto_2.getSalarioMensal() << "\n\n";

  cout << "--------------FIM-----------------\n\n\n";
  
  
}