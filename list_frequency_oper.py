a=list(map(int,input().split()))
b=''
for i in range(0,len(a),2):
    b=b+str(a[i+1])*a[i]    
print(list(b))    
