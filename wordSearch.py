


# = = = = = = = = TIPO DIRECAO = = = = = = = = = #
#                                                #
# O tipo direcao e' representado                 #
# como uma string com a abreviatura              #
# das orientacoes de uma rosa dos ventos         #
#                                                # 
# = = = = = = = = = = = = = = = = = = = = = = =  #




# 1. Reconhecedores

def e_direcao(arg):
    '''e_direcao : universal -> logico
       e_direcao(arg) tem o valor verdadeiro se o arg for do 
       tipo direcao e falso caso contrario.'''

    if (arg == 'N' or arg == 'S' or arg == 'E' or arg == 'W' or \
        arg == 'NE' or arg == 'NW' or arg == 'SE' or arg == 'SW'):
        return True
    else:
        return False
    
def e_norte(arg):    
    '''e_norte: direcao -> logico
       e_norte(arg) tem o valor verdadeiro se o arg for o 
       elemento 'N' e falso caso contrario.'''

    if arg == 'N' :
        return True
    else:
        return False
    
def e_sul(arg):
    '''e_sul: direcao -> logico
       e_sul(arg) tem o valor verdadeiro se o arg for o 
       elemento 'S' e falso caso contrario.'''

    if arg == 'S' :
        return True
    else:
        return False
    
def e_leste(arg):
    '''e_leste: direcao -> logico
       e_leste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'E' e falso caso contrario.'''

    if arg == 'E' :
        return True
    else:
        return False
    
def e_oeste(arg):
    '''e_oeste: direcao -> logico
       e_oeste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'W' e falso caso contrario.'''

    if arg == 'W' :
        return True
    else:
        return False
    
def e_nordeste(arg):
    '''e_nordeste: direcao -> logico
       e_nordeste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'NE' e falso caso contrario.'''

    if arg == 'NE' :
        return True
    else:
        return False
    
def e_noroeste(arg):
    '''e_noroeste: direcao -> logico
       e_noroeste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'NW' e falso caso contrario.'''

    if arg == 'NW' :
        return True
    else:
        return False
    
def e_sudeste(arg):
    '''e_sudeste: direcao -> logico
       e_sudeste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'SE' e falso caso contrario.'''

    if arg == 'SE' :
        return True
    else:
        return False
    
def e_sudoeste(arg):
    '''e_sudoeste: direcao -> logico
       e_sudoeste(arg) tem o valor verdadeiro se o arg for o 
       elemento 'SW' e falso caso contrario.'''

    if arg == 'SW' :
        return True
    else:
        return False

# 2. Testes

def direcoes_iguais(d1, d2):
    '''direcoes_iguais: direcao * direcao -> logico
       direcoes_iguais(d1, d2) devolve o valor verdadeiro 
       se as direcoes d1 e d2 forem iguais e falso caso contrario.'''

    if d1 == d2 :
        return True
    else:
        return False
    
# 3. Outras operacoes

def direcao_oposta(d):
    '''direcao_oposta: direcao -> direcao
       direcao_oposta(d) devolve a direcao oposta de d 
       de acordo com a rosa dos ventos.'''

    coordenadas = {'N':'S','S':'N' ,  \
                   'E':'W','W':'E' ,   \
                   'NE':'SW','SW':'NE' ,\
                   'NW':'SE','SE':'NW'}
    
    return coordenadas[str(d)]





# = = = = = = TIPO COORDENADA = = = = = #
#                                       #
# O tipo coordenada e' representado     #
# como um tuplo de tres argumentos:     #
#                                       #
#       1) linha                        #
#       2) coluna                       #
#       3) direcao                      #
#                                       #
# = = = = = = = = = = = = = = = = = = = #



# 1. Construtor

def coordenada(l, c, d):
    '''coordenada: No x No x direcao -> coordenada   (l,c,d)
       coordenada(l, c, d) tem como valor a coordenada referente 
       a posicao (l,c) e direcao d.'''

    if not isinstance(l, int) or not isinstance(c, int):
        raise ValueError('coordenada: argumentos invalidos') 
    elif e_direcao(d) == False:
        raise ValueError('coordenada: argumentos invalidos')    
    elif l < 0 or c < 0:
        raise ValueError('coordenada: argumentos invalidos')
    else:
        return (l, c, d) # representacao interna
    
    
# 2. Selectores

def coord_linha(c):
    '''coord_linha: coordenada -> No
    coord_linha(c) tem como valor a linha da coordenada.'''

    return c[0]


def coord_coluna(c):
    '''coord_coluna: coordenada -> No
    coord_coluna(c) tem como valor a coluna da coordenada.'''

    return c[1]


def coord_direcao(c):
    '''coord_direcao: coordenada -> direcao
       coord_direcao(c) tem como valor a direcao da coordenada.'''

    return c[2]


#3. Reconhecedor 

def e_coordenada(arg):
    '''e_coordenada: universal -> logico
       e_coordenada(arg) tem o valor verdadeiro se o arg for 
       do tipo coordenada e falso caso contrario.'''   


    if isinstance(arg, tuple) or \
       isinstance(arg, list) or \
       isinstance(arg, dict) \
       and len(arg) == 3:
        
        return arg[0] >= 0 and \
                    arg[1] >= 0 and \
                    isinstance(arg[0], int) and \
                    isinstance(arg[1], int) and \
                    e_direcao(arg[2])        
    else:
        return False
    


# 4. Testes

def coordenadas_iguais(c1, c2):
    '''coordenadas_iguais: coordenada x coordenada -> logico
       coordenadas_iguais(c1, c2) compara cada elemento de uma 
       coordenada com o correspondente da outra coordenada'''

    if c1[0] == c2[0] and \
       c1[1] == c2[1] and \
       c1[2] == c2[2]:
        return True
    else:
        return False

# 5. Outras operacoes

def coordenada_string(c): 
    '''coordenada_string: coordenada -> string
       coordenada_string(c) devolve a representacao externa de uma coordenada'''
    strg = '(' + str(c[0]) + ', ' + str(c[1]) + ')' + '-' + c[2]
    return (strg)



# = = = = = = = = TIPO GRELHA = = = = = = = = #
#                                             #
# Uma grelha e' uma matriz mxn, com m o       #
# numero de linhas e n o numero de colunas.   #
# Este tipo e' representado como uma lista    #
# na qual cada elemento e' uma cadeia de      #
# caracteres.                                 #
#                                             #
# = = = = = = = = = = = = = = = = = = = = = = #



# 1. Construtor

def grelha(lst):
    '''grelha: lista de strings -> grelha
       grelha(lst) tem como valor uma grelha mxn, em que m e' o 
       numero de elementos da lista lst e n o numero de caracteres 
       de cada string na lista.'''
    
    if ((not isinstance (lst, list)) or lst == []):
        raise ValueError('grelha: argumentos invalidos')
    
    i = 0
    while (i < len(lst)):
        if ( isinstance (lst[i], str )):
            comprimentoposicaozero = len(lst[0])
            comprimentodasoutras = len(lst[i])
            if ( comprimentoposicaozero != comprimentodasoutras ):
                raise ValueError('grelha: argumentos invalidos')
            else:
                i = i + 1
        else:
            raise ValueError('grelha: argumentos invalidos')
    
    return lst


# 2. Selector 

def grelha_nr_linhas(g):
    '''grelha_nr_linhas: grelha -> No
       grelha_nr_linhas(g) devolve o numero de linhas da grelha g.'''
    
    return len(g)

def grelha_nr_colunas(g):
    '''grelha_nr_colunas: grelha -> No
       grelha_nr_colunas(g) devolve o numero de colunas da grelha g.'''

    return len(g[0])

def grelha_elemento(g, l, c):
    '''grelha_elemento: grelha x No x No -> caracter
       grelha_elemento(g, l, c) devolve o caracter que esta na 
       posicao (l , c) da grelha g.'''
    
    if (0 <= l <= (grelha_nr_linhas(g) - 1)) and \
            (0 <= c <= (grelha_nr_colunas(g) - 1)):
        return g[l][c]  
    else:
        raise ValueError('grelha_elemento: argumentos invalidos')
    
    

def grelha_linha(g, c):
    '''grelha_linha: grelha x coordenada -> string
       grelha_linha(g, c) devolve a cadeia de caracteres que 
       corresponde a linha definida segundo a direcao dada pela 
       coordenada c, e que inclui a posicao dada pela mesma coordenada.'''
    
    direc = c[2]          #direcao para implementar a condicao adequada
    i = 0                 #numero da linha
    j = 0                 #numero da coluna
    a = c[0] + 1          #variavel para nao haver repeticao de caracteres
    b = c[1] + 1          #variavel para nao haver repeticao de caracteres
    col = c[1] - 1        #variavel especial para SW e NE
    palavra1 = ''
    palavra2 = ''
    if not 0 <= c[0] < grelha_nr_linhas(g) or \
            not 0 <= c[1] < grelha_nr_colunas(g):
        raise ValueError('grelha_linha: argumentos invalidos')
    
    if direc == 'S':
        while i < grelha_nr_linhas(g):
            palavra1 = palavra1 + grelha_elemento(g, i, c[1])
            i = i + 1
            
    if direc == 'N':
        while i < grelha_nr_linhas(g):
            palavra1 = grelha_elemento(g, i, c[1]) + palavra1
            i = i + 1
            
    if direc == 'E':
        while j < grelha_nr_colunas(g):
            palavra1 = palavra1 + grelha_elemento(g, c[0], j)
            j = j + 1
            
    if direc == 'W':
        while j < grelha_nr_colunas(g):
            palavra1 = grelha_elemento(g, c[0], j) + palavra1
            j = j + 1
            
    if direc == 'SE':
        while a < grelha_nr_linhas(g) and b < grelha_nr_colunas(g):
            palavra2 = palavra2 + grelha_elemento(g, a, b)
            a = a + 1
            b = b + 1
        a = c[0]
        b = c[1]
        while a >= 0 and b >= 0:
            palavra1 = grelha_elemento(g, a, b) + palavra1
            a = a - 1
            b = b - 1
            
    if direc == 'NW':
        while a < grelha_nr_linhas(g) and b < grelha_nr_colunas(g):
            palavra1 = grelha_elemento(g, a, b) + palavra1
            a = a + 1
            b = b + 1
        a = c[0]
        b = c[1]
        while a >= 0 and b >= 0:
            palavra2 = palavra2 + grelha_elemento(g, a, b)
            a = a - 1
            b = b - 1  
            
    if direc == 'SW':
        while a < grelha_nr_linhas(g) and col >= 0:
            palavra2 = palavra2 + grelha_elemento(g, a, col)
            a = a + 1
            col = col - 1
        a = c[0]
        col = c[1]
        while a >= 0 and col < grelha_nr_colunas(g):
            palavra1 = grelha_elemento(g, a, col) + palavra1
            a = a - 1
            col = col + 1
            
    if direc == 'NE':
        while a < grelha_nr_linhas(g) and col >= 0:
            palavra1 = grelha_elemento(g, a, col) + palavra1
            a = a + 1
            col = col - 1
        a = c[0]
        col = c[1]
        while a >= 0 and col < grelha_nr_colunas(g):
            palavra2 =  palavra2 + grelha_elemento(g, a, col)
            a = a - 1
            col = col + 1
                         
    return str(palavra1 + palavra2)

            
# 3. Reconhecedor

def e_grelha(arg):
    '''e_grelha: universal -> logico
       e_grelha(arg) tem o valor verdadeiro se o arg 
       for do tipo grelha e falso caso contrario.'''

    i = 1
    if isinstance(arg, list):
        if isinstance(arg[0], str):
            while i < len(arg):
                if len(arg[i]) != len(arg[0]):
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False
    
    
    
# 4. Testes

def grelhas_iguais(g1, g2):
    '''grelhas_iguais: grelha x grelha -> logica
       grelhas_iguais(g1, g2) devolve o valor verdadeiro se 
       as grelhas forem iguais e falso caso contrario.'''

    return g1 == g2




# = = = = = = = = Tipo Resposta = = = = = = = = #
#                                               #
# Uma resposta e' uma lista de tuplos, em que   #
# cada tuplo contem uma palavra no primeiro     #
# elemento e uma coordenada no segundo.         #
#                                               #
# = = = = = = = = = = = = = = = = = = = = = = = #


# 1. Construtor

def resposta(lst):
    '''resposta: lista de tuplos (string, coordenada) -> resposta
       resposta(lst) tem como valor a resposta que contem cada 
       um dos tuplos que compoem a lista lst.'''

    l = lst
    i = 0
    if not isinstance(l, list):
        raise ValueError('resposta: argumentos invalidos')
    elif isinstance(l, list):
        while i < len(l):
            if (not isinstance(l[i], tuple)or len(l[i]) != 2 or \
                not isinstance (l[i][0], str) or not e_coordenada(l[i][1]) ):
                raise ValueError('resposta: argumentos invalidos')
            i = i + 1
        else:
            return lst





# 2. Selectores

def resposta_elemento(res, n):
    '''resposta_elemento: resposta x No -> tuplo (string, coordenada)
       resposta_elemento(res, n) devolve o enesimo elemento da resposta res.'''

    if res == []:
        raise ValueError('resposta_elemento: argumentos invalidos')
    if 0 <= n:
        elem = res[n]
        return elem
    else:
        raise ValueError('resposta_elemento: argumentos invalidos')


       
def resposta_tamanho(res):
    '''resposta_tamanho: resposta -> No
       resposta_tamanho(res) devolve o numero de elementos da resposta res.'''
    
    return len(res)



# 3. Modificador

def acrescenta_elemento(r, s, c):
    '''acrescenta_elemento: resposta x string x coordenada -> resposta
       acrescenta_elemento(r, s, c) devolve a resposta r com mais 
       um elemento - o tuplo (s, c).'''
    
    return r + [(s, c)]




# 4. Reconhecedor

def e_resposta(arg):
    '''e_resposta: universal -> logico
       e_resposta(arg) tem o valor verdadeiro se o arg for 
       do tipo resposta e falso caso contrario.'''

    l = arg
    i = 0
    if not isinstance(l, list):
        return False
    
    elif isinstance(l, list):
        while i < len(l):
            if (not isinstance(l[i], tuple) or len(l[i]) != 2 or \
                not isinstance((l[i][0]), str) or not e_coordenada(l[i][1]) ):
                return False
            i = i + 1
        else:
            return True
        


# 5. Testes

def respostas_iguais(r1, r2):
    '''respostas_iguais: resposta x resposta - logico
       respostas_iguais(r1, r2) devolve o valor verdadeiro se as respostas 
       r1 e r2 contiverem os mesmos tuplos e falso caso contrario.'''

    n = 0
    for i in range(resposta_tamanho(r1)):
        if r1[i] in r2:
            n = n + 1
    return n == resposta_tamanho(r2)


# 6. Outras operacoes

def resposta_string(res):
    '''resposta_string: resposta -> string
       resposta_string(res) devolve a representacao externa da resposta'''
    
    i = 0
    k = 0
    nenhumatroca = False
    maiorindice = len(res) - 1
    palavra = ()
    coord = ()
    stringmedia = ''                 
    stringpalavra = ''
    stringfinal = ''
    
    while not nenhumatroca:
        nenhumatroca = True
        for i in range(maiorindice):
            if not (res[i][0] < res[i+1][0]):
                res[i+1], res[i] = res[i], res[i+1]
                
                nenhumatroca = False
            i = i + 1
    
        
    while k < len(res):
        palavra = res[k][0]
        coord = res[k][1]
        stringpalavra = '<'+ str(palavra) + ':' + coordenada_string(coord) + '>'
        stringmedia = stringmedia + stringpalavra
        
        if (len(res) - k == 1):
            break
        
        stringmedia = stringmedia + ', '

        k = k + 1
    
    stringfinal = '[' + stringmedia + ']'
    return (stringfinal)
    


# Funcoes a implementar    

from janela_sopa_letras import *

def sopa_letras(fich):
    '''sopa_letras : cadeia de caracteres -> resposta
       sopa_letras(fich) tem como resultado a resposta ao puzzle descrito no ficheiro fich '''
    

    file = open(fich , 'r')
    lst_linhas = file.readlines()

    palavrasaprocurar = lst_linhas[1][10:-1]
    matriz = lst_linhas[2:]
    
    grelha = ''
    g = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if ' ' != matriz[i] or '\n' != matriz[i]:
                grelha = grelha + matriz[i]
        g = g + [grelha]

    res = resposta([])
    
    
    janela = janela_sopa_letras(fich)
    janela.mostra_palavras(res)
    janela.termina_jogo()    

    return lst_linhas
    


    
    
        
    
def procura_palavras_numa_direcao(g, p, dir):
    '''procura_palavras_numa_direcao : grelha x lista de strings x direcao ->
       resposta
       procura_palavras_numa_direcao(grelha, palavras, dir) tem como resultado
       a resposta que representa as coordenadas das palavras encontradas na grelha'''
    
    res = resposta([])
    for palavra in p:
        for l in range(grelha_nr_linhas(g)):
            for c in range(grelha_nr_colunas(g)):
                if grelha_elemento(g, l, c) == palavra[0]:
                    elem = grelha_linha(g, coordenada(l, c, dir))

                    if e_norte(dir):
                        if elem[grelha_nr_linhas(g) - 1 - l:len(palavra) + grelha_nr_linhas(g) - 1 - l] == palavra:
                            res = acrescenta_elemento(res, palavra, coordenada(l, c, dir))
                            
                    if e_sul(dir):
                        if elem[l:len(palavra) + l] == palavra:
                            res = acrescenta_elemento(res, palavra, coordenada(l, c, dir)) 
                            
                    if e_oeste(dir):
                        if elem[grelha_nr_colunas(g) - 1 - c:len(palavra) + grelha_nr_colunas(g) - 1 - c] == palavra:
                            res = acrescenta_elemento(res, palavra, coordenada(l, c, dir))
                    if e_leste(dir):
                        
                        if elem[c:len(palavra) + c] == palavra:
                            res = acrescenta_elemento(res, palavra, coordenada(l, c, dir))
                            
                      
    return res


                        
                            
                        
                    
                    
            
        
        
        

            
    
    
    
    
    



