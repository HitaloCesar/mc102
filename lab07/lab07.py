#Hitalo Cesar Alves
#ra217878

a = int(input() )

b = [[0 for i in range(a)] for j in range(a)]
c = 0

for i in range(1,a+1):
	for j in range(1,a+1):
		if (j%i == 0 or i%j == 0):
			b[i-1][j-1] = "*"
			c+=1
		else:
			b[i-1][j-1] = "-"

for i in range(a):
	for j in range(a):
		print(b[i][j], end = "")
	print("")

print(c)
