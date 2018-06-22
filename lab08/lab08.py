

def quebraLinha(string):
	ints = [int(i) for i in string.split()]
	return ints
def fodac(numero):
	if numero%1 == 0:
		return int(numero)
	else:
		return int(numero) +1
	

N = int(input() )

a = []

for i in range(N):
	b = input()
	a.append([quebraLinha(b)[0], quebraLinha(b)[2]/quebraLinha(b)[1]] )

c=[]
d=[]

for i in range(N):
	if a[i][0] in d:
		continue
	d.append(a[i][0])
	for j in range(N):
		if a[i][0] == a[j][0]:
			c.append(a[j])

#print(c)

s = c[0][1]
n = 1
e = []
for i in range(len(c) ):
	if i+1 == len(c):
		e.append([c[i][0], s/n])
		break
	elif c[i][0] == c[i+1][0]:
		s+=c[i+1][1]
		n+=1		
	else:
		e.append([c[i][0], s/n])
		n = 1
		s = c[i+1][1]



#print(e)


dictionary = {}
for i in range(len(e) ):
	dictionary.update({e[i][0]: e[i][1]})
z = 1
z1 = 1
while z1 != 0:
	z = quebraLinha(input() )
	z1 = z[0]
	if z1 == 0:
		break
	print(fodac(dictionary[z1]*z[1]))



