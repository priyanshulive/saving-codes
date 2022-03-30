p=open("hello.txt")
t=p.read()
k=t.split()
for x in k:
    if len(x)==5:
        print(x)
p.close()