#play a dice rolling game
#user decides what number is the winning number
  #getting closest to the winning number without going over wins
#set user score to 0
#roll the dice to get a random number (add that number to user score)
#options to roll again or stop
#You win with user score/decided number
# OR Computer wins with message you went over the decided number

import random

winning_number = input("What number would you like to try to get to?: ")
if not winning_number.isdigit():
  print("Please enter a valid number.")
  quit

user_score = 0

def roll_dice():
  number = random.randint(1, 6)
  return number

while True:
  answer = input("Would you like to roll? (Y/N) or Q to quit. ").lower()
  if answer == 'q':
    quit()

  if answer == 'y':
    roll = roll_dice()
    print(f"You rolled a {roll}.")
    user_score += roll 
    if int(user_score) < int(winning_number):
      print(f"You are at {user_score} out of {winning_number}.")
    elif int(user_score) == int(winning_number):
      print(f"You WIN! :) You got to {winning_number}!!")
      quit()
    elif int(user_score) > int(winning_number):
      print(f"You went over :( Your score: {user_score} Goal: {winning_number}")
      quit()
  elif answer == 'n':
    print(f"You scored {user_score} out of {winning_number}.")
    quit()
  
