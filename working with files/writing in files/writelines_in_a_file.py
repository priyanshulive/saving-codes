p=open("hello","w+")
k=["my name is mac\n","your friend name is john\n","we are classmates\n"]
p.writelines(k)
p.seek(0,0)
print(p.read())
p.close()