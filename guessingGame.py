import random

print("This is a number guessing game between 1-9, try to guess the number in 5 turns, or lose!")
number= random.randint(1,9)
guess= int(input("Enter your first guess here:-"))

if guess == number:
    print("Yay! Congratulations! You won!")

elif guess < number:
    print("Your guess was too low, try a higher number than" ,guess)

else:
    print("Your guess was too high, try a lower number than" ,guess)
    
if guess != number:
    guess2= int(input("Enter your second guess here:-"))
if guess2 == number:
    print("Yay! Congratulations! You won!")
elif guess2 < number:
    print("Your guess was too low, try a higher number than" ,guess2)
else:
    print("Your guess was too high, try a lower number than" ,guess2)

if guess2 != number:
    guess3= int(input("Enter your third guess here:-"))
if guess3 == number:
    print("Yay! Congratulations! You won!")
elif guess3 < number:
    print("Your guess was too low, try a higher number than" ,guess3)
else:
    print("Your guess was too high, try a lower number than" ,guess3)

if guess3 != number:
    guess4= int(input("Enter your fourth guess here:-"))
if guess4 == number:
    print("Yay! Congratulations! You won!")
elif guess4 < number:
    print("Your guess was too low, try a higher number than" ,guess4)
else:
    print("Your guess was too high, try a lower number than" ,guess4)

if guess4 != number:
    guess5= int(input("Enter your fifth and last guess here:-"))
if guess5 == number:
    print("Yay! Congratulations! You won!")
else:
    print("Sorry, you ran out of turns, the number was" ,number)