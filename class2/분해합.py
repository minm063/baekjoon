N=int(input())
answer=0

for _ in range(1, N+1):
    M=list(map(int, str(_)))
    tmp=_+sum(M)
    if tmp==N:
        answer=_
        break

print(answer)