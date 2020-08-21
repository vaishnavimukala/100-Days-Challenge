def check(s):
    ascen=descen=0
    for i in range(0,len(s)-1):
        if s[i]<s[i+1]:
            ascen+=1
        elif s[i]>s[i+1]:
            descen+=1
        else:
            break
    if ascen==len(s)-1:
        return("is Ascending")
    elif descen==len(s)-1:
        return("is descending")
    else:
        return("Not in order")
string=input()
print(check(string))

    
