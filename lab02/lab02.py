vi = int(input() )
xi = int(input() )
yi = int(input() )
xf = int(input() )
yf = int(input() )
t = int(input() )
cd = int(input() )
pr = int(input() )



d = (xf - xi) + (yf - yi)
VC = vi+(d*t)
if cd > (VC*pr/100):
	VD = cd
else:
	VD = VC*pr/100
VF = VC - VD

print("%.2f" % VF)
