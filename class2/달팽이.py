A, B, V = list(map(int, input().split()))

# while 0<=V:
#     day+=1
#     if V-A<=0:
#         break
#     V=V-A+B

# print(day)
 
H = V - A
if H % (A-B) == 0:
    day = H//(A-B)
else:
    day = H//(A-B) + 1
print(day + 1)