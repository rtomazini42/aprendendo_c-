#include <iostream>
#include <string>
#include<map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>


using namespace std;
// make CXXFLAGS= -std=c++11


string palavra = "___________";
map <char, bool> chutou;
vector <char> chutes_errados;
//vector <char> chutes_errados;

vector <string> le_arquivo(){
  ifstream arquivo;
  arquivo.open("bancopalavras.txt");
  int quantidade_palavras;
  arquivo>> quantidade_palavras;

  vector<string> palavras_arquivo;

  for(int i = 0; i <quantidade_palavras; i++){
    string palavra_lida;
    arquivo >> palavra_lida;
    palavras_arquivo.push_back(palavra_lida);
    //cout<<palavras_arquivo.size()<<endl;

  }
  return palavras_arquivo;

}

void sorteia_palavra(){
  vector<string> palavras = le_arquivo();
  srand(time(NULL));
  //cout <<palavras.size()<< '\n';
  int indice_sorteado = rand()%palavras.size();
  //cout <<indice_sorteado<< '\n';
  //palavra =  palavras[indice_sorteado];
  cout <<palavra<< '\n';
}

bool letra(char chute){
//  for(int i = 0; i < palavra.size(); i++){
//    if(chute == palavra[i]){
  for(char letra :palavra){
      if(chute == letra){
        return true;
      }
  }
  return false;
}


string printar(){

  for(char letra:palavra){
    if(chutou [letra]){
      cout << letra << ' ';
    }
    else{
      cout << " _ ";
    }

  }
  cout << "\n";
}

bool nao_acertou(){
    for(char letra:palavra){
      if(!chutou[letra]){
        return true;
      }
    }
    cout<<"Acertou!"<<endl;
    return false;

}

bool nao_enforcou(){
    if(chutes_errados.size() == 5){
      cout<<"perdeu!"<<"\n"<<"A palavra era:"<<palavra<<endl;
    }
    return chutes_errados.size() < 5;

}
int abertura(){
  cout<<"*************************" << '\n';
  cout<<"****JOGO DO ENFORCADO****"<<endl;
  cout<<"*************************" << '\n';
}

int gameloop(){
  char chute;
  //sorteia_palavra();

  while (nao_enforcou() && nao_acertou()){
    cout <<"Chute: "<<endl;
    cin >> chute;
    cout <<"seu chute foi: "<<chute<<endl;
    chutou[chute] = true;


    if(letra(chute)){
      cout <<"Voce acertou uma letra"<<endl;
    }
    else{
      cout <<"voce errou"<<endl;
      chutes_errados.push_back(chute);
    }
    printar();
    cout << "Chutes errados: ";
    for (char letra:chutes_errados) {
      cout << letra <<"  ";
    }
     cout <<endl<<endl;
  }
}



int main () {
  abertura();
  sorteia_palavra();
  printar();

  gameloop();

}
