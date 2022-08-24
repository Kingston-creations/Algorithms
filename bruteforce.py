from itertools import combinations_with_replacement as c
n=list(map(int,input().split()))
m=int(input())
l=[]
k=100000000
for i in range(1,m+1):
    x=c(n,i)
    for j in x:
        z=list(j)
        if sum(z)==m:
            if len(z)<k:
                k=len(z)
                l=z
print(l)
