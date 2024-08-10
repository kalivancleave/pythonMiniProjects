print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is Gilderoy Lockhart's favourite colour? ")
if answer.lower() == "lilac":
  score += 1
  print("Correct!")
else:
  print("Tut tut - hardly any of you remembered that my favourite colour is lilac.")

answer = input("What is Gilderoy Lockart's ideal birthday gift? ")
if answer.lower() == "harmony between all magic and non-magic peoples":
  score += 1
  print("Correct!")
else:
  print("A few of you need to read Wanderings with Warewolves more carefully - I clearly state in chapter twelve that my ideal birthday gift would be harmony between all magic and non-magic peoples.")

answer = input("Which is the personal name which Gilderoy Lockhart has given to his broomstick? ")
if answer.lower() == "the swashbuckler":
  score += 1
  print("Correct!")
else:
  print("Sorry, that's not correct.")

answer = input("How many times has Gilderoy Lockhart won Whtch Weekly's Most Charming Smile Award? ")
if answer.lower() == "five":
  score += 1
  print("Correct!")
else:
  print("Oops, that's wrong.")

print(f"You got {score} questions correct!")
print(f"You got {score/4 * 100}%.")