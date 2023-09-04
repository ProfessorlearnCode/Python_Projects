

import random
ALPHABETS = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

# Function to encode the program
def encoder(item):
    if len(item) >= 3:
        first_letter = item[0]
        item = item.removeprefix(first_letter)
        word = item + first_letter            
        word = random.choice(ALPHABETS) + random.choice(ALPHABETS) + random.choice(ALPHABETS) + word + random.choice(ALPHABETS) + random.choice(ALPHABETS) + random.choice(ALPHABETS)
        return word        
    
    elif len(item) < 3:
        word = item[::-1]
        return word
    
    else: 
        print("Invalid Input")

# Function to decode the program
def decoder(item):
    if len(item) < 3:
        item = item[::-1]
        return item
        
    elif len(item) >= 3:
        item = item[3:]
        item = item[:-3] 
        last_letter = item[-1]
        item = item.removesuffix(last_letter)
        word = last_letter + item
        return word
    
    else:
        print("Invalid Input")
        

def main():
    LIST = []
    print("\t\t-------------------------------\n")
    print("\t\t------Encryptor/Decryptor------\n")
    print("\t\t-------------------------------\n")
    print("\t\t            Welcome            \n")
    
    print("Select an option \n1. Encrypt Your Message \n2. Decrypt Your Message")
    choice = input("Enter here: ")
    
    if choice == '1':
        while True:
            message = input("Enter Your Message (q to quit): ").strip(" ")
            encoded_message = encoder(message)            
            if message == 'q':
                break
            if message == ' ':
                pass
            else: 
                LIST.append(encoded_message)
        print()
        print("\t--------Encrypted Message ----------")
        for entry in LIST:
            print(entry,end=" ") 
        print()  
        
    elif choice == '2':
        message = input("Enter Expression (with spaces): ")
        message_tuple = message.split(" ")
        print()
        for entry in message_tuple:
            print(decoder(entry),end=" ")
            
    else:
        print("Invalid input")
               
    
main()