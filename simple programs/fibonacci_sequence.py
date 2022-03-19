terms = int(input("how many terms you want?  "))
first = 0
second = 1
count = 0
if terms <=0 :
    print("please enter more than 0 and positive value")
elif terms == 1:
    print("fibonacci sequence upto ",terms,":",first)
else:
    print("fibonacci sequence : ")
    while count < terms: 
        print(first)
        next = first + second
        first=second
        second= next
        count+=1