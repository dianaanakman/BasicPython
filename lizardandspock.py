computer_choice = 'scissors'
user_choice = input('Do You Want a rock,paper,scissors,lizard or spock?\n')
if computer_choice == user_choice:
    print("SERI")
elif user_choice == "rock" and computer_choice == "scissors":
    print("user win")
elif  user_choice == "paper" and computer_choice == "rock":
    print("user win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("user win")
elif user_choice == "lizard" and computer_choice == "paper":
    print("user win")
elif user_choice == "spock" and computer_choice == "scissors":
    print("user win")
elif user_choice == "rock" and computer_choice == "lizard":
    print("user win")
elif user_choice == "paper" and computer_choice == "spoke":
    print("user win")
else:
    print("you lose :( computer win :)")