import random
import string
def password_generator():
  while True:
       characters = string.ascii_letters + string.digits + string.punctuation
       password =""
       length = int(input('enter length of your password >> '))
       if length < 8:
       	print('choose minimum of 8 characters!')
       	continue
       for i in range(length):
         	password += random.choice(characters)
       print(password )
       break
password_generator()  
while True:
	choice = input('Do you want other password?,choose yes/no>>  ').lower()
	if choice == 'yes':
	     password_generator()
	else:
		print('exiting')