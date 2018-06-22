#! /usr/bin/env python3

p1 = float(input() )
p2 = float(input() )
Ml = float(input() )
Mp = (2*p1+3*p2)/5

if (Mp < 5.0 and Mp > 2.5) or (Ml < 5 and Ml > 2.5):
	ex = float(input() )
	M = min(Mp, 4.9)
	F = (M+ex)/2
else:
	M = (3*Mp+2*Ml)/5
	F = M
print("%.1f" %Mp)
print("%.1f" %M)
print("%.1f" %F)
