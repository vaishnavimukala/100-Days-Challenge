n=int(input())
def decimal_to_octal(n):
    s=''
    while n:
            s+=str(n%8)
            n=n//8
    s=s[::-1]
    return s
print(decimal_to_octal(n))
