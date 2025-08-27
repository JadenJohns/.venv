
game = True

import random

def cont():
     
     choice = input('Continue(Y/N): ').strip().upper()

     if choice == 'Y':
          return True
    
     elif choice == 'N':

        print ('\nHave a nice day!')

        return False
     else:
        print('Invalid input.\n')
        return cont()
        

#Main
while game == True:

    numb = int(input('\nChoose a number 1-10: '))

    y = random.randint(1, 10)

    if numb > 0 and numb < 11 :
        if numb < y:
        
            print('\nI rolled a:',y)
            print ('\nHaha you lose!\n')
            game = cont()


        elif numb > y:
        
            print('\nI rolled a:',y)
            print('\nDang I lost \n')
            game = cont()

        else:
        
            print('\nI rolled a:',y)
            print('\nDang a tie\n')
            game = cont()
        
    else:
            print('Invalid please choose again\n')
            


