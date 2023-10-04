# Exercise # 3 : About the implementation of the lists, tuples and loops (Kaun Banne ga CarorePati)
##############################################################################



import os
   

questions = (
    "What is the capital of France?",
    "How many continents are there on Earth?",
    'Which planet is known as the "Red Planet"?',
    "What is the largest mammal in the world?",
    "Which gas do plants use for photosynthesis?",
    "What is the process by which plants make their own food using sunlight?",
    "Who painted the Mona Lisa?",
    "What is the primary gas that makes up Earth's atmosphere?",
    "Which is the largest ocean on Earth?",
    "Which of the following is a primary color?",
)

choices = (
    ("a) London" , "b) Berlin" , "c) Paris" , "d) Rome"),
    ("a) 5" , "b) 6" , "c) 7" , "d) 8"),
    ("a) Venus", "b) Mars" , "c) Jupiter" , "d) Saturn"),
    ("a) Elephant" , "b) Giraffe" , "c) Blue whale" , "d) Lion"),
    ("a) Oxygen" , "b) Nitrogen" , "c) Carbon dioxide" , "d) Hydrogen"),
    ("a) Respiration" , "b) Photosynthesis" , "c) Digestion" , "d) Fermentation"),
    ("a) Vincent van Gogh" , "b) Leonardo da Vinci" , "c) Pablo Picasso" , "d) Michelangelo"),
    ("a) Oxygen" , "b) Carbon dioxide" , "c) Nitrogen" , "d) Hydrogen"),
    ("a) Atlantic Ocean" , "b) Indian Ocean" , "c) Arctic Ocean" , "d) Pacific Ocean"),
    ("a) Orange" , "b) Green" , "c) Purple" , "d) Blue")
    )

money_list = (
    "$1", 
    "$10",
    "$100",
    "$10,000",
    "$100,000",
    "$250,000",
    "$500,000",
    "$750,000",
    "$900,000",
    "$1,000,000",
    )

answers = ("c",
           "b",
           "b",
           "a",
           "c",
           "b",
           "b",
           "c",
           "d",
           "d",
           )

score = 0
counter = 1
choice_number = 0


print("-------------------------- ")
print("------Welcome to KBC------")
print("--------------------------",end="\n")


print("Money Jackpot")
for money in money_list:
    print(money,"\n")
    

print("Question Follow-up")
for question in questions:
    print(f"\nQ.{counter}:{question}")
    for choice in choices[choice_number]:
        print(choice)
    print("--------------------------------")
    userinput = input("Enter your answer choice: ").lower()
    if userinput == answers[choice_number]:
        score += 1
        print(f"You won {money_list[choice_number]} ")
    else:
        break
    
    counter += 1
    choice_number +=1
    
    
os.system('cls')
print(f"Congratulations!! You have won {money_list[score]}\n\n")
