#RootsOfAQuadraticEquation

#find the roots r1 , r2 of the equation aX**2+bX+c = 0

a = int(input())
b = int(input())
c = int(input())

r1 = ((-b) + (b**2 - 4*a*c)**0.5)/(2*a)
print(round(r1,2))
r2 = ((-b) - (b**2 - 4*a*c)**0.5)/(2*a)
print(round(r2,2))