l,l1=[16,17,4,3,5,2],[]
for i in range(len(l)):
    if(max(l[i::])==(l[i])):
        l1.append(l[i])
print(l1)

l = [16, 17, 4, 3, 5, 2]
l1 = []
current_max =0

for i in range(len(l)-1,-1,-1):
    if l[i] > current_max:
        l1.append(l[i])
        current_max = l[i]

l1.reverse()
print(l1)

