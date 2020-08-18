n=int(input("Enter the size of list:"))
li=[]
print("Enter the list elements:")
for i in range(0,n):
    ele=int(input())
    li.append(ele)
def rever(l):
    rlist=[]
    for k in range(len(l)-1,-1,-1):
        rlist.append(l[k])
    return rlist
print("Original list:",li)    
print("Reversed  list:",rever(li))      
