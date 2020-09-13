import random
def prime(n):
   count=0
   for i in range(2,n+1):
       if n%i==0:
           count+=1
   if count==1:
       return (1)
   else:
       return (0)
n=int(input("Enter a number:"))
def before_prime(n):
    while n>1:
        if prime(n-1)==1:
             return n-1       
        else :
             n=n-1
spl_p_l=[]
num=n
while num>2:
   spl_p_l.append(before_prime(num))
   num-=1
spl=list(set(spl_p_l))
print(spl)

   
