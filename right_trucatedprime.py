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
if prime(num)==1:
    n=num
    count=0
    while n!=0:
        if prime(n)==1:
            count+=1
        else:
            count=0
        n=n//10   
    if count==len(str(num)):
        print(num, 'is right trucated prime')
    else:
        print(num, 'is not right trucated prime')
else:
    print(num, 'is not prime')
