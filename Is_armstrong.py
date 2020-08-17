def is_armstrong(digit):
    n=digit
    sum=0
    while n!=0:
        d=n%10
        sum=sum+d**3
        n=n//10
    if sum==digit:
        return True
    else:
        return False
num=int(input("Enter a three digit number:"))
print(is_armstrong(num))
