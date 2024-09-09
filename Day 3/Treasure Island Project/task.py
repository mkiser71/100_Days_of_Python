'''

88                               88
88                               88
88                               88
88,dPPYba,  ,adPPYYba, ,adPPYba, 88,dPPYba,
88P'    "8a ""     `Y8 I8[    "" 88P'    "8a
88       d8 ,adPPPPP88  `"Y8ba,  88       88
88b,   ,a8" 88,    ,88 aa    ]8I 88       88
8Y"Ybbd8"'  `"8bbdP"Y8 `"YbbdP"' 88       88
                                              '''

print("Welcome to the bash!")
choice1 = input('Would you turn "left" or "right"?').lower()

if choice1 == "left":
    choice2 = input('Would you "swim" or "wait"?').lower()
    if choice2 == "wait":
        choice3 = input('Would you choose the "red", "yellow" or "blue" door?').lower()
        if choice3 == "red":
            print('Game Over')
        elif choice3 == "yellow":
            print("Treasure found. You win.")
        elif choice3 == "blue":
            print('You got ate by beasts.')
        else:
            print('No door there, sorry. You lose.')
    else:
        print('Killed by angry trout. Game Over.')





else:
    print('You ded sucka!')
    '''
    
       if choice3 == "blue":
            print("You ded sucka!")
        elif choice3 == "red":
            print("Burned by fire - GAME OVER!")
        else:
            print("You WIN!")
else:
    print('You ded sucka!')
    '''





