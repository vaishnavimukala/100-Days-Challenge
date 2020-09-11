n=int(input())
def num(n):
    s=0
    while n>0:
        r=n%10
        s=s+r**2
        n=n//10
    return s
def happy(n):
    k=num(n)
    while n>=10:
        if k==1 or k==7:
            return True
        else:
            k=num(k)
            if k==4:
                return False
            
    else:
        if n==1 or n==7:
            return True
        else:
            return False       
print(happy(n))
