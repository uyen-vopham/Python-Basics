a = input("Type a parameter: ")
b = input("Type b parameter: ")
c = input("Type c parameter: ")
numeric = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0","-"]
numeric_negative = ["-1","-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9"]
delta = x1 = x2 = 0

if a in numeric or a in numeric_negative:
    if b in numeric or b in numeric_negative:
        if c in numeric or c in numeric_negative:
            a = int(a)
            b = int(b)
            c = int(c)
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
        else: print("Please type the number only !!")
    else: print("Please type the number only!!")
else:
  print("Please type the number only!!")
