a = input("Type a parameter: ")
b = input("Type b parameter: ")
c = input("Type c parameter: ")
numeric = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
sign = ["-", "+"]

delta = x1 = x2 = 0
flag_a = flag_b = flag_c = True

list_a = list(a)
list_b = list(b)
list_c = list(c)

if list_a.count(".") > 1: flag_a = False
if list_b.count(".") > 1: flag_b = False
if list_c.count(".") > 1: flag_c = False

if list_a[0] in numeric or list_a[0] in sign: pass
if list_b[0] in numeric or list_b[0] in sign: pass
if list_c[0] in numeric or list_c[0] in sign: pass

for i in range (1, len(list_a)):
    if list_a[i] in numeric: pass
    else: flag_a = False
for i in range (1, len(list_b)):
    if list_b[i] in numeric: pass
    else: flag_b = False
for i in range (1, len(list_c)):
    if list_c[i] in numeric: pass
    else: flag_c = False

if flag_a and flag_b and flag_c:
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
else:
  print("Please type the number only!!")

