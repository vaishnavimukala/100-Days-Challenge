def fact(n):
    if n==1or n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number:"))
if num<0:
    print("Only positive numbers")
else:    
    print("factorial of ",num,"is",fact(num))
