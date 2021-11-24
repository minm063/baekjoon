# 덱
from collections import deque
import sys

N=int(input())
stack=deque()
while N:
    tmp=sys.stdin.readline().strip()
    if 'push_front' in tmp:
        stack.appendleft(tmp.split()[1])

    elif 'push_back' in tmp:
        stack.append(tmp.split()[1])

    elif tmp=='pop_front': #stack
        if not stack:
            print(-1)
        else:
            print(stack.popleft())

    elif tmp=='pop_back':
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
    
    elif tmp=='front':
        if stack:
            print(stack[0])
        else:
            print(-1)

    elif tmp=='back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    N-=1