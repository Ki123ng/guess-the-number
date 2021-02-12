import random
score = 0
while True:
  num = random.randint(1, 5)
  guess = input("Please Enter your Number (Hint: Number lies between 1 and 5) :- ")
  if(guess == str(num)):
    score += 1
    print("GG!\nYour Score :", score, "\n")
  else:
    break
print("Game Over!\nThe number was", num, "\nYour Score :", score, "\n")
