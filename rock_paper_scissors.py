import random
def rps():
    print('Welcome to rock paper scissors game')
    options = ['rock','paper','scissors']
    
    attempt = 3
    
    while True:
        computer_choice = random.choice(options)
        user_choice = input('enter your choice >> ')  
        if user_choice not in options:
            print('enter valid choice')
            continue
        winning_situation = {
            "rock" : "scissors",
            "scissors" : "paper",
            "paper":"rock"
            }
            
        if winning_situation[user_choice ]== computer_choice:
            print('congrats ,you won')
            break
        elif user_choice == computer_choice:
            print('its a tie')  
            
        elif winning_situation[computer_choice] == user_choice:
            print('you lost!')
            attempt -= 1            
            print(f'number of attempts left are {attempt}')
            if attempt == 0:
                print('you are out of chances')
                break
        
rps()            
while True:
  user = input('do you want to play again? yes/no >> ').lower()
  if user != 'no':
    rps()
   