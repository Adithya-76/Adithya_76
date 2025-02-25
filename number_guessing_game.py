import random
def number_game():
    print('welcome to number guessing game')
    attempts = 5
    computer_choice = random.randint(1,100)  
    while True:
      try:
        user_choice = int(input('enter a number between 1 to 100 >>  '))
        attempts-=1
      except :
          print('enter a valid number') 
          
          continue
      if user_choice < 1 or user_choice > 100:
           print('enter a number between 1 to 100!!!')
      if user_choice > computer_choice:
           print('try a smaller number')   
      elif user_choice < computer_choice:
           print('try a bigger number') 
      elif user_choice == computer_choice:
           print('congrats, you chose correct answer') 
           break
      
      
      
      if attempts == 0:
           print('you lost')
           print(f'computers choice is {computer_choice}')
           break
      print(f'number of attempts left >> {attempts}')    
      
number_game()
again= input('Do yo want to play again?  Enter yes or no >> ').lower()
if again == 'yes':
	number_game()
else:
	print('exiting')	