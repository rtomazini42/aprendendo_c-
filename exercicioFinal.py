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
    frases = []
    palavras =[]
    palavras_aux = []
    letras = 0
    n_c_sentencas = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        n_c_sentencas = n_c_sentencas + len(sentenca)
        frases_aux = separa_frases(sentenca)
        frases.append(frases_aux)

    #print(frases)
    num_frases = 0
    for linha in range(len(frases)):
        for conteudo in frases[linha]:
            palavras_aux.append(separa_palavras(conteudo))
            num_frases = num_frases + 1
    #print(palavras_aux)
    for element in palavras_aux:
        palavras.extend(element)
    #print(palavras)
    for palavra in palavras:
        for letra in palavra:
            letras = letras + 1
    #print(len(palavras))
    palavras_diferentes = n_palavras_diferentes(palavras)
    #print(palavras_diferentes)
    num_char_frases = 0
    #print(frases)
    for frase in frases:
        for conjunto in frase:
            num_char_frases = num_char_frases + len(conjunto)
    #print(frases)
    num_sentencas = len(sentencas)
    #print(num_sentencas)


    tamanhoMedioPalavra = letras/len(palavras)
    token = palavras_diferentes/len(palavras)
    hapax = n_palavras_unicas(palavras)/len(palavras)
    tamanhoMedioSentenca = n_c_sentencas/num_sentencas
    complexidadeSentenca = num_frases/num_sentencas
    tamanhoMedioFrase = num_char_frases/num_frases
    #pass
    return tamanhoMedioPalavra, token, hapax, tamanhoMedioSentenca, complexidadeSentenca, tamanhoMedioFrase

def avalia_textos(textos, assinatura_lida):
    resultados = []
    for n in textos:
        resultados.append(calcula_assinatura(n))

    semelhanca = []
    for n in resultados:
        semelhanca.append(compara_assinatura(assinatura_lida, n))

    maior_pos = 0
    maior = semelhanca[0]
    for n in range(len(semelhanca)):
        if semelhanca[n]> maior:
            maior = semelhanca[n]
            maior_pos = n

    return maior_pos

#texto = "o gato caçava o rato"
#texto = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
#texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
#texto = 'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
#texto2 = 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.'
#texto3 = 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
#Assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
#texto = 'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
#print(calcula_assinatura(texto))

#Assinatura = le_assinatura()
#suspeitos = le_textos()
def main():
    assinatura_lida = le_assinatura()
    suspeitos = le_textos()
    print("O autor do texto " , avalia_textos(suspeitos, assinatura_lida), " está infectado com COH-PIAH")

main()
