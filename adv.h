#ifndef ADV_H_INCLUDED
#define ADV_H_INCLUDED

using namespace std;


bool max_tent(int tentativas,int tent_max){
        if(tentativas == tent_max){
            cout <<"Você perdeu "<<endl;
            return true;
        }
        else{
            cout<<endl<<"jogando"<<endl;
            return false;
        }

}




int joga(){
    int tentativas = 0;
    double pontos = 1000.00;
    int tent_max;
    string nome;
    cout << "digita seu nome " <<endl;
    cin >> nome;
    cout << "Jogando: "<< nome <<" Ok? "<<endl;

    char dificuldade;

    cout<< "qual dificuldade? Fácil(f), Médio(m) ou dificil(d)"<<endl;

    cin >> dificuldade;
    if (dificuldade == 'f'){
        tent_max = 10;
    }
        if (dificuldade == 'm'){
        tent_max = 7;
    }
    if (dificuldade == 'm'){
        tent_max = 5;
    }
    else{
        tent_max = 3;
    }



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
            //tentando(tentativas, tent_max);


        }
        else {
            cout <<"Chute menor que numero" <<endl;
            pontos_perdidos = (NUMERO - chute)/2.0;
            pontos = pontos - pontos_perdidos;
            //tentando(tentativas, tent_max);
        }

        if((max_tent(tentativas, tent_max))== true){
            break;
        }




    }

    return 0;

}


#endif // ADV_H_INCLUDED
