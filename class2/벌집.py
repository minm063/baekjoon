N=int(input())
tmp=1
while N>1:
    N-=(6*tmp)
    tmp+=1

print(tmp)