# a,b,c are quadratic equation coefficients
a=int(input("enter a value of a :"))
b=int(input("enter a value of b:"))
c=int(input("enter a value of c:"))
d=b**2-4*a*c
if d>0:
    print("real and distinct roots")
elif d==0:
    print("real and equal roots")
else:
    print("imaginary roots")

