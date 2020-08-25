n=int(input("Enter a number:"))
def num_prime(n):
    count=0
    for i in range(2,n+1):
           if n%i==0:
               count+=1
    if count==1:
           return (1)
    else:
           return (0)
prime=num_prime(n)
print(prime)
check=0
num=n
while num!=0:
        rem=num%10
        num=num//10
        if num_prime(rem)==1:
            check=1
print(check)
if prime==1 and check==1:
    print(n,'is meg prime')
else:
    print(n,'is not ameg prime')
