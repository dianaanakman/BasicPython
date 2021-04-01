import random

#value = random.randint(1,10)

#print("one day..")
#role = input("what type of role are your character?")
#bornAge = input("what year are yu born")
#print(value/10)


print("                   Colossal Cave                                 ")
print("                 The First Adventure                             ")
print("                 _________________                               ")
role = input("What is your role? [wizard,warrior,monk,mage]")
print("Your role is",role)
age = int(input("What is your age?"))
print("Your age is",age)

if age>20:
    print("You are old")
else:
    print("You are quite young")

pH=random.randint(50,100)
mH=random.randint(50,100)
print("MonsterHealth "+ str(mH))
print("PlayerHealth  "+ str(pH))

if pH<mH:
    print("Danger")
elif pH==mH:
    print("You will make it")
else:
    print("Sure Win")

monsters = ['dragon', 'snake' , 'shark']
#monsters.append('dragon')
#monsters.append('snake')
for monster in monsters:
    print(monster)

Nilai = ['60', '50' , '40', '30']
for x in Nilai:
   print("monster is bleeding : ", str(x))

if MonsterHealth%age >5 & PlayerHealth <65:
    print('You got chances to get gold')
elif MonsterHealth%age >3 & PlayerHealth <40:
    print('You got coins instead')
else:
    print('No treasure')


