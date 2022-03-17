def hello():
    a=int(input("enter first number: "))
    b=int(input('enter second number: '))
    c=int(input ('enter third number: '))
    return a,b,c
# p,q,r = hello()               # in commented lines we can use in
# print('this is p: ',p)        # place of last two lines.
# print('this is q: ',q)
# print("this is r:",r)
t=hello()
print(t)