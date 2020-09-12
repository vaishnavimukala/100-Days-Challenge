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
count=0
for i in range(2,num+1):
    if prime(i)==1:
        count+=1
        if prime(count)==1:
            print(num,'is super prime')
            break
else:
    print(num,'is not super prime')
