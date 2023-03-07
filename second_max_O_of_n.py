A = [6,-1,-8,-9,-2]
if A[0]<A[1]:
    a = A[0]
else:
    a = A[1]
max1 = max2 = a
for i in range(1,len(A)):
    if A[i]>max1:
        max2 = max1
        max1 = A[i]
    if A[i]<max1 and A[i]>max2:
        print(max2)
        max2 = A[i]
print(max2)
#not for([-1,-8,-9,-2])
