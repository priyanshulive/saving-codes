p=open("hello.txt","w+")
k="hello world\n"
t="today is a great day"
p.write(k)
p.write(t)
p.flush()    #it ensures data is pushed into file from buffer memory
p.seek(0,0)
m=p.read()
print(m)
p.close()
