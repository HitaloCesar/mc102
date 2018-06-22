import sys

def arqToList(arquivo):
    arquivo = list(arquivo)
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].split()
        for j in range(len(arquivo[i])):
            try:
                arquivo[i][j] = int(arquivo[i][j])
            except:
                pass
    return arquivo

def p(matriz,y,x):
    return matriz[y][x]

def p1(matrizA,y,x):
    global matrix
    global D

    if x <= 0 or y <= 0 or y >= len(matrizA)-1 or x >= len(matrizA[0])-1:
        return p(matrizA,y,x)
    
    lista = []
    for k in range(y-1,y+2):
        for l in range(x-1,x+2):
           a = matrizA[k][l]
           b = matrix[k-y+1][l-x+1]
           d = a*b
           lista.append(d)
    final = sum(lista)/D
    if final<=0:
        return 0
    if final >=255:
        return 255
    return int(final)
###################################################################
imagem = arqToList(open(sys.argv[1]))
matrix = arqToList(open(sys.argv[2]))

D = matrix[0][0]
matrix.remove(matrix[0])

apendix = []
for i in range(3):
    apendix.append(imagem[i])

del imagem[0:3]

imagemCopia = []
for i in range(len(imagem)):
    imagemCopia.append(imagem[i][:])

##################################################################

for i in range(len(imagemCopia)):
    for j in range(len(imagemCopia[i])):
        imagemCopia[i][j] = p1(imagem,i,j)

for i in range(len(imagemCopia)):
    for j in range(len(imagemCopia[i]) ):
        imagemCopia[i][j] = str(imagemCopia[i][j])

for i in range(3):
    for j in range(len(apendix[i])):
        try:
            apendix[i][j] = str(apendix[i][j])
        except:
            pass
for i in range(3):
    print(" ".join(apendix[i]))


for i in range(len(imagemCopia)):
    print(" ".join(imagemCopia[i])+"  ")
