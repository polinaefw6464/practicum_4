x,y,n=map(int,input().split())
doxod_r1=x*n
doxod_r2=y*n//100
doxod_k=y*n-doxod_r2*100
print(doxod_r1+doxod_r2,'руб.', doxod_k,'коп.')