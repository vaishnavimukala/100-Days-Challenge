num=int(input())
def Abundant(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
           sum+=i
    if sum>=n:
        return "is Abundant Number"
    else:
        return "is not Abundant Number"
print(Abundant(num))    
