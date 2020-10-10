a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i not in b:
        c.append(i)
for j in b:
    c.append(j)
print(c)        

        
