l=[1,2,3,5,5,7,6,3,2,7,6,7,8,9,4,6,7,8,3,9]
a=[]
b=[]
for i in range(len(l)):
        if l[i] not in a:
            a.append(l[i])
for i in range(len(a)):
    c=0
    for j in range(len(l)):
        if a[i]==l[j]:
            c=c+1
    b.append(c)
d = {k: v for k, v in zip(a,b)}
print(d)
