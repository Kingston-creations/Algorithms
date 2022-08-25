n=int(input())
c=[chr(i+96) for i in range(1,n+1)]
m=1
i=0
while len(c)!=1:
    if i==len(c):
        i=0
    if m%4==0 or m%10==4:
        c.remove(c[i])
        i-=1
    m+=1
    i+=1
print(c)
