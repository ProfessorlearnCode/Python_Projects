# Password Generator
'''
Features of Password Generators
- Provides Password with 10
- Makes passwords from a collection of lowercase/uppercase and special Symbols 

'''
import random

def password_generator():
    
    # Collection of data
    lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabets = lowercase_alphabets.upper()
    special_characters = '!@#$%^&*()-_={}[]/,.'
    all = lowercase_alphabets + uppercase_alphabets + special_characters


    # Length of the password
    length = 10


    # Password Generate
    password = ''
    for _ in range(length):
        password = ''.join([password, random.choice(all)])    

    return password
  
    
def main():
    password = password_generator()   
    print("Random Passoword Generated:", password)
    
    
if __name__ =="__main__":
    main()