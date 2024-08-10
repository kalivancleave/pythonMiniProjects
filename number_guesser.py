import random

top_of_range = input("Type the greatest number for the range: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print("Please type a number larger than 0 next time")
    quit()
else: 
  print("Please type a number next time.")
  quit()


# r_range = random.randrange(-5, 11) #note the range does not include the upper bound number
r_int = random.randint(0, top_of_range) #note the int will include the upper bound as an option
guesses = 0

while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)

  else: 
    print("Please type a number next time.")
    continue

  if user_guess == r_int:
    print("You got it!")
    break
  elif user_guess > r_int:
    print("You were above the number!")
  else:
    print("You were below the number!")

print(f"You got it in {guesses} guesses.")


