
#  Funcao: removePalavras
# 
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
# 
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
    texto = s[:]
    texto = texto.split()
    for i in range(len(vs) ):
        while vs[i] in texto:
            texto.remove(vs[i])
    texto =  " ".join(texto)
    return texto

#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(palavrasPagina, termosBusca):
    ignore = False
    for i in range(len(palavrasPagina) ):
        palavrasPagina[i] = palavrasPagina[i].split()
    lista = []

    for i in range(len(palavrasPagina) ):
        for j in range(len(termosBusca) ):
            if termosBusca[j] not in palavrasPagina[i] :
                lista.append(0)
                ignore = True
                break
        if ignore == False:
            lista.append(1)
        ignore = False
    

    return lista
	

#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas 
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
    numLinks = []
    for i in range(len(resp) ):
        if resp[i] == 0:
            numLinks.append(-1)
        else:
            cont = 0
            for j in range(len(links) ):
                if links[j][i] == 1 and resp[j] == 1:
                    cont+=1
            numLinks.append(cont)


    return numLinks
