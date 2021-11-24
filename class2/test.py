a=[]
b=[]
value=0

for i in range(0,100):
    a.append(value)
    value+=2

for i in range(0,100):
    b.append(a[99-i])

print('bb[0] %d, bb[99] %d'%(b[0], b[99]))