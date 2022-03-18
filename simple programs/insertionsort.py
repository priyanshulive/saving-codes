p=[10,1,18,65,35,1,0,52,10,9,8,7,45]
print('unsorted list',p)
for x in range (1,len(p)):
    pos = x-1
    temp = p[x]
    while p[pos]>temp and pos>=0:
        p[pos+1]= p[pos]
        pos=pos-1
    p[pos+1]=temp
print ("sorted list",p)