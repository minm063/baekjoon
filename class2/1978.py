# 소수 찾기

N=int(input())
N_list=list(map(int, input().split()))

count=0
for n in N_list:
    tmp=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                tmp+=1
                break
        if not tmp:
            count+=1

print(count)