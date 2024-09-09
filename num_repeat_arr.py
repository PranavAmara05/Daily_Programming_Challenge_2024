def asc(arr):
    zer=on=tw=0
    for i in arr:
        if i==0:
            zer+=1
        elif i==1:
            on+=1
        else:
            tw+=1
    arr=[0]*zer+[1]*on+[2]*tw
    return arr
print(asc([0, 1, 2, 1, 0, 2, 1, 0]))
print(asc([2, 2, 2, 2])) 
print(asc([0,0,0,0])) 
print(asc([1,1,1,1])) 
print(asc([2,0,1])) 
print(asc([])) 