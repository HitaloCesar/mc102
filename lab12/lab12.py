#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome:
# RA:

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda) 
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario 
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
    # Implementar a funcao e trocar o valor de retorno
	if rot:
		largura = a
		altura = l
	else:
		largura = l
		altura = a
	
	extremoDirInicial = x+(largura-1)
	extremoEsqInicial = x

	if desl >= 0:
		posicaoFinal = x+desl
		if extremoDirInicial+desl > 9:
			posicaoFinal = 9-(largura-1)
	elif desl < 0:
		posicaoFinal = x+desl
		if extremoEsqInicial+desl < 0:
			posicaoFinal = 0

		
	
	return largura, altura, posicaoFinal

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro 
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):
    # Implementar a funcao e trocar o valor de retorno
	for j in range(len(mat)-1,-1,-1 ):
		for i in range(x,x+l):
			if mat[j][i] == 1:
				alturaFinal = j+1
				return alturaFinal

	alturaFinal = 0
	return alturaFinal

# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
	if a+y > 10:
		return 0
	else:
		return 1

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro 
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):
    # Implementar a funcao
	for i in range(y,y+a):
		for j in range(x, x+l):
			mat[i][j] = 1

# Funcoes: atualiza_matriz
# 
#    mat: matriz do tabuleiro 
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):
    # Implementar a funcao e trocar o valor de retorno
	linhas = 0
	for i in range(len(mat) ):
		for q in range(len(mat) ):
			if 0 not in mat[i]:
				linhas+=1
				for j in range(i,9):
					mat[j] = mat[j+1][:]
				mat[9] = [0 for k in range(10)]
	return linhas





