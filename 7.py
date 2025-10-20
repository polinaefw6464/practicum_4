x,y,z=map(int,input().split())
best=x
if y>x:
    best=y
if z>x:
    best=z
print(best)