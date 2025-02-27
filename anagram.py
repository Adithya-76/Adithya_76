def anagram(x,y):
    return  sorted(x) == sorted(y)
while True:    
    
    word1= input('Enter the first word : ')
    if word1.isalpha() == False:
       print('This should not include numbers!!')
       continue
    
    word2 = input('Enter the second word: ')
    if word2.isalpha() == False:
          print('This should not include numbers!!')  
          continue
    check = anagram(word1 , word2)
    if check == True:
      print(f'{word1} and {word2} are anagram words')
      break
    else:
      print(f'{word1} and {word2} are not anagram words')   
      
    choice = input('do you want to check again?, yes/no >> ').lower()
    if choice != 'yes':
        print('exiting')
        break