x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
if x>y:
    num=y
else:
    num=x
l=[]    
for i in range(1,num+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(max(l))        
