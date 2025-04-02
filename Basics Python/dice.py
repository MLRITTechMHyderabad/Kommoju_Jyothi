import random

d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
l=[]
for i in d1:
    for j in d2:
        l.append((i,j))
        
x={}
for i in range(2,13):
    c=0
    for j  in l:
        if i==j[0]+j[1]:
            c+=1
    x[str(i)]=c/len(l)
    
n=int(input())
y=0
z=0
for i in range(n):
    a=random.randrange(1,6)
    b=random.randrange(1,6)
    c=random.randrange(1,6)
    d=random.randrange(1,6)
    print(a,b,c,d)
    e=a+b
    f=c+d
    if x[str(e)]<x[str(f)]:
        y=y+1
    else:
        z=z+1
if(y>z):
    print("player 1 wins")
elif(z>y):
    print("player 2 wins")
else:
    print("Draw")

