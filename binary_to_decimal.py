n=int(input())
def decimal(n):
    p=len(str(n))
    sum=0
    for i in range(0,p):
        c=n%10
        sum+=c*(2**i)
        n=n//10
    print(sum)
decimal(n)
