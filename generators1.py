
def fact(n):
    k=1
    while n>0:
        f=1
        for i in range(1,k+1):
            f=f*i
        yield f
        
        k+=1
        n-=1
        
        
res = list(fact(6))

print(*res,end=" ")
