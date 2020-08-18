import math
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
print("GCD of",x,y,"=",math.gcd(x,y))
print("LCM of",x,y,"=",abs(x*y)//math.gcd(x,y))

