p=open("hello.txt")
c=0
k=p.read()
l=['a','e','i','o','u']
for i in k:
    for x in l:
        if i==x:
            c+=1
print("total no. of vowels",c)