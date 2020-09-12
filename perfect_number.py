num=int(input())
def xyz(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
           sum+=i
    if sum==n:
        return True
    else:
        return False
print(xyz(num))    
