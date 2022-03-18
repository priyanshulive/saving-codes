k=[52,34,6,1,8,9,19]
print ("unsorted list",k)
n=len(k)
for x in range (n-1):
    for y in range (n-x-1):
        if k[y]>k[y+1]:
            k[y],k[y+1]=k[y+1],k[y]
print('sorted list',k)