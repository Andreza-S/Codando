class Carro{

public:
  Carro(string marcaCarro, int anoCarro, string nomePropritario){

    marca = marcaCarro;
    ano = anoCarro;
    proprietario = nomePropritario;
  }

  string getMarca(){
    return marca;
  }
  int getAno(int anoCarro){
    return ano;
  }
  string getProprietario (){
    return proprietario;
  }
  string setProprietario (string nomePropritario){
    proprietario = nomeProprietario;
  }
  

private:
  string marca;
  int ano;
  string proprietario;
}