n, k = list(map(int, input().split()))

def fac(num):
    f=1
    for n in range(num, 1, -1):
        f*=n
    return f
fN, fK, fD = fac(n), fac(k), fac(n-k)

print(fN//(fK*fD))