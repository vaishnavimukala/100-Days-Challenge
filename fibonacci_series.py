n=int(input("enter range:"))
a=0
b=1
print(a,b,end=' ')
while n!=0:
   c=a+b
   a=b
   b=c
   print(c,end=' ')
   n=n-1
