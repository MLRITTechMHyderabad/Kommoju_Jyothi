s=[("Alice",[85,90,78,92]), ("bob",[60,70,65,75]),("charlie",[40,45,50,55]),("David",[95,100,98,92])]
l=[]
m=[]
for  i in range(len(s)):
    l.append(s[i][0])
for i in range(len(s)):
               for j in range(1,len(s[i])):
                              m.append(s[i][j])
d={k:v for k,v in zip(l,m)}
print("Dictonary of students and grades: ",d)
n=input()
print("Average grade of given name: ",sum(d[n])/len(d[n]))
c=[]
for i in range(len(m)):
    x=0
    for j in range(len(m[i])):
                   x=x+(m[i][j])
    c.append(x//len(m[i]))
z=c.index(max(c))
print("student with highest average: ",l[z])
co=0
for i in range(len(c)):
    if c[i]>=50:
        co=co+1
print("no of students passed: ",co)
