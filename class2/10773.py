K=int(input())
cash=[]
while K:
    n=int(input())
    if n==0:
        cash.pop()
    else:
        cash.append(n)
    K-=1
print(sum(cash))