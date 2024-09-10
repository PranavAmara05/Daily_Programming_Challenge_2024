def arr1(arr):
    for i in range(len(arr)):
        if arr[i]!= i+1:
            return i+1
    else:
        return i+2
print(arr1([1, 2, 4, 5]))
print(arr1([2, 3, 4, 5]))
print(arr1([1,2,3,4]))
print(arr1([1]))

