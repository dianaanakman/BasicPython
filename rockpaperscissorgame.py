computer_choice = 'scissors'
user_choice = input('Do You Want a rock,paper or scissors?\n')
if computer_choice == user_choice:
    print("SERI")
elif user_choice == "rock" and computer_choice == "scissors":
    print("user win")
elif  user_choice == "paper" and computer_choice == "rock":
    print("user win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("user win")
else:
    print("You Lose :( computer win :)")