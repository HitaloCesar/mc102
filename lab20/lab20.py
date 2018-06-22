#!/usr/bin/env python3

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

# O aluno pode criar outras funcoes que ache necessario

def acharProxima(matriz, y,x):
    for i in range(y,9):
        for j in range(x,9):
            if matriz[i][j] == 0:
                return i,j

    for i in range(0,9):
        for j in range(0,9):
            if matriz[i][j] == 0:
                return i,j
    return -1,-1

def gerarTransposta(matriz):
    transposta = []
    for i in range(len(matriz) ):
        transposta.append([])
        for j in range(len(matriz) ):
            transposta[i].append(matriz[j][i])

    return transposta

def possivel(matriz,y,x,n):
    if n in matriz[y]:
        return False
    if n in gerarTransposta(matriz)[x]:
        return False

    yS = (y//3)*3
    xS = (x//3)*3
    #checking submatrix
    for i in range(yS,yS+3):
        for j in range(xS,xS+3):
            if matriz[i][j]==n:
                return False

    return True

def devolve(matriz,y=0,x=0):
    y,x = acharProxima(matriz, y,x)
    if y == -1:
        return True
    for w in range(1,10):
        if possivel(matriz, y, x, w):
            matriz[y][x] = w
            if devolve(matriz,y,x):
                return True
            matriz[y][x] = 0
    return False



# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta):
    # Implementar a funcao e trocar o valor de retorno

    #print_sudoku(resposta)
    #print_sudoku(gerarTransposta(resposta) )

    return devolve(resposta)
