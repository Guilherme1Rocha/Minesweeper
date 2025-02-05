#2.2.1
#Construtores
def cria_gerador(bits,seed):
    """
    int,int → gerador
    representação interna → lista ; exemplo: [32,1]
    devolve um gerador sendo que os valores de entrada correspodem respetivamente ao número de bits e à seed(estado inicial)
    (Verifica a validade dos argumentos)
    """
    if not (type(bits)==int and (bits==32 or bits==64)):
        raise ValueError('cria_gerador: argumentos invalidos')
    if not (type(seed) == int and seed>0 and seed<=2**bits):
        raise ValueError('cria_gerador: argumentos invalidos')
    return[bits,seed]
def cria_copia_gerador(gerador):
    """
    gerador → gerador
    recebe um gerador e devolve uma cópia do mesmo
    """
    copia_gerador = gerador.copy()
    return copia_gerador

#Seletores
def obtem_estado(gerador):
    """
    gerador → int
    devolve o estado inicial do gerador sem o alterar
    """
    return gerador[1]

#Modificadores
def define_estado(gerador,estado):
    """
    gerador,int → int
    recebe um gerador,define o estado do mesmo e devolve o novo estado
    """
    gerador[1]=estado
    return estado
def atualiza_estado(gerador):
    """
    gerador → int
    cria um novo estado através do algoritmo xorshift de geração de números pseudoaleatórios,
    atualiza o estado do gerador e devolve o novo estado
    """
    if gerador[0]==32:
        gerador[1] ^= ( gerador[1] << 13 ) & 0xFFFFFFFF 
        gerador[1] ^= ( gerador[1] >> 17 ) & 0xFFFFFFFF 
        gerador[1] ^= ( gerador[1] << 5 ) & 0xFFFFFFFF
        return gerador[1]
    if gerador[0]==64:
        gerador[1] ^= ( gerador[1] << 13 ) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= ( gerador[1] >> 7 ) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= ( gerador[1] << 17 ) & 0xFFFFFFFFFFFFFFFF
        #aplicação do algoritmo xorshift de geração de números pseudoaleatórios
    return gerador[1]
#Reconhecedores
def eh_gerador(argumento):
    """
    universal → booleano
    devolve True caso o argumento de entrada seja um gerador e devolve False caso contrário
    """
    return type(argumento)==list and len(argumento)==2 and type(argumento[0])==int and (argumento[0]==32 or argumento[0]==64)\
        and type(argumento[1])==int and 0<argumento[1]<=2**argumento[0]

#Teste
def geradores_iguais(gerador_1,gerador_2):
    """
    gerador,gerador → booleano
    verifica se ambos valores de entrada são geradores e se são iguais, devolve True caso essas duas condições se verificam
    e devolve False caso contrário
    """
    return eh_gerador(gerador_1) and eh_gerador(gerador_2) and gerador_1[0]==gerador_2[0] and gerador_1[1]==gerador_2[1]

#Tranformadores
def gerador_para_str(gerador):
    """
    gerador → str
    devolve a representação do argumento de entrada(gerador) numa cadeia de carateres
    """
    return 'xorshift{}(s={})'.format(gerador[0],gerador[1])

#Funções de alto nível
def gera_numero_aleatorio(gerador,num):
    """
    gerador,int → int
    atualiza o estado do gerador e devolve um número aleatório no intervalo [1,num]
    obtido a partir do novo estado do gerador como 1 + novo_estado%num, em que % corresponde ao resto da divisão inteira
    """
    return define_estado(gerador,atualiza_estado(gerador))%num + 1

def gera_carater_aleatorio(gerador,letra):
    """
    gerador,str → str
    atualiza o estado do gerador g e devolve um carater
    aleatório no intervalo entre 'A' e o carater maiúsculo 'letra'. Este é obtido a partir donovo estado do gerador
    como o carater na posição estado % l da cadeia de carateresde tamanho l formada por todos os carateres entre 'A' e letra.
    A operação % corresponde ao resto da divisão inteira
    """
    define_estado(gerador,atualiza_estado(gerador))
    return chr(obtem_estado(gerador)%(ord(letra)-ord('A')+1)+ord('A'))

#2.1.2
#Construtor
def cria_coordenada(coluna,linha):
    """
    str,int → coordenada
    representação interna → lista ; exemplo: ['A',1]
    recebe os valores correspondentes à coluna e à linha (respetivamente), constroí e devolve uma coordenada tendo em conta esses valores
    (Verifica a validade dos argumentos)
    """
    if not (type(coluna)==str and type(linha)==int and len(coluna)==1 and 65<=ord(coluna)<=90 and 0<linha<=99):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return [coluna,linha]

#Seletores
def obtem_coluna(coordenada):
    """
    coordenada → str
    devolve a coluna da coordenada de entrada
    """
    return coordenada[0]
def obtem_linha(coordenada):
    """
    coordenada → int
    devolve a linha da coordenada de entrada
    """
    return coordenada[1]

#Reconhecedor
def eh_coordenada(argumento):
    """
    universal → booleano
    devolve True caso o argumento de entrada corresponder a uma coordenada e devolve False caso contrário
    """
    return type(argumento)==list and len(argumento)==2 and type(argumento[0])==str and len(argumento[0])==1\
        and type(argumento[1])==int and 65<=ord(argumento[0])<=90 and 0<argumento[1]<=99
#Teste
def coordenadas_iguais(coordenada_1,coordenada_2):
    """
    coordenada,coordenada → booleano
    verifica se ambos valores de entrada são coordenadas e se são iguais, devolve True caso essas duas condições se verificam
    e devolve False caso contrário
    """
    return eh_coordenada(coordenada_1) and eh_coordenada(coordenada_2) and coordenada_1[0]==coordenada_2[0] and \
        coordenada_1[1]==coordenada_2[1]

#Transformador
def coordenada_para_str(coordenada):
    """
    coordenada → str
    devolve a representação do argumento de entrada(coordenada) numa cadeia de carateres
    """
    if coordenada[1]<=9:
        return '{}0{}'.format(coordenada[0],coordenada[1])
    return '{}{}'.format(coordenada[0],coordenada[1])

def str_para_coordenada(string):
    """
    str → coordenada
    devolve a coordenada correspondente à sua representação de cadeia de carateres
    """
    return [string[0],int(string[1::])]

#Funções de alto nível
def obtem_coordenadas_vizinhas(coordenada):
    """
    coordenada → tuplo
    devolve um tuplo que contém as coordenadas vizinhas da coordenada de entrada 
    começando pela coordenada na diagonal acima-esquerda desta e seguindo no sentido horário
    """
    contador = ord(obtem_coluna(coordenada))-1
    coordenadas_vizinhas = []
    resultado = []
    while contador<=ord(obtem_coluna(coordenada))+1:
        coordenadas_vizinhas.append([chr(contador),obtem_linha(coordenada)-1])
        contador+=1
    contador = obtem_linha(coordenada)
    while contador<=obtem_linha(coordenada)+1:
        coordenadas_vizinhas.append([chr(ord(obtem_coluna(coordenada))+1),contador])
        contador+=1
    contador = ord(obtem_coluna(coordenada))
    while contador>=ord(obtem_coluna(coordenada))-1:
        coordenadas_vizinhas.append([chr(contador),obtem_linha(coordenada)+1])
        contador-=1
    coordenadas_vizinhas.append([chr(ord(obtem_coluna(coordenada))-1),obtem_linha(coordenada)])
    for i in range(len(coordenadas_vizinhas)):
        if eh_coordenada(coordenadas_vizinhas[i]):
            resultado.append(coordenadas_vizinhas[i])
    return tuple(resultado)

def obtem_coordenada_aleatoria(coordenada,gerador):
    """
    coordenada,gerador → coordenada
    devolve uma coordenada gerada aleatoriamente onde a coluna e linha da coordenada de entrada, correspondem à coluna máxima e linha máxima 
    da coordenada aleatória. Deve ser gerada, em sequência primeiro a coluna e depois a linha.
    """
    return cria_coordenada(gera_carater_aleatorio(gerador,obtem_coluna(coordenada)),gera_numero_aleatorio(gerador,obtem_linha(coordenada)))

#2.1.3
#Construtores
def cria_parcela():
    """
    {} → parcela
    representação interna → lista com dois elementos ; exemplo:['tapada','sem mina']
    cria e devolve uma parcela tapada sem mina escondida
    """
    return ['tapada','sem mina']
def cria_copia_parcela(parcela):
    """
    parcela → parcela
    cria e devolve uma cópia da parcela de entrada
    """
    return parcela.copy()

#Modificadores
def limpa_parcela(parcela):
    """
    parcela → parcela
    modifica destrutivamente a parcela de entrada, alterando o seu estado para limpa e devolve a própria parcela
    """
    parcela[0]='limpa'
    return parcela
def marca_parcela(parcela):
    """
    parcela → parcela
    modifica destrutivamente a parcela de entrada, alterando o seu estado para marcada e devolve a própria parcela
    """
    parcela[0]='marcada'
    return parcela
def desmarca_parcela(parcela):
    """
    parcela → parcela
    modifica destrutivamente a parcela de entrada, alterando o seu estado para tapada e devolve a própria parcela
    """
    parcela[0]='tapada'
    return parcela
def esconde_mina(parcela):
    """
    parcela → parcela
    modifica destrutivamente a parcela de entrada, escondendo um mina na mesma e devolve a própria parcela
    """
    parcela[1]='com mina'
    return parcela

#Reconhecedores
def eh_parcela(argumento):
    """
    universal → booleano
    devolve True caso o argumento de entrada corresponder a uma parcela e devolve False caso contrário
    """
    return type(argumento)==list and len(argumento)==2 and type(argumento[0])==str and type(argumento[1])==str and\
         (argumento[0]=='tapada' or argumento[0]=='marcada' or argumento[0]=='limpa') and \
            (argumento[1]=='sem mina' or argumento[1]=='com mina')
def eh_parcela_tapada(parcela):
    """
    parcela → booleano
    devolve True caso a parcela de entrada se encontre tapada e devolve False caso contrário
    """
    return parcela[0]=='tapada'
def eh_parcela_marcada(parcela):
    """
    parcela → booleano
    devolve True caso a parcela de entrada se encontre marcada e devolve False caso contrário
    """
    return parcela[0]=='marcada'
def eh_parcela_limpa(parcela):
    """
    parcela → booleano
    devolve True caso a parcela de entrada se encontre limpa e devolve False caso contrário
    """
    return parcela[0]=='limpa'
def eh_parcela_minada(parcela):
    """
    parcela → booleano
    devolve True caso a parcela de entrada esconda uma mina e False caso contrário
    """
    return parcela[1]=='com mina'

#Testes
def parcelas_iguais(parcela_1,parcela_2):
    """
    parcela,parcela → booleano
    verifica se ambos valores de entrada são parcelas e se são iguais, devolve True caso essas duas condições se verificam
    e devolve False caso contrário
    """
    return eh_parcela(parcela_1) and eh_parcela(parcela_2) and parcela_1[0]==parcela_2[0] and parcela_1[1]==parcela_2[1]
    
#Transformadores
def parcela_para_str(parcela):
    """
    parcela → str
    devolve a cadeia de caracteres que representa a parcela de entrada
    em função do seu estado: parcelas tapadas ('#'), parcelas marcadas ('@'),
    parcelas limpas sem mina ('?') e parcelas limpas com mina ('X')
    """
    if parcela[0]=='tapada':
        return '#'
    if parcela[0]=='marcada':
        return '@'
    if parcela[0]=='limpa':
        if parcela[1]=='com mina':
            return 'X'
        return '?'

#Funções de Alto Nível
def alterna_bandeira(parcela):
    """
    parcela → booleano
    modifica destrutivamente a parcela de entrada: desmarcando-a se estiver marcada e marcando-a se estiver tapada,
    devolvendo True nestes dois casos, em qualquer outro caso, não modifica a parcela e devolve False
    """
    if eh_parcela_marcada(parcela):
        desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela):
        marca_parcela(parcela)
        return True
    return False

#2.1.4
#Construtores
def cria_campo(coluna,linha):
    """
    str,int → campo
    representação interna → lista de listas ; exemplo: [[['tapada','sem mina']],[['tapada','sem mina']]]
    recebe a última coluna e a última linha do campo (respetivamente) e devolve um campo do tamanho pretendido
    constituído apenas por parcelas tapadas sem minas
    verifica a validade dos argumentos
    """
    contador = ord('A')
    colunas = ''
    campo = []
    parcelas = []
    if not (type(coluna)==str and len(coluna)==1 and type(linha)==int and 65<=ord(coluna)<=90 and 0<linha<=99):
        raise ValueError('cria_campo: argumentos invalidos')
    while contador<=ord(coluna):
        colunas+=chr(contador)
        contador+=1
    for i in range(len(colunas)):
        for j in range(linha):
            parcelas += [cria_parcela()]
        campo.append(parcelas)
        parcelas=[]
    return campo

def cria_copia_campo(campo):
    """
    campo → campo
    devolve uma cópia do campo dado com argumento de entrada
    """
    copia_campo = campo.copy()
    return copia_campo

#Seletores
def obtem_ultima_coluna(campo):
    """
    campo → str
    devolve a cadeia de carateres que corresponde à última coluna do campo
    """
    return chr(ord('A')+len(campo)-1)

def obtem_ultima_linha(campo):
    """
    campo → int
    devolve o valor que corresponde à última linha do campo
    """
    count = 0
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            count +=1
        return count

def obtem_parcela(campo,coordenada):
    """
    campo,coordenada → parcela
    devolve a parcela pertencente ao campo numa coordenada específica
    """
    return campo[ord(obtem_coluna(coordenada))-ord('A')][obtem_linha(coordenada)-1]

def obtem_coordenadas(campo,estado):
    """
    campo,str → tuplo
    devolve um tuplo que contém as coordenadas do campo ordenadas em ordem ascendente da esquerda para direita e de cima para baixo
    correspondentes às parcelas com um estado definido:'limpas' para as parcelas limpas, 'tapadas' paraas parcelas tapadas, 
    'marcadas' para as parcelas marcadas, e 'minadas' para as parcelas que escondem minas.
    """
    resultado = []
    if estado=='tapadas':
        for i in range(len(campo)):
            for j in range(len(campo[i])):
                if campo[i][j][0]=='tapada':
                    resultado.append(cria_coordenada(chr(i+ord('A')),j+1))
    if estado == 'limpas':
        for i in range(len(campo)):
            for j in range(len(campo[i])):
                if campo[i][j][0]=='limpa':
                    resultado.append(cria_coordenada(chr(i+ord('A')),j+1))
    if estado == 'marcadas':
        for i in range(len(campo)):
            for j in range(len(campo[i])):
                if campo[i][j][0]=='marcada':
                    resultado.append(cria_coordenada(chr(i+ord('A')),j+1))
    if estado == 'minadas':
        for i in range(len(campo)):
            for j in range(len(campo[i])):
                if campo[i][j][1]=='com mina':
                    resultado.append(cria_coordenada(chr(i+ord('A')),j+1))
    resultado.sort(key = lambda x:x[1])
    #ordenar a lista tendo em conta a ordem pedida
    return tuple(resultado)

def obtem_numero_minas_vizinhas(campo,coordenada):
    """
    campo,coordenada → int
    devolve o número de parcelas vizinhas da parcela correspondente à coordenada que esconde uma mina
    """
    minas_vizinhas = 0
    coordenadas_vizinhas = obtem_coordenadas_vizinhas(coordenada)
    for i in range(len(coordenadas_vizinhas)):
        if ord(coordenadas_vizinhas[i][0])-ord('A')+1<=len(campo) and coordenadas_vizinhas[i][1]<=obtem_ultima_linha(campo)\
            and eh_parcela_minada(obtem_parcela(campo,coordenadas_vizinhas[i])):
            #verifica se a coordenada pertence ao campo e se a parcela correspondente esconde uma mina
            minas_vizinhas+=1
    return minas_vizinhas

#Reconhecedores
def eh_campo(arg):
    """
    universal → booleano
    devolve True caso o argumento de entrada corresponder a um campo e devolve False caso contrário
    """
    contador_parcelas=0
    if not type(arg)==list:
        return False
    if not len(arg)>0:
        return False
    for i in range(len(arg)):
        if not type(arg[i])==list and len(arg[i])>0:
            return False
        for j in range(len(arg[i])):
            contador_parcelas+=1
            if not eh_parcela(arg[i][j])==True:
                return False
    if contador_parcelas<12:
        return False
    return True

def eh_coordenada_do_campo(campo,coordenada):
    """
    campo,coordenada → booleano
    devolve True caso a coordenada pertencer ao campo e devolve False caso contrário
    """
    n_linhas=0
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            n_linhas+=1
        break
    return len(campo)>=ord(coordenada[0])-ord('A')+1 and n_linhas>=coordenada[1]

#Teste
def campos_iguais(campo_1,campo_2):
    """
    campo,campo → booleano
    verifica se ambos valores de entrada são campos e se são iguais, devolve True caso essas duas condições se verificam
    e devolve False caso contrário
    """
    if not eh_campo(campo_1) and eh_campo(campo_2):
        return False
    if not len(campo_1)==len(campo_2):
        return False
    for i in range(len(campo_1)):
        if not len(campo_1[i])==len(campo_2[i]):
            return False
        for j in range(len(campo_1[i])):
            if parcelas_iguais(campo_1[i][j],campo_2[i][j])==False:
                return False
    return True


#Tranformadores
def campo_para_str(campo):
    """
    campo → str
    devolve uma cadeia de carateres que representa o campo
    """
    n_minas = 0
    contador = 1
    representaçao = ''
    cadeia = '   '
    representaçao_linhas=[]
    representaçao_parcelas = ''
    representaçao_total = []
    for i in range(len(campo)):
        cadeia+=chr(i+ord('A'))
    cadeia += '\n''  ' + '+'+ len(campo)*'-'+'+'
    while contador<=obtem_ultima_linha(campo):
        cadeia_coordenada = coordenada_para_str(cria_coordenada(chr(ord('A')),contador)) 
        representaçao_linhas.append('\n'+ cadeia_coordenada[1::])
        contador+=1
    contador=0
    while contador<obtem_ultima_linha(campo):
        for i in range(len(campo)):
            parcela = campo[i][contador]
            representaçao = parcela_para_str(parcela)
            n_minas = obtem_numero_minas_vizinhas(campo,cria_coordenada(chr(ord('A')+i),contador+1))
            if representaçao=='?' and n_minas>0:
                #caso a parcela esteja limpa e exista minas na vizinhança
                representaçao = str(n_minas)
            if representaçao=='?' and n_minas==0:
                #caso a parcela esteja limpa e não exista minas na vizinhança
                representaçao = ' '
            representaçao_parcelas+=representaçao
        representaçao_total.append(representaçao_linhas[contador]+'|'+representaçao_parcelas+'|')
        representaçao_parcelas=''
        contador+=1
    for i in range(len(representaçao_total)):
        cadeia+=representaçao_total[i]
    cadeia += '\n''  ' + '+'+ len(campo)*'-'+'+'
    return cadeia

#Funções de Alto Nível
def coloca_minas(campo,coordenada,gerador,minas):
    """
    campo,coordenada,gerador,int → campo
    modifica destrutivamente o campo escondendo minas nele(o número de minas suposto colocar é o 4ºvalor de entrada). 
    As coordenadas onde é suposto esconder uma mina são aleatórias e irão ser geradas em sequência utilizando o gerador.
    É necessário que a coordenadas geradas aleatoriamente não coincidem com a coordenada de entrada nem com as suas vizinhas.
    """
    coluna = obtem_ultima_coluna(campo)
    linha = obtem_ultima_linha(campo)
    coordenadas_vizinhas = obtem_coordenadas_vizinhas(coordenada)
    while minas!=0:
        coordenada_aleatoria = obtem_coordenada_aleatoria(cria_coordenada(coluna,linha),gerador)
        if not coordenadas_iguais(coordenada_aleatoria,coordenada) and coordenada_aleatoria not in coordenadas_vizinhas\
            and coordenada_aleatoria not in obtem_coordenadas(campo, 'minadas'):
            esconde_mina(obtem_parcela(campo,coordenada_aleatoria))
            minas-=1
    return campo
   
def limpa_campo(campo,coordenada):
    """
    campo,coordenada → campo
    modifica destrutivamente o campo limpando a parcela correspondente à coordenada de entrada (se esta não estiver já limpa)
    Caso não haja minas escondidas na vizinhança, limpa todas as parcelas vizinhas tapadas. Caso a parcela correspondente à coordenada
    de entrada já esteja limpa, a operação não tem efeito
    """
    if eh_parcela_limpa(obtem_parcela(campo,coordenada)):
        return campo
    limpa_parcela(obtem_parcela(campo,coordenada))
    if obtem_numero_minas_vizinhas(campo,coordenada)==0 and not eh_parcela_minada(obtem_parcela(campo,coordenada)):
        coordenadas_vizinhas = obtem_coordenadas_vizinhas(coordenada)
        for i in range(len(coordenadas_vizinhas)):
            if eh_coordenada_do_campo(campo,coordenadas_vizinhas[i]) and eh_parcela_tapada(obtem_parcela(campo,coordenadas_vizinhas[i])):
                limpa_campo(campo,coordenadas_vizinhas[i])
    return campo

#Funções Adicionais
def jogo_ganho(campo):
    """
    campo → booleano
    devolve True caso todas as parcelas sem minas no campo se encontrem limpas e devolve False caso contrário
    """
    n_colunas = ord(obtem_ultima_coluna(campo))-ord('A')+1
    n_linhas = obtem_ultima_linha(campo)
    for i in range(n_colunas):
        for j in range(n_linhas):
            if not eh_parcela_minada(obtem_parcela(campo,cria_coordenada(chr(i+ord('A')),j+1)))\
                and not eh_parcela_limpa((obtem_parcela(campo,cria_coordenada(chr(i+ord('A')),j+1)))):
                return False
    return True

def turno_jogador(campo):
    """
    campo → booleano
    oferece ao jogador a opção de escolher uma ação e uma coordenada.De acordo com a ação escolhida (limpar ou marcar)
    a função irá modificar destrutivamente o campo (limpando ou marcando parcelas). Caso o jogador tenha limpo uma parcela
    que esconde um mina a função devolve False,caso contrário devolve True
    """
    açao = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while açao!='L'and açao!='M':
        açao=input('Escolha uma ação, [L]impar ou [M]arcar:')
    #caso o input do jogador é diferente do esperado continua a pedir a ação
    coordenada = input('Escolha uma coordenada:')
    while len(coordenada)!=3 or not eh_coordenada(str_para_coordenada(coordenada)) \
        or not eh_coordenada_do_campo(campo,str_para_coordenada(coordenada)):
        coordenada = input('Escolha uma coordenada:')
    #caso o input do jogador é diferente do esperado continua a pedir a coordenada
    if açao=='M':
       alterna_bandeira(obtem_parcela(campo,str_para_coordenada(coordenada)))
       return True
    if açao=='L':
        limpa_campo(campo,str_para_coordenada(coordenada))
        if eh_parcela_minada(obtem_parcela(campo,str_para_coordenada(coordenada))):
            return False
        return True

def minas(coluna,linha,parcelas_minadas,bits,seed):
    """
    str,int,int,int,int → booleano
    devolve True caso o jogador conseguir ganhar o jogo,caso contrário devolve False
    (Verifica a validade dos argumentos)
    """
    marcadas = 0
    if not (type(coluna)==str and len(coluna)==1 and type(linha)==int and 65<=ord(coluna)<=90 and 0<linha<=99):
        raise ValueError('minas: argumentos invalidos')
    if not (type(parcelas_minadas)==int and 0<parcelas_minadas<(ord(coluna)-ord('A')+1)*linha):
        raise ValueError('minas: argumentos invalidos')
    campo = cria_campo(coluna,linha)
    if not eh_campo(campo):
        raise ValueError('minas: argumentos invalidos')
    if not (type(bits)==int and (bits==32 or bits==64) and type(seed)==int and 0<seed<=2**bits):
        raise ValueError('minas: argumentos invalidos')
    gerador = cria_gerador(bits,seed)
    print('   [Bandeiras {}/{}]'.format(marcadas,parcelas_minadas))
    print(campo_para_str(campo))
    coordenada = input('Escolha uma coordenada:')
    while len(coordenada)!=3 or not eh_coordenada(str_para_coordenada(coordenada)) or\
         not eh_coordenada_do_campo(campo,str_para_coordenada(coordenada)):
        coordenada = input('Escolha uma coordenada:')
    coloca_minas(campo,str_para_coordenada(coordenada),gerador,parcelas_minadas)
    limpa_campo(campo,str_para_coordenada(coordenada))
    print('   [Bandeiras {}/{}]'.format(marcadas,parcelas_minadas))
    print(campo_para_str(campo))
    while turno_jogador(campo):
        if not jogo_ganho(campo):
            marcadas = len(obtem_coordenadas(campo,'marcadas'))
            print('   [Bandeiras {}/{}]'.format(marcadas,parcelas_minadas))
            print(campo_para_str(campo))
        if jogo_ganho(campo):
            marcadas = len(obtem_coordenadas(campo,'marcadas'))
            print('   [Bandeiras {}/{}]'.format(marcadas,parcelas_minadas))
            print(campo_para_str(campo))
            print('VITORIA!!!')
            return True
    marcadas = len(obtem_coordenadas(campo,'marcadas'))
    print('   [Bandeiras {}/{}]'.format(marcadas,parcelas_minadas))
    print(campo_para_str(campo))
    print('BOOOOOOOM!!!')
    return False