number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != str(number):
   if guess == 'q' or guess == 'Q':
      print(f'the correct number is {number}. Goodbye')
      break
   else:
      guess = input("Nope. Please try again: ")

print("Congratulations! You guessed the right number.")
