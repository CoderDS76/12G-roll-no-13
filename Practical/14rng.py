import random
sum=0
for i in range(10):
    x=random.randint(1,6)
    y=random.randint(1,6)
    sum+=(x+y)
    print(x,y,end="#")
print("The sum of the 10 throws is: ",sum)