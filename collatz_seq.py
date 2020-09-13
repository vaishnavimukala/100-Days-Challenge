def collatz(n):
    result=0
    while n>1:
        if n%2==0:
            result= n/2
        else:
            result=3*n+1
        print(int(result))
        n=result
        if result==1:
            break
n=int(input())
collatz(n)
