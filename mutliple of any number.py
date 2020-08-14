Number=int(input("Enter the Number:"))
a=int(input("Enter lower bound:"))#a is lower bound
b=int(input("Enter upper bound:"))#b is upperbound
while a<=b:
    if a%Number==0:
        print(a,end="\t")
    a+=1
#while True:
#    if a%Number==0:
#        print(a,end="\t")    
#    a+=1
#    if a>b:
#       break
#
