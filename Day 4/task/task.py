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

user_turn = int(input("1 for rock, 2 for paper, or 3 for scissors: "))
bot_turn = random.randint(1, 3)



if user_turn == 1:
    print("users move: Rock!")
    print(rock)
    if bot_turn == 1:
        print("computer move: Rock")
        print(rock)
        print("Draw!")
    elif bot_turn == 2:
        print("computer move: paper")
        print(paper)
        print("computer wins!")
    else:
        print("computer move: scissors")
        print(scissors)
        print("user wins!")
elif user_turn == 2:
    print("users move: paper")
    print(paper)
    if bot_turn == 1:
        print("computer move: Rock")
        print(rock)
        print("user wins!")
    elif bot_turn == 2:
        print("computer move: paper")
        print(paper)
        print("Draw!")
    else:
        print("computer move: scissors")
        print(scissors)
        print("computer wins!")
else:
    print("users move: scissors")
    print(scissors)
    if bot_turn == 1:
        print("computer move: Rock")
        print(rock)
        print("computer wins!")
    elif bot_turn == 2:
        print("computer move: paper")
        print(paper)
        print("user wins!")
    else:
        print("computer move: scissors")
        print(scissors)
        print("Draw!")