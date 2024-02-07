number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != str(number):
   if guess == 'q' or guess == 'Q':
      print(f'the correct number is {number}. Goodbye')
      break
   elif int(guess) > number:
      guess = input('Your answer was too high. Try again: ')
   elif int(guess) < number:
      guess= input('Your answer was too low. Try again: ')
   else:
      guess = input("Nope. Please try again: ")
if guess == number:
   print("Congratulations! You guessed the right number.")
