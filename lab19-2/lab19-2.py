
def ataque(tabuleiro,y,x):
    try:
        if tabuleiro[y][x] == "@":
            tabuleiro[y][x] = "-"
        else:
            return tabuleiro
    except:
        return tabuleiro
        pass
    try:
        if tabuleiro[y-1][x] == "@" and y >= 1:
            tabuleiro = ataque(tabuleiro,y-1,x)
    except:
        pass
    try:
        if tabuleiro[y+1][x] == "@":
            tabuleiro = ataque(tabuleiro,y+1,x)
    except:
        pass
    try:
        if tabuleiro[y][x-1] == "@" and x >=1:
            tabuleiro = ataque(tabuleiro,y,x-1)
    except:
        pass
    try:
        if tabuleiro[y][x+1] == "@":
            tabuleiro = ataque(tabuleiro,y,x+1)
    except:
        pass

    return tabuleiro

def isValido():
    global tabJog1
    global tabJog2

    flagTable1 = True
    flagTable2 = True

    for i in range(len(tabJog1)):
        if "@" in tabJog1[i]:
            break
    if i == len(tabJog1)-1 and "@" not in tabJog1[i]:
        flagTable1 = False

    for i in range(len(tabJog2)):
        if "@" in tabJog2[i]:
            break
    if i == len(tabJog2)-1 and "@" not in tabJog2[i]:
        flagTable2 = False

    return flagTable1 and flagTable2




###############################################
valores = input().split("x")
for i in range(2):
    valores[i] = int(valores[i])


tabJog1 = []
tabJog2 = []

for i in range(valores[0]):
    tabJog1.append(list(input()) )
    
for i in range(valores[0]):
    tabJog2.append(list(input()) )

count = 0
while isValido():
    a = input().split(",")
    if count%2 == 0:
        tabJog2 = ataque(tabJog2,int(a[0])-1,int(a[1])-1 )
        print("Ataque em (%s,%s) do jogador 1" %(a[0], a[1]))
        for i in range(len(tabJog2)):
            print("".join(tabJog2[i]))
    else:
        tabJog1 = ataque(tabJog1,int(a[0])-1,int(a[1])-1 )
        print("Ataque em (%s,%s) do jogador 2" %(a[0], a[1]))
        for i in range(len(tabJog1)):
            print("".join(tabJog1[i]))
    count+=1
