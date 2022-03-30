p=open("hello.txt","w+")
k=[]
num=int(input("enter total no. of students: "))
for x in range(num):
    r=input("enter roll no. ")
    n=input('enter name of the student  ')
    k.append(r+" "+n+"\n")
p.writelines(k)
p.seek(0,0)
p=open("hello.txt")
print(p.read())
p.close()