def arr2(arr):
    arr1=[]
    for i in arr:
        if i not in arr1:
            arr1.append(i)
        else:
            return i
print(arr2([1,3,4,2,2]))
print(arr2([3,1,3,4,2]))
print(arr2([1,1]))
print(arr2([1,4,4,2,3]))

