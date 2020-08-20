L=list(map(int,input("Enter the list:").split()))
D={}
for i in L:
    j=L.count(i)
    D[i]= j
for i in D:
    print(i,"occured",D.get(i),"times")
