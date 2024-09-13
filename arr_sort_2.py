def sorting(arr1,arr2):
    arr3=sorted((arr1+arr2))
    a=len(arr1)
    for i in range(len(arr1)):
        arr1[i]=arr3[i]
        arr2[i]=arr3[a]
        a+=1
    return arr1,arr2

print(sorting([1,3,5],[2,4,6]))





