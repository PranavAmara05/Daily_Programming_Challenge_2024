sent=input("enter the sentence").split()
new=sent[len(sent)-1]
for i in range(len(sent)-2,-1,-1):
    new=new+" "+sent[i]
print(new)


