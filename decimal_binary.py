n=int(input())
def binary(n):
    str=''
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        while n!=1:
            if n%2==0:
                str=str+'0'
                n=n//2
            else :
                n=n//2
                str=str+'1'
        str=str+'1'
        str=str[::-1]
        return str
print(binary(n))
