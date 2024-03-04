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
hand_gestures=[rock,paper,scissors]
userchoice= int(input("Choose 0 for Rock , 1 for Paper 2 for Scissors.  : \n"))
if userchoice >= 3 or userchoice < 0:
    print(f"You typed an invalid input..you were told to select between 0 1 and 2 but you chose {userchoice} , hence you lost!")
else:
    print(hand_gestures[userchoice])
    computerchoice = random.randint(0,2)
    print(f"Computer choose: \n {hand_gestures[computerchoice]}")
    if userchoice == 0 and computerchoice == 2:
        print("You win!")
    elif computerchoice == 0 and userchoice == 2:
        print("You Loose!")
    elif computerchoice > userchoice:
        print("You Lose")
    elif userchoice > computerchoice:
        print("You Win")
    elif computerchoice == userchoice:
        print("It's a draw!")
