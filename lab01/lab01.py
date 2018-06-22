pi = 3.14

#print("Digite a distancia em estadios")
dist = float(input())
#print("Digite o angulo em graus")
ang = float(input())*2*pi/360

Ce = 2*pi*dist/ang
Ckm = 176.4*Ce/1000

print("%.1f" % float(Ce) )
print("%.1f" % float(Ckm) )
