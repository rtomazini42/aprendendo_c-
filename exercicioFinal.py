import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
            #print(palavra)
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    sum = 0
    for n in range(len(as_b)):
        sum += abs(as_a[n] - as_b[n])
    resultado = sum/6
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    return resultado

def calcula_assinatura(texto):
    letras =[]
    for letra in texto:
        if letra != ',' and letra != '.'and letra != ' ':
            letras.append(letra)
    palavras = separa_palavras(texto)
    #tam_med_palavra = len(letras)/len(palavras)

    palavras_limpas = []
    for palavra in palavras:
        aux = ""
        for letra in palavra:
            if letra != ',' and letra != '.'and letra != ' ':
                aux = aux+letra
        palavras_limpas.append(aux)


    #type_token = n_palavras_diferentes(palavras_limpas)/len(palavras)
    #hapax = n_palavras_unicas(palavras_limpas)/len(palavras)


    sentencas = separa_sentencas(texto)
    n_c_sentencas = 0
    n_sentencas = 0




    for sentenca in sentencas:
        n_sentencas = n_sentencas + 1
        for caracter in sentenca:
            if caracter != '.':
                n_c_sentencas = n_c_sentencas+1

    #tam_med_sent =n_c_sentencas/n_sentencas

    frases_temp = []
    frases = []
    frases_aux = sentencas
    for sentenca in frases_aux:
        frases_aux = separa_frases(sentenca)
        frases_temp.append(frases_aux)
    for i in range(len(frases_temp)):
        for frase in frases_temp[i]:
            frases.append(frase)

    n_c_frases = 0
    for frase in frases:
        for caracter in frase:
            n_c_frases = n_c_frases + 1

    tam_med_palavra = len(letras)/len(palavras)
    type_token = n_palavras_diferentes(palavras_limpas)/len(palavras)
    hapax = n_palavras_unicas(palavras_limpas)/len(palavras)
    tam_med_sent =n_c_sentencas/n_sentencas
    com_sent = len(frases)/n_sentencas
    tam_med_frase = n_c_frases/len(frases)

    #print(tam_med_frase)
    #print(tam_med_palavra, type_token , hapax)
    return tam_med_palavra, type_token, hapax, tam_med_sent,com_sent, tam_med_frase

def avalia_textos(textos, ass_cp):
    resultados = []
    for n in textos:
        resultados.append(calcula_assinatura(n))

    semelhanca = []
    for n in resultados:
        semelhanca.append(compara_assinatura(original, n))

    maior_pos = 0
    maior = semelhanca[0]
    for n in range(len(semelhanca)):
        if semelhanca[n]> maior:
            maior = semelhanca[n]
            maior_pos = n

    return maior_pos

#texto = "o gato caçava o rato"
#texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
#print(calcula_assinatura(texto))

original = le_assinatura()
suspeitos = le_textos()


print("O autor do texto " , avalia_textos(suspeitos, original), " está infectado com COH-PIAH")
