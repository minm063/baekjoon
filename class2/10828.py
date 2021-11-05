from collections import deque
import sys

N=int(input())
stack=deque()
while N:
    tmp=sys.stdin.readline().strip()
    if 'push' in tmp:
        stack.append(tmp.split()[1])
    elif tmp=='pop': #stack
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif tmp=='size':
        print(len(stack))
    elif tmp=='empty':
        if stack:
            print(0)
        else:
            print(1)
    elif tmp=='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    N-=1