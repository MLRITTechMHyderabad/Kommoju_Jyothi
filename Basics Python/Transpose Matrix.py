a=[[1,2,3],[4,5,6]]
b=[[7,8],[9,0],[34,56]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for r in b:
    print(r)
