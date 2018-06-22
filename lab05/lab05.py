#! /usr/bin/python3

#Hitalo Cesar Alves
#ra217878



class atributos(object):
	__status__ = ["hp", "lastHp", "golpes", "combo", "rounds"]

golpeAtual = 0

ryu = atributos()
ken = atributos()

quemBate = "none"
lastPunch = "none"

ryu.hp = 50
ryu.lastHp = 50
ryu.golpes = []
ryu.combo = 0
ryu.rounds = 0

ken.hp = 50
ken.lastHp = 50
ken.golpes = []
ken.combo = 0
ken.rounds = 0

while (ken.rounds + ryu.rounds) < 2:
	golpeAtual = int(input() )
	lastPunch = quemBate
	if golpeAtual > 0:
		quemBate = "ryu"
		ryu.golpes.append(abs(golpeAtual) )
		ryu.combo += ryu.golpes[-1]
		ken.hp -= ryu.golpes[-1]

	elif golpeAtual < 0:
		quemBate = "ken"
		ken.golpes.append(abs(golpeAtual) )
		ken.combo += ken.golpes[-1]
		ryu.hp -= ken.golpes[-1]

	if quemBate != lastPunch and lastPunch != "none":
		if quemBate == "ryu":
			if ken.combo > 0:
				print("Ryu: " + "%d" %(ryu.hp+ken.combo) + " - " + "%d" %ken.combo + " = %d" %ryu.hp)
			ryu.lastHp = ryu.hp
			ken.combo = 0
		elif quemBate == "ken":
			if ryu.combo > 0:
				print("Ken: " + "%d" %(ken.hp+ryu.combo) + " - " + "%d" %ryu.combo + " = %d" %ken.hp)
			ken.lastHp = ken.hp
			ryu.combo = 0
	
	"""if ken.hp == 0 or ryu.hp == 0:
		if ryu.hp == 0:
			ken.rounds+=1 
		else:
			ryu.rounds+=1

		ryu.hp = 50
		ken.hp = 50
		ryu.lastHp = 50
		ken.lastHp = 50	"""	

	if ken.hp <= 0:

		ryu.rounds+=1
		if ryu.combo > 0:
				print("Ken: " + "%d" %(ken.hp+ryu.combo) + " - " + "%d" %ryu.combo + " = %d" %ken.hp)
		ken.lastHp = ryu.lasthp = 50
		ken.hp = ryu.hp = 50
		ryu.combo = 0		
		
	elif ryu.hp <= 0:
		ken.rounds+=1
		if ken.combo > 0:
			print("Ryu: " + "%d" %(ryu.hp+ken.combo) + " - " + "%d" %ken.combo + " = %d" %ryu.hp)
		ryu.lastHp = ken.lastHp = 50
		ryu.hp = ken.hp = 50
		ken.combo = 0

if ryu.rounds > ken.rounds:
	print("Ryu venceu")
elif ken.rounds > ryu.rounds:
	print("Ken venceu")
else:
	print("empatou")










		
	
