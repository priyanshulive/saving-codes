p=open("hello.txt")
t=p.read()
k=t.split()
print(k)                #it split every word of the file and make a list
print(len(k))