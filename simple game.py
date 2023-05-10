import random
choice = int(input("enter your choice 1: rock, 2: paper, 3: Scissor?? "))
computer_choice = random.randint(1, 3)

if choice == computer_choice:
    print("DRAW")
elif choice == 1:
    if computer_choice == 2:
        print("Computer Win")
    else:
        print("You Win")
elif choice == 2:
    if computer_choice == 3:
        print("Computer Win")
    else:
        print("You Win")