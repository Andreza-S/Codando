class Monster{

public:
  Monster(double vida, double golpe){
    life = vida;
    ataque = golpe;
  }

  double getLife(){
    return life;
  }

  double atacar(){
    return ataque;
  }

  void sofreGolpe (){
    if (life < 1.0){
      life = 0.0;
    }else{
      life -= life * 0.01;
   }
    
  }

  bool estaVivo(){
    if (life != 0.0){
      return true;
    }else{
      return false;
    }
  }
  
private:
  double life;
  double ataque;
};