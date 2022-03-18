def hello(P):
    print(P,id(P))
    P[0]=101
    print(P,id(P))
a=[3,2,5]
print(a,id(a))
hello(a)
print(a,id(a))