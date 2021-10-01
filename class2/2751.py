# 수 정렬하기2

N=int(input())
p=[0]*N
while N:
    n=int(input())
    p[N-1]=n
    N-=1
print(sorted(p))
n=[int(input()) for i in range(int(input()))]
print("\n".join(map(str, sorted(n))))