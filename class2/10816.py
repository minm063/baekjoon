import sys
N=int(input())
card=list(map(int, sys.stdin.readline().split()))
# card.sort()
M=int(input())
sang=list(map(int, sys.stdin.readline().split()))
# sang.sort()

result=[0]*M
for _ in card:
    if _ in sang:
        result[sang.index(_)]+=1
for _ in result:
    print(_, end=' ')