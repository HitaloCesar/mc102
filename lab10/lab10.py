#Hitalo Cesar Alves
#ra217878
listaPontuacoes = [",", ".", "?", "!", ":"]

texto = input()

listaTextoOriginal = texto.split()



def apagar(palavra):
	for k in range(len(listaTextoOriginal) ):
		listaAuxiliar = [listaTextoOriginal[i].lower() for i in range(len(listaTextoOriginal) )]
		palavra = palavra.lower()
		palavrasPontuadas = [palavra]
		for i in range(len(listaPontuacoes) ):
			palavrasPontuadas.append(palavra + listaPontuacoes[i] )

		for i in range(len(palavrasPontuadas) ):
			if palavrasPontuadas[i] in listaAuxiliar:
				listaTextoOriginal.remove(listaTextoOriginal[listaAuxiliar.index(palavrasPontuadas[i])])


	return



def inverter(palavra):
	listaAuxiliar = [listaTextoOriginal[i].lower() for i in range(len(listaTextoOriginal) )]
	palavra = palavra.lower()
	listaIndices = []
	for i in range(len(listaTextoOriginal) ):
		if palavra in listaAuxiliar[i]:
			listaIndices.append(i)
	#print("aaa:" ,listaIndices)
	for j in listaIndices:
		palavraFinal = listaTextoOriginal[j]
		palavraInvertida = []
		for i in range(len(palavraFinal) ):
			palavraInvertida.append(palavraFinal[len(palavra) - (i+1)])
		palavraInvertida = ''.join(palavraInvertida)
		palavrasPontuadas = [palavra]
		for i in range(len(listaPontuacoes) ):
			palavrasPontuadas.append(palavra + listaPontuacoes[i] )
		for i in range(len(palavrasPontuadas) ):
			if i != 0:
				acento = palavrasPontuadas[i][-1]
			else:
				acento = ''

			if palavrasPontuadas[i] in listaAuxiliar:
				listaTextoOriginal.remove(listaTextoOriginal[j] )
				listaTextoOriginal.insert(j, palavraInvertida )
				break
				
	return

def substituir(palavraVelha, palavraNova):
	for k in range(len(listaTextoOriginal) ):
		listaAuxiliar = [listaTextoOriginal[i].lower() for i in range(len(listaTextoOriginal) )]
		palavraVelha = palavraVelha.lower()
		palavrasPontuadas = [palavraVelha]
		for i in range(len(listaPontuacoes) ):
			palavrasPontuadas.append(palavraVelha + listaPontuacoes[i] )
		for i in range(len(palavrasPontuadas) ):
			if palavrasPontuadas[i] in listaAuxiliar:
				if i != 0:
					acento = palavrasPontuadas[i][-1]
				else:
					acento = ''

				listaTextoOriginal.remove(listaTextoOriginal[listaAuxiliar.index(palavrasPontuadas[i])] )
				listaTextoOriginal.insert(listaAuxiliar.index(palavrasPontuadas[i]), palavraNova+("%s" %acento) )

	return




print(texto)



instrucao = None
while instrucao != "Q":
	instrucao = input()
	if instrucao == "D":
		apagar(input() )
	if instrucao == "I":
		inverter(input() )
	if instrucao == "R":
		substituir(input(), input() )
	if instrucao == "Q":
		break

	print(" ".join(listaTextoOriginal ) )



