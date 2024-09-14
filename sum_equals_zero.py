arr=[4,-1,-3,1,2,-1]
l=[]
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum==0:
            l.append((i,j))
print(l)
