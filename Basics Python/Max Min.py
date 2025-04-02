a=[[1,2,3],[7,8,9]]
max=a[0][0]
min=a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]<min:
            min=a[i][j]
        if a[i][j]>max:
            max=a[i][j]
        
print(max,min)

b=[[1,2,3],[7,8,9]]
print(max(b),min(b))
