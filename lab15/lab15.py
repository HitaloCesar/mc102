#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno
    if num in conj:
        return True
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    for i in range(len(conj1) ):
        if conj1[i] not in conj2:
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao
    if num not in conj:
        conj.append(num)
    return

def subtracao(conj, num):
    # Implementar a funcao
    if num not in conj:
        return

    conj.remove(num)
    return

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    uniao = conj1+conj2
    aux = uniao[:]
    for i in range(len(uniao) ):
        if uniao[i] in aux:
            aux.remove(uniao[i])
        if uniao[i] not in aux:
            aux.append(uniao[i])
    return aux

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    listaMaior = conj1 if len(conj1) > len(conj2) else conj2  
    final = []
    for i in range(len(listaMaior) ):
        if listaMaior[i] in conj1 and listaMaior[i] in conj2:
            final.append(listaMaior[i])
        
    return final

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    fim = conj1[:]
    for i in conj2:
        if i in conj1:
            fim.remove(i)
    return fim

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    A = conj1
    B = conj2
    
    return diferenca(conj1,conj2) + diferenca(B,A) 
