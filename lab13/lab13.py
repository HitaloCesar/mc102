#!/usr/bin/env python3
#Hitalo Cesar Alves
#ra217878

#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
	jogo = jogo.split()
	for i in range(len(tabela) ):
		if jogo[0] in tabela[i]:
			tabela[i][4] += int(jogo[1])
			tabela[i][3] += int(jogo[1])
			tabela[i][3] -= int(jogo[3])
			if int(jogo[1]) > int(jogo[3]):
				tabela[i][2]+=1
				tabela[i][1]+=3
			elif int(jogo[1]) == int(jogo[3]):
				tabela[i][1]+=1 
		if jogo[4] in tabela[i]:
			tabela[i][4] += int(jogo[3])
			tabela[i][3] += int(jogo[3])
			tabela[i][3] -= int(jogo[1])
			if int(jogo[3]) > int(jogo[1]):
				tabela[i][2]+=1
				tabela[i][1]+=3
			elif int(jogo[1]) == int(jogo[3]):
				tabela[i][1]+=1 
		
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
	if int(time1[1]) > int(time2[1]):
		return 1
	if int(time1[1]) < int(time2[1]):
		return -1

	if int(time1[2]) > int(time2[2]):
		return 1
	if int(time1[2]) < int(time2[2]):
		return -1

	if int(time1[3]) > int(time2[3]):
		return 1
	if int(time1[3]) < int(time2[3]):
		return -1

	if int(time1[4]) > int(time2[4]):
		return 1
	if int(time1[4]) < int(time2[4]):
		return -1
	
		
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
	for j in range(len(tabela) ):
		for i in range(len(tabela)-1,0,-1 ):
			if comparaTimes(tabela[i], tabela[i-1]) == 1:
				tabelaLast = tabela[i][:]
				tabelaPreLast = tabela[i-1][:]
				tabela[i] = tabelaPreLast
				tabela[i-1] = tabelaLast
			
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
	for i in range(len(tabela) ):
		print(tabela[i][0]+', '+ str(tabela[i][1])+', '+ str(tabela[i][2]) + ', ' + str(tabela[i][3]) + ', ' + str(tabela[i][4]) )
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
