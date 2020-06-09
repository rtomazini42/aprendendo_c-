#include <iostream>
#include <string>
#include<map>
#include <vector>

using namespace std;
// make CXXFLAGS= -std=c++11


string palavra = "CHINELO";
map <char, bool> chutou;
vector <char> chutes_errados;
//vector <char> chutes_errados;

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
    return false;

}

bool nao_enforcou(){
    return chutes_errados.size() < 5;

}


int main () {
  cout<<"*************************" << '\n';
  cout<<"****JOGO DO ENFORCADO****"<<endl;
  cout<<"*************************" << '\n';
  //cout<<palavra<<endl;
  printar();
  //bool enforcado = false;
  //bool acertou = false;
  char chute;



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
