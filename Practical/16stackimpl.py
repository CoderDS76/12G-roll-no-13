def pop(l):
    l.pop()
def push(x,l):
    l.append(x)
def peek(l):
    print(l[-1])
a=[0,1,2,3,4,5,6,7]
b=2
print(a)
pop(a)
peek(a)
push(b,a)
print(a)