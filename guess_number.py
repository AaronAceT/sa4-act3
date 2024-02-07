number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
limit = 5
while guess != str(number):
   if limit < 2:
      print(f'You ran out of tires. The correct answer is {number}')
      break
   elif guess == 'q' or guess == 'Q':
      print(f'the correct number is {number}. Goodbye')
      break
   elif int(guess) > number:
      limit-=1
      guess = input('Your answer was too high. Try again: ')
   elif int(guess) < number:
      limit-=1
      guess= input(f'Your answer was too low. You have {limit} Try again: ')
  


if guess == number:
   print("Congratulations! You guessed the right number.")
