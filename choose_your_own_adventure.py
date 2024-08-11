name = input("Type your name: ")

print(f"Welcome, {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go to the left or the right. Which way would you like to go? ").lower()
if answer == 'left':
  answer2 = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around it or 'swim' to swim across it: ").lower()
  
  if answer2 == 'walk':
    print("You walked for many miles, ran out of water and lost the game.")
  elif answer2 == 'swim':
    print("You swam across and were eaten by an alligator.")
  else:
    print("Not a valid option. You lose. :(")
    
elif answer == 'right':
  answer3 = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type 'cross' to cross the bridge or 'turn' to turn back. ").lower()
  
  if answer3 == 'cross':
    answer4 = input("You cross the bridge and meet a stranger. Do you talk to the stranger? Type 'yes' to talk or 'no' to walk past them. ").lower()
    
    if answer4 == 'yes':
      print("You talk to the stranger and they give you gold. YOU WIN!")
    elif answer4 == 'no':
      print("You walk for miles and never see another person. You run out of food and water. You lose.")
    else:
      print("Not a valid option. You lose :(")

  elif answer3 == 'turn':
    print("You turned back into a band of thieves and were taken. You lose.")
  else:
    print("Not a valid option. You lose. :(")

else:
  print("Not a valid option. You lose. :(")