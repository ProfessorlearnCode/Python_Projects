# Exercise # 5 : To create a Snake Water gun
##########################################################
'''
- Prompt the user to either choose snake, water or gun
- The computer chooses one automatically
- The computer and then your option is compared

                   S  W  G
computer          -1  0  1
player      S -1   D  W  L
            W  0   L  D  W
            G  1   W  L  D

'''

# Program that plays water, gun, snake with you. Then after quitting the program you can see your 'Score' & 'Attempts'

import random
ATTEMPTS = 0
SCORE = 0
L = ['snake', 'water', 'gun']
user_name = input("Enter your Name: ")
print(f"Hello \"{user_name}\"",end = "\n")
while True:
    while True:
        print("Press 'Q' to exit")
        user_choice = input("Enter your choice (water, gun, snake): ").lower().strip(" ")
        if user_choice == 'q':
            break
        elif not user_choice in L:
            print("Invalid Input\n")
            continue
        else:
            break
    machine_choice = random.choice(L)
    if user_choice == 'q':
        break
    else:
        print(f"User : {user_choice}\nMachine : {machine_choice}")
        if user_choice == 'water' and machine_choice == 'water':
            print("\t\tDraw!")
            ATTEMPTS += 1
        elif user_choice == 'water' and machine_choice == 'gun':
            print("\t\tUser Wins! (Waters makes the gun useless)")
            ATTEMPTS += 1
        elif user_choice == 'water' and machine_choice == 'snake':
            print("\t\tMachine Wins! (Snake drinks the water)")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'gun' and machine_choice == 'water':
            print("\t\tMachine wins! (Water renders the gun useless)")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'gun' and machine_choice == 'gun':
            print("\t\tDraw!")
            ATTEMPTS += 1
        elif user_choice == 'gun' and machine_choice == 'snake':
            print("\t\tUser wins ! (User kills the snake with the gun)")
            ATTEMPTS += 1
        elif user_choice == 'snake' and machine_choice == 'water':
            print("\t\tUser with ! (Snake drinks the water)")
            ATTEMPTS += 1
        elif user_choice == 'snake' and machine_choice == 'gun':
            print("\t\tMachine wins ! (Machine kills the snake with the gun)")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'snake' and machine_choice == 'snake':
            print("\t\tDraw!")
            ATTEMPTS += 1
        else:
            raise ValueError()
        print("---------------------------------------------\n")
print("---------------------------------------------")
print(f"Final Score: {SCORE}\nTotal Attempts: {ATTEMPTS}")
print("---------------------------------------------")

