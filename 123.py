#L=[]
#for e in range(0,10):
#    L.append(e**2)
#print(L)
L=[[1,2,3], [4,5,6], [7,8,9]]
Det = L[0][0]*(L[2][2]*L[1][1] - L[2][1]*L[1][2]) - L[0][1]*(L[2][2]*L[1][0] - L[2][0]*L[1][2]) + L[0][2]*(L[2][1]*L[1][0] - L[2][0]*L[1][1])
print(Det)
for e in L:
    print(e)