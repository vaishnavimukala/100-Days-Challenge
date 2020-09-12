num=int(input())
def aliquot(n):
    sum=0 
    for i in range(1,n//2+1):
             if n%i==0:
                  sum+=i
    return sum
while num>0:
    print(aliquot(num),end=" ")
    num=aliquot(num)
    
