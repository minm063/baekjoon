N, M=list(map(int,input().split()))
card=list(map(int,input().split()))

answer=0
l=len(card)

for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1, l):
            sum_val=card[i]+card[j]+card[k]
            if sum_val<=M:
                answer=max(answer, sum_val)

print(answer)