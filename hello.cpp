#include <iostream>

using namespace std;

int main()
{   int numero_teste = 13;
    cout << "Olá mundo. Eu to aprendendo C++, pq eu perdi o sentido da minha vida" << endl;
    cout << "Testando mais uma linha" << endl;
    cout << "ainda hoje: desisitndo de C++" << endl;
    cout << "numero escondido: "<< numero_teste <<" para dar sorte"<< endl;

    int entrada;
    cout << "digita algo " <<endl;
    cin >> entrada;
    cout << "numero digitado: "<< entrada <<endl;

    //vamos testar ifs e elses

    int numero_secreto = 31;
    int chute;
    cout <<"Chuta um numero: " <<endl;
    cin >> chute;
    if(chute == numero_secreto){
        cout <<"Voce acertou!" <<endl;
    }
    else if(chute > numero_secreto){
        cout <<"Numero eh menor que o chute" <<endl;

    }
    else {
        cout <<"Numero eh maior que o chute" <<endl;
    }
    return 0;
 //linha adicionada só pra fazer de conta que fiz algo hoje
}
