from collections import Counter

N=int(input())
n=[]
for i in range(N):
    n.append(int(input()))

n=sorted(n)
print(sum(n)//N)
print(n[N//2])
print(Counter(n).most_common(1)[0][0])
print(max(n)-min(n))