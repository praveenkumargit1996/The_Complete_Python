import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Building a Rock Scissors game

# the list is storing the strings of images.
game_images = [rock, paper, scissors]

items =["rock", "paper", "scissors"]

computer_int = random.randint(0,2)
computer_choice = items[computer_int]


your_choice=input('select your choice "rock" or "paper" or "scissors".\n').lower()
if computer_choice == "rock" and your_choice == "rock":
    print(f"you choose:{your_choice}\n {rock}")
    print(f"computer choose:{computer_choice}\n {rock}")
    print(f"you will win the game!")
elif computer_choice == "paper" and your_choice == "paper":
    print(f"you choose:{your_choice}\n {paper}")
    print(f"computer choose:{computer_choice}\n {paper}")
    print(f"you will win the game!")
elif computer_choice == "scissors" and your_choice == "scissors":
    print(f"you choose:{your_choice}\n {scissors}")
    print(f"computer choose:{computer_choice}\n {scissors}")
    print(f"you will win the game!")
else :
    if your_choice == "rock" and computer_choice != "rock":
        print(f"you choose:{your_choice}\n {rock}")
        print(f"computer choose:{computer_choice}\n ")
        print(game_images[computer_int])
        print(f"you will loose the game!")

    elif your_choice == "paper" and computer_choice != "paper":
        print(f"you choose:{your_choice}\n {paper}")
        print(f"computer choose:{computer_choice}\n ")
        print(game_images[computer_int])
        print(f"you will loose the game!")

    else:
        print(f"you choose:{your_choice}\n {scissors}")
        print(f"computer choose:{computer_choice}\n ")
        print(game_images[computer_int])
        print(f"you will loose the game!")