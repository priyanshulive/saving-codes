first=input("enter string: ")
second= ""
l=len(first)
for x in range(-1,-l-1,-1):
    second = second + first[x]
if first == second:
    print("It is a palindrome")
else:
    print("It is not a palindrome")