def hello():
    a=3                         #nonlocal changes the value of a=3 to a=7
    def today():
        nonlocal a              #it changes the value of enclose variable
        a=7                     #nonlocal changes the value of just outside
        print("today",a)        #present variable
    today()
    print("hello",a)
a=50
print('main',a)
hello()
print("main",a)