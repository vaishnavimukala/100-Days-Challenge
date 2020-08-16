n=int(input("Enter the number:"))
fact=1
if n!=0:
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of ",n,"is",fact)    
else:
    print("Factorial of ",n,"is",fact)   
