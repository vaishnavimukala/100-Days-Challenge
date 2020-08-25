def prime(n):
   count=0
   for i in range(2,n+1):
       if n%i==0:
           count+=1
   if count==1:
       return (1)
   else:
       return (0)
num=int(input())
for i in range(num-1,0,-1):
    if prime(i)==1:
        print(i)
        break
j=num+1    
while j>num:
    if prime(j)==1:
        print(j)
        break
    j+=1
if abs(num-i)<abs(num-j):
    print(i,'is nearest prime')
elif abs(num-i)==abs(num-j):
    print(i,j,'are nearest prime')
else:
    print(j,'is nearest prime')
