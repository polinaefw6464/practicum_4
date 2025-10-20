x=str(input('введите счет матча '))
y=x.split(':')
a1=int(y[0])
a2=int(y[-1])
if a1>a2:
    print(1)
elif a1<a2:
    print(2)
else:
    print(0)