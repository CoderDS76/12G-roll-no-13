def isprime(x):
    prime=True
    if x==1:
        prime=False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            prime=False
            break
        else:
            prime=True
    return(prime)
for i in range(1,101):
    if isprime(i):
        print(i,end=" ")