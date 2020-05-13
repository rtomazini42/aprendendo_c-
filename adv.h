#ifndef ADV_H_INCLUDED
#define ADV_H_INCLUDED



using namespace std;

int joga(){
    string entrada;
    cout << "digita algo " <<endl;
    cin >> entrada;
    cout << "Escreveu "<< entrada <<" Ok?"<<endl;

    //vamos testar ifs e elses

    const int NUMERO = 31;
    int chute;

    cout <<"Chuta um numero: " <<endl;
    cin >> chute;

    bool acertou = chute == NUMERO;
    bool maior = chute > NUMERO;


    if(acertou){
        cout <<"Voce acertou!" <<endl;
    }
    else if(maior){
        cout <<"Chute maior que numero" <<endl;

    }
    else {
        cout <<"Chute menor que número" <<endl;
    }
    return 0;

}


#endif // ADV_H_INCLUDED
