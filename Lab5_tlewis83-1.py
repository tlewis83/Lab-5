'''
Roll the dice game
Tyee Lewis
Execute Dice Game
9/28/2025
'''

import random

dice_one = random.randint(1, 6)

dice_two = random.randint(1, 6)

roll = f'{dice_one},{dice_two}'

keep_going = True


result_dict = {
    2: "Snake Eyes",
    3: "Ace Caught a Deuce",
    "2,2": "Little Joe from kokomo",
    5: "Little Phoebe",
    "3,3": "Jimmy Hicks from the Sticks",
    "6,1": "Six Ace",
    "4,4": "Eighter from Decatur",
    9: "Nina from Pasadena",
    "5,5": "Puppy Paws",
    "6,5": "Six Five no Jive",
    12: "Boxcars"
}

def the_game():
    if dice_one + dice_two == 2:
        print(result_dict[2])
    elif dice_one + dice_two == 3:
        print(result_dict[3])
    elif roll == '2,2':
        print(result_dict["2,2"])
    elif dice_one + dice_two == 5:
        print(result_dict[5])
    elif roll == '3,3':
        print(result_dict["3,3"])
    elif roll == '6,1':
        print(result_dict['6,1'])
    elif roll == '4,4':
        print(result_dict["4,4"])
    elif dice_one + dice_two == 9:
        print(result_dict[9])
    elif roll == '5,5':
        print(result_dict['5,5'])
    elif roll == '6,5':
        print(result_dict["6,5"])
    elif dice_one + dice_two == 12:
        print(result_dict[12])
    else:
        print('miss')

while keep_going == True:
    print(roll)
    the_game()
    go_again = input('Would you like to try again? (y/n)')
    if go_again == 'n':
        print('Thanks for playing!')
        keep_going = False
    elif go_again == 'y':
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        roll = f'{dice_one},{dice_two}'
        continue


