k=list(map(int,input().split()))
e=3
bool_candy=[]
for i in k:
    if i+e>=max(k):
        bool_candy.append('True')
    else:
        bool_candy.append('False')
print(bool_candy)        
