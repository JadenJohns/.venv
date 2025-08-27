#Decision Maker
# Use this when I dont know what I want to eat
'''How it works: 1. How much do I want to Spend 2. Figure out if I can cook something is I dont want to spend
3. If I do want to spend would I rather do Uber or walk. 4. If I don't want to spend but no food at home use a random generator to pick cheap resturants
5.If I am spending and I another txt file and do what step for does 6.If I'm walking choose what place to go to
7. Implement by date/time/closing time if applicable 8.Divide by food category? 9.Make a function where it goes through everything and chooses a random place?
10.Maybe a scoring to find what I am truly feeling like eating???'''
import random

##def step1():
##   print('test')


d1 = input('Do you want to spend more than $15?(Y/N): \n').strip().upper()

if d1 == "N":
    choice = input('Is there food at home fi cook?(Y/N):\n').strip().upper()

    if choice == 'Y':
        
        print('Then find sum fi cook')

    if choice == 'N':
        #Place holder (Might do a resturant genarator using a txt file)
        print('Test for now.')