p=open("hello.txt","w+")
num= int(input ("enter total no. of students you want to enter: "))
for x in range(num):
    r=input("enter roll no. ")
    n=input("enter name of the student: ")
    s=r+' '+n+'\n'
    p.write(s)
p.seek(0,0)
m=p.read()
print(m)
p.close()