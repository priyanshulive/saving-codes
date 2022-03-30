p=open("hello.txt")
for x in p:
    if x[0]=='d':
        print(x)
p.close()