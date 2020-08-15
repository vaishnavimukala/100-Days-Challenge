n=int(input("Enter the number:"))
sl=int(input("Enter start limit:"))
el=int(input("Enter end limit:"))
if sl<el:
   for i in range(sl,el+1):
           print(n,"*",i,"=",n*i)
else :
    for i in range(sl,el-1,-1):
          print(n,"*",i,"=",n*i)

