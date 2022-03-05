def admd():
    print("### Addition ###")
    m=int(input('enter a no.: '))
    n=int(input('enter another no.: '))
    print(m+n)
    print("type 'y' to add more no.s  type 'n' for quit ")
    j = input('enter your choice: ')
    h=j.upper()
    if h == 'Y':
        admd()
    elif h=='N':
        print("thankyou for coming")
    else:
        print("wrong input! ")
admd()