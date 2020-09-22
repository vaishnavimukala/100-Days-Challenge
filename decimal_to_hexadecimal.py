n=int(input())
def decimal_to_hexad(n):
    s=''
    while n:
        c=n%16
        if c<10:
            s+=str(chr(c+48))
        else:
            s+=str(chr(c+55))
            n=n//8
        n=n//16    
    s=s[::-1]
    return s
print(decimal_to_hexad(n))
