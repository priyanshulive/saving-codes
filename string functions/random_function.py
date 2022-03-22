import random
print(random.random())      #it gives value between 0 to 1
print(random.random()*(50-10)+10)  #it gives value between 10 to 50
print(random.randint(15,25))     #it gives value between 15 to 25
print(random.randrange(1,100,2))  #it gives value between 1 to 100 but only odd no.s
print(random.choice("today"))     #it gives any of the letter of "today"
print(random.choice([42,18,16])) #it gives any one of them 42,18,16 
