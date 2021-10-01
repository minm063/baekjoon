N=int(input())
coordinate = []
while N:
    coordinate.append(list(map(int, input().split())))
    N-=1

coordinate=sorted(coordinate, key=lambda x: x[0])
coordinate=sorted(coordinate, key=lambda x: x[1])

for _ in coordinate:
    print(_[0], _[1])