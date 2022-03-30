p=open("hello.txt")
char=" "
while char:
    char=p.read(1)
    print(char,end="")
p.close()
