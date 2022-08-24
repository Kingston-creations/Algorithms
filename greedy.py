n=list(map(int,input().split()))
s=int(input())
i=0
l=[]
while s!=0:
    if n[i]<=s:
        s-=n[i]
        l.append(n[i])
    else:
        i+=1
print(l)
