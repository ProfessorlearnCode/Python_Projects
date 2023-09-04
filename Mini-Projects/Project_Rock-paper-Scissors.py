# Program that plays Rock, Paper, Scissors with you. Then after quitting the program you can see your 'Score' & 'Attempts'

import random
ATTEMPTS = 0
SCORE = 0
L = ['scissors', 'rock', 'paper']
user_name = input("Enter your Name: ")
print(f"Hello \"{user_name}\"")
print()
while True:
    while True:
        print("Press 'Q' to exit")
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower().strip(" ")
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
        if user_choice == 'rock' and machine_choice == 'rock':
            print("\t\tDraw!")
            ATTEMPTS += 1
        elif user_choice == 'rock' and machine_choice == 'paper':
            print("\t\tMachine Wins with Paper!")
            ATTEMPTS += 1
        elif user_choice == 'rock' and machine_choice == 'scissors':
            print("\t\tUser Wins with Rock!")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'paper' and machine_choice == 'rock':
            print("\t\tUser wins with Paper!")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'paper' and machine_choice == 'paper':
            print("\t\tDraw!")
            ATTEMPTS += 1
        elif user_choice == 'paper' and machine_choice == 'scissors':
            print("\t\tMachine wins with Scissors!")
            ATTEMPTS += 1
        elif user_choice == 'scissors' and machine_choice == 'rock':
            print("\t\tMachine with wins Rock!")
            ATTEMPTS += 1
        elif user_choice == 'scissors' and machine_choice == 'paper':
            print("\t\tUser wins with Paper!")
            SCORE +=1
            ATTEMPTS += 1
        elif user_choice == 'scissors' and machine_choice == 'scissors':
            print("\t\tDraw!")
            ATTEMPTS += 1
        else:
            raise ValueError()
        print("---------------------------------------------\n")
print("---------------------------------------------")
print(f"Final Score: {SCORE}\nTotal Attempts: {ATTEMPTS}")
print("---------------------------------------------")

