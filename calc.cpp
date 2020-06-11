#include <iostream>
#include <cstdlib>

using namespace std;


int operacao(int op){
  int numero1;
  int numero2;
 cout << "Digite o primeiro numero" << '\n';
 cin >> numero1;
 cout << "Digite o primeiro numero" << '\n';
 cin >> numero2;
 if(op == 1){
    return numero1 + numero2;
 }
 if(op == 2){
    return numero1 - numero2;
 }
 if(op == 3){
    return numero1 * numero2;
 }
 if(op == 4){
    return numero1 / numero2;
 }
 else{
   std::cout << "esse programa é inquebravel" << '\n';
   return numero1 % numero2;
 }
}

int main() {
  int op;
  cout << "escolha a operacao\n1-soma\n2-subtracao\n3-multiplicacao\n4-divisao" << '\n';
  cin >> op;
  cout<< operacao(op);
  return 0;
}
