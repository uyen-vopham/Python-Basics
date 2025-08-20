a = input("Type a parameter: ")
b = input("Type b parameter: ")
c = input("Type c parameter: ")
numeric = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
sign = ["-", "+"]
delta = x1 = x2 = 0



def check_number(list_num):
    flag = True
    list_num=list(list_num)
    if list_num.count(".")>1: flag = False
    if list_num[0] in numeric or list_num[0] in sign: pass

    for i in range(1, len(list_num)):
        if list_num[i] in numeric: continue
        else: flag = False
    return flag
    
def calculate_quadratic_equation(a, b, c):
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

list_a = check_number(a)
list_b = check_number(b)
list_c = check_number(c)
if list_a and list_b and list_c:
    calculate_quadratic_equation(a, b, c)
else: 
    print("Please type the number only")