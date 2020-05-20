#ifndef ADV_H_INCLUDED
#define ADV_H_INCLUDED



using namespace std;

int joga(){
    int tentativas = 0;
    double pontos = 1000.00;
    string nome;
    cout << "digita seu nome " <<endl;
    cin >> nome;
    cout << "Jogando: "<< nome <<" Ok? "<<endl;

    //vamos testar ifs e elses

    const int NUMERO = 31;
    bool nao_acertou = true;
    int chute;
    double pontos_perdidos;

    while(nao_acertou){
        tentativas++;
        cout <<"Tentativa: "<< tentativas <<endl;
        cout <<"Chuta um numero: " <<endl;
        cin >> chute;

        bool acertou = chute == NUMERO;
        bool maior = chute > NUMERO;


        if(acertou){
            cout <<endl<<endl;
            cout <<"Voce acertou!" <<endl;
            pontos = pontos - tentativas;
            cout <<"Voce acertou em: "<< tentativas<<" tentativas"<<endl;
            cout <<endl<<endl;
            cout <<nome<< " ganhou "<< pontos << endl;
            nao_acertou = false;
        }
        else if(maior){
            cout <<"Chute maior que numero" <<endl;
            pontos_perdidos = (chute - NUMERO)/2.0;
            pontos = pontos - pontos_perdidos;


        }
        else {
            cout <<"Chute menor que numero" <<endl;
            pontos_perdidos = (NUMERO - chute)/2.0;
            pontos = pontos - pontos_perdidos;
        }



    }

    return 0;

}


#endif // ADV_H_INCLUDED
