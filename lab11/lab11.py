#Hitalo Cesar Alves
#ra217878

def contadorTermos(lista, termo):
	k = 0
	for i in lista:
		if i == termo:
			k+=1
	return k

tamanho = input().split()
linhas = int(tamanho[0])
colunas = int(tamanho[1])
dias = int(input() )

matriz = []
matriz.append(["0" for i in range(colunas+2)] )

for i in range(linhas):
	matriz.append(input().split() )
	matriz[i+1].insert(0, "0")
	matriz[i+1].append("0")

matriz.append(["0" for i in range(colunas+2)] )

print("iteracao 0")
for i in range(1,len(matriz)-1 ):
	print("".join(matriz[i][1:colunas+1] ) )

for q in range(dias):

	"""for i in range(len(matriz) ):
		print(matriz[i])"""

	matrizAux = []
	for i in range(1, len(matriz)-1 ):
		matrizAux.append([])
		for j in range(1, colunas+1):
			matrizAux[i-1].append([matriz[i][j],matriz[i-1][j-1], matriz[i-1][j],matriz[i-1][j+1],matriz[i][j-1],matriz[i][j+1],matriz[i+1][j-1], matriz[i+1][j],matriz[i+1][j+1] ])

	"""for i in range(len(matrizAux) ):
		print(matrizAux[i] )"""

	matrizAux2 = [ [] for i in range(linhas) ]

	for i in range(len(matrizAux) ):
		for j in range(len(matrizAux[i]) ):
			if matrizAux[i][j][0] == "1": #humano
				if "2" in matrizAux[i][j]:
					matrizAux2[i].append("2")
				else:
					matrizAux2[i].append("1")		
		
			elif matrizAux[i][j][0] == "2": #zumbi
				if contadorTermos(matrizAux[i][j], "1") >= 2:
					matrizAux2[i].append("0")
				elif contadorTermos(matrizAux[i][j], "1") == 0:
					matrizAux2[i].append("0")
				else:
					matrizAux2[i].append("2")			

			elif matrizAux[i][j][0] == "0": #vazio
				if contadorTermos(matrizAux[i][j], "1") == 2:
					matrizAux2[i].append("1")
				else:
					matrizAux2[i].append("0")

	print("iteracao %d" %(q+1) )
	for i in range(len(matrizAux2) ):
		print("".join(matrizAux2[i] ) )

	matriz = matrizAux2
	matriz.insert(0, ["0" for i in range(colunas+2)])
	matriz.append(["0" for i in range(colunas+2)])
	
	for i in range(1,linhas+1):
		matriz[i].append("0")
		matriz[i].insert(0, "0")
	
	"""for i in range(len(matriz) ):
		print(matriz[i] )"""


	



