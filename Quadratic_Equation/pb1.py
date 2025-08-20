a = input("Type a parameter: ")
b = input("Type b parameter: ")
c = input("Type c parameter: ")
delta = x1 = x2 = 0


a = float(a)
b = float(b)
c = float(c)
if a == 0:
    x2 = -c/b
    print("Equation is first degree equation, and has the root x is: ",x2)
else:
    delta = b**2 - 4*a*c

if delta < 0: print("No root") 
elif delta == 0:
    x1 = x2 = -b/(2*a)
    print ("x1 = x2 = ", x1)
else:
    x1 = (-b-delta**(1/2))/(2*a)
    x2 = (-b+delta**(1/2))/(2*a)
    print("x1 is: ", x1)
    print("x2 is: ", x2)

