def maxi(n):
    return max(n)
def mini(n):
    return min(n)
def avg(n):
    sum=0
    for i in n:
        sum+=i
    avg=round((sum/(len(n))),2)
    return avg
l=[]
ans="y"
while ans.lower()=="y":
    a=int(input("Enter term in the list: "))
    l.append(a)
    ans=input("Enter more terms? (y/n): ")
print("The maximum value in the list is: ",maxi(l))
print("The minimum value in the list is: ",mini(l))
print("The average of the values in the list is: ",avg(l))