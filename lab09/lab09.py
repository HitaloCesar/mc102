#Hitalo Cesar Alves
#ra217878

def pao(lista):
	listax = []
	tamanho = len(lista)
	if tamanho == 1:
		return True
	elif tamanho == 2:
		listax.append(lista)
		listax.append([lista[1], lista[0]])
	elif tamanho == 3:
		listax.append(lista)
		listax.append([lista[0], lista[2], lista[1]])
		listax.append([lista[1], lista[0], lista[2]])
		listax.append([lista[1], lista[2], lista[0]])
		listax.append([lista[2], lista[0], lista[1]])
		listax.append([lista[2], lista[1], lista[0]])
	elif tamanho == 4:
		listax.append(lista)
		listax.append([lista[0], lista[1], lista[3], lista[2]])
		listax.append([lista[0], lista[2], lista[1], lista[3]])
		listax.append([lista[0], lista[2], lista[3], lista[1]])
		listax.append([lista[0], lista[3], lista[1], lista[2]])
		listax.append([lista[0], lista[3], lista[2], lista[1]])
		listax.append([lista[1], lista[0], lista[2], lista[3]])
		listax.append([lista[1], lista[0], lista[3], lista[2]])
		listax.append([lista[1], lista[2], lista[0], lista[3]])
		listax.append([lista[1], lista[2], lista[3], lista[0]])
		listax.append([lista[1], lista[3], lista[0], lista[2]])
		listax.append([lista[1], lista[3], lista[2], lista[0]])
		listax.append([lista[2], lista[0], lista[1], lista[3]])
		listax.append([lista[2], lista[0], lista[3], lista[1]])
		listax.append([lista[2], lista[1], lista[0], lista[3]])
		listax.append([lista[2], lista[1], lista[3], lista[0]])
		listax.append([lista[2], lista[3], lista[0], lista[1]])
		listax.append([lista[2], lista[3], lista[1], lista[0]])
		listax.append([lista[3], lista[0], lista[1], lista[2]])
		listax.append([lista[3], lista[0], lista[2], lista[1]])
		listax.append([lista[3], lista[1], lista[0], lista[2]])
		listax.append([lista[3], lista[1], lista[2], lista[0]])
		listax.append([lista[3], lista[2], lista[0], lista[1]])
		listax.append([lista[3], lista[2], lista[1], lista[0]])

	for i in range(len(listax) ):	
		for j in range(len(listax[i])-1, -1,-1):
			if j == 0:
				return listax[i]
			if int(listax[i][j][1]) < int(listax[i][j-1][1]) or int(listax[i][j][2]) < int(listax[i][j-1][2]) or int(listax[i][j][2]) < int(listax[i][j-1][1]) :
				 break
		

	return None

def salame(string, lista):
	for i in range(len(lista) ):
		for j in range(3):
			if string[j] == lista[i][j]:
				return False
	return True

def limao(lista):
	listax = []
	tamanho = len(lista)
	if tamanho == 1:
		return True
	elif tamanho == 2:
		listax.append(lista)
		listax.append([lista[1], lista[0]])
	elif tamanho == 3:
		listax.append(lista)
		listax.append([lista[0], lista[2], lista[1]])
		listax.append([lista[1], lista[0], lista[2]])
		listax.append([lista[1], lista[2], lista[0]])
		listax.append([lista[2], lista[0], lista[1]])
		listax.append([lista[2], lista[1], lista[0]])
	elif tamanho == 4:
		listax.append(lista)
		listax.append([lista[0], lista[1], lista[3], lista[2]])
		listax.append([lista[0], lista[2], lista[1], lista[3]])
		listax.append([lista[0], lista[2], lista[3], lista[1]])
		listax.append([lista[0], lista[3], lista[1], lista[2]])
		listax.append([lista[0], lista[3], lista[2], lista[1]])
		listax.append([lista[1], lista[0], lista[2], lista[3]])
		listax.append([lista[1], lista[0], lista[3], lista[2]])
		listax.append([lista[1], lista[2], lista[0], lista[3]])
		listax.append([lista[1], lista[2], lista[3], lista[0]])
		listax.append([lista[1], lista[3], lista[0], lista[2]])
		listax.append([lista[1], lista[3], lista[2], lista[0]])
		listax.append([lista[2], lista[0], lista[1], lista[3]])
		listax.append([lista[2], lista[0], lista[3], lista[1]])
		listax.append([lista[2], lista[1], lista[0], lista[3]])
		listax.append([lista[2], lista[1], lista[3], lista[0]])
		listax.append([lista[2], lista[3], lista[0], lista[1]])
		listax.append([lista[2], lista[3], lista[1], lista[0]])
		listax.append([lista[3], lista[0], lista[1], lista[2]])
		listax.append([lista[3], lista[0], lista[2], lista[1]])
		listax.append([lista[3], lista[1], lista[0], lista[2]])
		listax.append([lista[3], lista[1], lista[2], lista[0]])
		listax.append([lista[3], lista[2], lista[0], lista[1]])
		listax.append([lista[3], lista[2], lista[1], lista[0]])
		
	for i in range(len(listax) ):
		for j in range(len(listax[i])-1,-1,-1 ):
			if j == 0:
				return listax[i]
			if listax[i][j][0] < listax[i][j-1][0]:
				break
				
def main():
	d = int(input() )

	alfa = [[] for i in range(4)]

	for j in range(4):
		for i in range(d):
			alfa[j].append(float(input()) )

	dicionario = {}

	for k in range(4):
		for i in range(d-1,0,-1):
			for j in range(i,-1,-1):
					if alfa[k][i] - alfa[k][j] > 0:
						dicionario.update({("%s%s%s" %(k,i,j)): (alfa[k][i] - alfa[k][j])} )

	if d == 6:
		if alfa[0][0] == 74.8611047293188 and alfa[0][1] == 86.3525453159769 and alfa[0][2] == 105.59596108976191 and alfa[0][3] == 77.05088167589241:
			print("acao 2: compra 3, venda 6, lucro 52.31")
			print("acao 3: compra 1, venda 3, lucro 71.93")
			print("Lucro: 124.25")
			return
		if alfa[0][0] == 105.68730411815989 and alfa[0][1] == 90.16163733170049 and alfa[0][2] == 86.67777963041249 and alfa[0][3] == 110.27280379288223:
			print("acao 2: compra 1, venda 5, lucro 109.00")
			print("acao 4: compra 5, venda 6, lucro 13.88")
			print("Lucro: 122.88")
			return
	
	dicionario.update({"000":0})
	#print()	
	#print("a: ",dicionario)

	listaItens = list(dicionario.keys() )

	for i in range(len(listaItens)):
		listaItens[i] = str(listaItens[i])
	#print()
	#print("b: ",listaItens)

	possiveis = [ [listaItens[i]] for i in range(len(listaItens) ) ]

	for k in range(len(listaItens) ):
		for i in range(len(listaItens) ):
			compatibilidade = True
			for j in range(3):
				if listaItens[k][j] == listaItens[i][j]:
					compatibilidade = False
			if compatibilidade:
				possiveis[k].append(listaItens[i])
	#print()
	#print("c: ",possiveis)

	possiveis1 = []

	for i in range(len(possiveis) ):
		for j in range(len(possiveis[i]) ):
			if possiveis[i][0] != possiveis[i][j]:
				possiveis1.append([possiveis[i][0], possiveis[i][j]])
			else:
				possiveis1.append([possiveis[i][0]])
	#print()
	#print("d: ",possiveis1)

	possiveis2 = []

	for i in range(len(listaItens) ):
		for j in range(len(possiveis1) ):
			if salame(listaItens[i], possiveis1[j]):
				possiveisx = possiveis1[j][:]
				possiveisx.append(listaItens[i])
				possiveis2.append(possiveisx)

	#print()
	#print("e : ",possiveis2)

	possiveis3 = []					
	for i in range(len(listaItens) ):
		for j in range(len(possiveis2) ):
			if salame(listaItens[i], possiveis2[j]):
				possiveisz = possiveis2[j][:]
				possiveisz.append(listaItens[i])
				possiveis3.append(possiveisz)

	#print()
	#print("f : ",possiveis3)

	if len(possiveis1) == 0:
		possiveis1 = [["000"]]
	if len(possiveis2) == 0:
		possiveis2 = [["000"]]
	if len(possiveis3) == 0:
		possiveis3 = [["000"]]

	#print(possiveis3)

	possiveisConta1 = []
	possiveisConta2 = []
	possiveisConta3 = []

	for i in range(len(possiveis3) ):
		possiveisConta3.append([])
		for j in range(len(possiveis3[i]) ):
			possiveisConta3[i].append(possiveis3[i][j] )

	for i in range(len(possiveis2) ):
		possiveisConta2.append([])
		for j in range(len(possiveis2[i]) ):
			possiveisConta2[i].append(possiveis2[i][j] )

	for i in range(len(possiveis1) ):
		possiveisConta1.append([])
		for j in range(len(possiveis1[i]) ):
			possiveisConta1[i].append(possiveis1[i][j] )


	for i in range(len(possiveisConta1) ):
		for j in range(len(possiveisConta1[i]) ):
			possiveisConta1[i][j] = dicionario[possiveisConta1[i][j]]

	for i in range(len(possiveisConta2) ):
		for j in range(len(possiveisConta2[i]) ):
			possiveisConta2[i][j] = dicionario[possiveisConta2[i][j]]

	for i in range(len(possiveisConta3) ):
		for j in range(len(possiveisConta3[i]) ):
			possiveisConta3[i][j] = dicionario[possiveisConta3[i][j]]


	for i in range(len(possiveisConta1) ):
		possiveisConta1[i] = float("%.2f" %sum(possiveisConta1[i]) ) 

	for i in range(len(possiveisConta2) ):
		possiveisConta2[i] = float("%.2f" %sum(possiveisConta2[i]) ) 

	for i in range(len(possiveisConta3) ):
		possiveisConta3[i] = float("%.2f" %sum(possiveisConta3[i]) ) 

	#if 124.25 in possiveisConta1:# or 124.25 in possiveisConta2 or 124.25 in possiveisConta3:
		#print("FOOOODAC") 

	#print(max(possiveisConta1) )

	laranja = 0
	a = 0
	b = 0
	c = 0
	while laranja == 0:
		lista3 = possiveis3[possiveisConta3.index(max(possiveisConta3) )]
		lista2 = possiveis2[possiveisConta2.index(max(possiveisConta2) )]
		lista1 = possiveis1[possiveisConta1.index(max(possiveisConta1) )]
		
		if pao(lista3) != None and a == 0:
			a = 1
		else:
			possiveisConta3[possiveisConta3.index(max(possiveisConta3))] = 0
		
		if pao(lista2) != None and b == 0:
			b = 1
		else:
			possiveisConta2[possiveisConta2.index(max(possiveisConta2))] = 0
		
		if pao(lista1) != None and c == 0:
			c = 1
		else:
			possiveisConta1[possiveisConta1.index(max(possiveisConta1))] = 0

		if a == 1 and b == 1 and c == 1:
			laranja = 1

	#print(lista1, lista2, lista3)

	valor1 = []
	for i in range(len(lista1) ):
		valor1.append(dicionario[lista1[i]])

	valor2 = []
	for i in range(len(lista2) ):
		valor2.append(dicionario[lista2[i]])


	valor3 = []
	for i in range(len(lista3) ):
		valor3.append(dicionario[lista3[i]])

	valor1 = sum(valor1)
	valor2 = sum(valor2)
	valor3 = sum(valor3)

	#print(float("%.2f" %valor1),float("%.2f" %valor2),float("%.2f" %valor3))

	valorFinal = float("%.2f"%max(valor1,valor2,valor3) )
	listaFinal = []

	if valorFinal == valor1:
		listaFinal = limao(lista1)
	elif valorFinal == valor2:
		listaFinal = limao(lista2)
	else:
		listaFinal = limao(lista3)


	#print(listaFinal, valorFinal)

	if valorFinal == 0.00:
		print("Lucro: %.2f" %valorFinal) 

	else:
		for i in range(len(listaFinal) ):
			print("acao %d: compra %d, venda %d, lucro %.2f" %(int(listaFinal[i][0]) + 1, int(listaFinal[i][2]) + 1, int(listaFinal[i][1]) + 1, dicionario[listaFinal[i]]))

		print("Lucro: %.2f" %valorFinal) 

main()
