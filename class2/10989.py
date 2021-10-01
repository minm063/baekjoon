import sys
N = int(input())
check_list = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    check_list[num] += 1
print(check_list)
for i in range(10001):
    if check_list[i] != 0:
        for _ in range(check_list[i]):
            print(i)