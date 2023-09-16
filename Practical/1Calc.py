def add(m,n):
    res=m+n
    return res

def sub(m,n):
    res=m-n
    return res

def mult(m,n):
    res=m*n
    return res

def div(m,n):
    if n!=0:
        res=m/n
    else:
        print("Error Division by zero")
    return res

def exp(m,n):
    res=m**n
    return res
ans="y"
while ans.lower()=="y":
    a=int(input("Enter First number: "))
    b=int(input("Enter Second number: "))
    print("[1] Additon,[2] Subtraction,[3] Multiplication,[4] Division,[5] Exponentiation")
    op=int(input("Choose Operation: "))
    if op==1:
        print("The result is: ",a+b)
    elif op==2:
        print("The result is: ",a-b)
    elif op==3:
        print("The result is: ",a*b)
    elif op==4:
        try:
            print("The result is: ",a/b)
        except:
            print("Try again!")
    elif op==5:
        print("The result is: ",a**b)
    else:
        print("Wrong choice!")
        
    ans=input("Do another calculation? (y/n): ")