import random
def game():

Name1 = input("Enter player 1's name: ")
Name2 = input("Enter player 2's name: ")

r=random.randint(1,6)
print("this is your number",r)
ask=input("do you want to continue or quit")
if ask == "continue":
    dice_roll()
else:
    print("goodbye")
    dice_roll()

