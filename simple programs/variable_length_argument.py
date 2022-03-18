def add (*P):       #In P we can pass arguments according to its need
    print(P)
    sum=0
    for x in P:   
        sum = sum + x
    print(sum)
add(3,4,5)
add(1,2,3,4,5,6)