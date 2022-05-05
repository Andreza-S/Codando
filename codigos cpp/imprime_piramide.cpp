// imprime 
//*
//**
//***
//****
//*****

#include <iostream>

int main() {
  int limite = 5;
  int contador;
  char asterisco = '*';

  int i;
  
  for (contador = 1; contador < limite+1; contador++){
    
    for (i = 0; i < contador; i++) {
      std::cout << asterisco;       
    }
    std::cout << '\n';

  }

}