
def procura(funcionario):
    global matriz
    global lista
    if "1" not in matriz[funcionario]:
        return
    
    for i in range(len(matriz[funcionario])):
        if matriz[funcionario][i] == "1":
            lista.append(i)
            procura(i)



linha1 = input()

linha1 = linha1.split()
for i in range(2):
    linha1[i] = int(linha1[i])
matriz = []
for i in range(linha1[0]):
    matriz.append(input().split())

lista = []
procura(linha1[1])

lista.sort()
lista.insert(0,linha1[1])
for i in range(len(lista)):
    lista[i] = str(lista[i])

lista = " ".join(lista)

print(lista)

