def imprimir():
	listaAux = []
	for i in range(len(lista) ):
		listaAux.append(str(lista[i]) )
	if listaAux == []:
		return
	print(" ".join(listaAux) + " " )
	

def ordenarCrescente():
	for i in range(len(lista) ):
		for j in range(len(lista)-1 ):
			if lista[j+1] < lista[j]:
				aux = lista[j+1]
				lista[j+1] = lista[j]
				lista[j] = aux
				
def ordenarDecrescente():
	for i in range(len(lista) ):
		for j in range(len(lista)-1 ):
			if lista[j+1] > lista[j]:
				aux = lista[j+1]
				lista[j+1] = lista[j]
				lista[j] = aux

		
	

def buscaBinaria(ra):
	if tipoOrdenacao == "nada":
		print("Vetor nao ordenado!")
		return

	ra = int(ra)
	indx = []
	minSub = 0
	maxSub = len(lista) -1
	while True:
		indx.append((minSub+maxSub)//2)
		if ra not in lista and (maxSub == minSub or minSub>maxSub):
			listaAux = indx[:]
			listaAux.remove(listaAux[-1])
			if indx[-1] in listaAux:
				indx[-1] = "#"
				indx.remove("#")
				
			break
		elif tipoOrdenacao == "cres":
			if lista[indx[-1]] > ra:
				maxSub = indx[-1] - 1
			elif lista[indx[-1]] < ra:
				minSub = indx[-1] + 1
			elif lista[indx[-1]] == ra:
				break
		elif tipoOrdenacao == "dcres":
			if lista[indx[-1]] < ra:
				maxSub = indx[-1] - 1
			elif lista[indx[-1]] > ra:
				minSub = indx[-1] + 1
			elif lista[indx[-1]] == ra:
				break



	for i in range(len(indx) ):
		indx[i] = str(indx[i])

	print(" ".join(indx) + " " )

	if ra not in lista:
		print("%s nao esta na lista!"%(ra))
		return

	print("%d esta na posicao: %s"%(ra, indx[-1]))				
	

	

def inserir(ra):
	if int(ra) in lista and len(lista) < 150:
		print("Aluno ja matriculado na turma!")
		return
	elif len(lista) >= 150:
		print("Limite de vagas excedido!")
		return

	lista.append(int(ra) )

	if tipoOrdenacao == "cres":
		ordenarCrescente()

	elif tipoOrdenacao == "dcres":
		ordenarDecrescente()

def remover(ra):
	if len(lista) == 0:
		print("Nao ha alunos cadastrados na turma!")

	elif int(ra) in lista:
		lista.remove(int(ra) )

	else:
		print("Aluno nao matriculado na turma!")
			
tipoOrdenacao = "nada"

lista = input().split()

for i in range(len(lista) ):
	lista[i] = int(lista[i])

while True:
	comando = input().split()
	if comando[0] == "p":
		imprimir()
	if comando[0] == "c":
		tipoOrdenacao = "cres"
		ordenarCrescente()
	if comando[0] == "d":
		tipoOrdenacao = "dcres"
		ordenarDecrescente()
	if comando[0] == "b":
		buscaBinaria(comando[1])
	if comando[0] == "i":
		inserir(comando[1])
	if comando[0] == "r":
		remover(comando[1])
	if comando[0] == "s":
		break
