#! /usr/bin/python3

a = []
n = 0
C = int(input() )
veiculo = int(input() )

while veiculo != 0:
	lastC = C
	C -= veiculo

	if C < 0:
		C = lastC
	if veiculo > 0 and C != lastC:
		a.append("Seja bem-vindo! Capacidade restante: %d" %C)
	elif veiculo < 0:
		a.append("Volte sempre! Capacidade restante: %d" %C)
	else:
		a.append("Veiculo muito grande! Capacidade restante: %d" %C)

	n+=1
	veiculo = int(input() )

for i in range(n):
	print(a[i])
	
