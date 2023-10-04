# Password Manager and Password Generator

'''
Features of Password Manager
- Make an encrypted file in which all passwords are stored with their websites
- Decrypt the contents the show the specified output
- Retrieve a specific password from the name of the website/platform
- Show all the passwords stored in the encrypted file
- Allow you to store(append) new passwords with websites/platform
- Read and Write from an encrypted file --> decode it then show the output

'''

from cryptography.fernet import Fernet
import sys
from pass_generator import password_generator

# Generating Key --> Used for encryption and Decryption
def key_generate():
    generated_key = Fernet.generate_key()

    return generated_key

# Using key to encrypt a message
def encryption(key, custom_message):
    secret_message_enc = key.encrypt(f"{custom_message}".encode())
    return secret_message_enc


# Using key to decrypt a message
def decryption(key, secret_message_enc):
    secret_message_dec = key.decrypt(secret_message_enc)
    return secret_message_dec


def main():
    Generated_key = key_generate()
    key_value = Fernet(Generated_key)


    print('''
        1. Create a New key
        2. Create a New Password File
        3. Encrypt a file
        4. Decrypt a file
        5. Get a password from existing enc_file
        6. Add a new password to a file
        7. Suggest a new password from password generator
        Q to Quit
    ''')

    choice = input("Choice? ")
    match choice:
        case '1':   # New key generation
            # Storing the key in a file (This will create a new key everytime)
            key_file_name = input("Enter key name: ")
            with open(f"{key_file_name}", 'bw') as key_file:
                key_file.write(Generated_key)
            print("Processing Complete")

            print("----------------------------\nKey is created")


        case '2':   # New Pass_file generation
            # Prompts the user to enter a website and password and stores it in a dictionary
            data_dictionary = {}
            for _ in range(100):
                website = input("Enter Website: ").lower()
                password = input("Enter Password: ")

                data_dictionary.update({website : password})

                exit = input("Do you like to enter in a new password entry? Y/N: ").lower()
                if exit == 'y':
                    continue
                elif exit == 'n':
                    break
                else:
                    print("invalid input")
                    exit2 = input("Do you like to enter in a new password entry? Y/N: ").lower()
                    if exit2 == 'y':
                        continue
                    elif exit2 == 'n':
                        break
                    else:
                        break

            # Saves the contents of the dictionary in the file called 'password file'
            with open(f"passwords", 'w') as passwords:
                for key, value in data_dictionary.items():
                    passwords.write(f"{key} : {value}\n")

            print("----------------------------\nPassword File is created")


        case '3':   # Encryption of Pass_file

            # Reads the data from the password file and key file
            password_file_name = input("Enter File name: ").lower()
            key_file_name = input("Enter key name: ")
            try:
                with open(f'{key_file_name}', 'rb') as key:
                    key = key.read()

                    # Making the object of the saved encrypted key
                    f_object = Fernet(key)

                with open(f'{password_file_name}', 'rb') as file:
                    file = file.read()


            # Encrypts the file data using the key
                encrypted_data = encryption(f_object, file)

            # Writes the encrypted data to a file
                encrypted_file_name = input("Encrypted File name: ")
                with open(f'{encrypted_file_name}', 'wb') as enc_file:
                    enc_file.write(encrypted_data)


                print("----------------------------\nEncrypted File is created")

            except FileNotFoundError:
                print("File or key not found || does not exists")


        case '4':   # Decryption of Pass_file

            # Reads the data from the password file and key file
            password_file_name = input("Enter Encrypted File name: ")
            key_file_name = input("Enter key name: ")
            try:
                with open(f'{key_file_name}', 'rb') as key:
                    key = key.read()

                    # Making the object of the saved encrypted key
                    f_object = Fernet(key)

                with open(f'{password_file_name}', 'r') as file:
                    file = file.read()


            # deccrypts the file data using the key
                decrypted_data = decryption(f_object, file)
                print("Processing complete\n")

            # Writes the decrypted data to a file
                decrypted_file_name = input("Decrypted File name: ")
                with open(f'{decrypted_file_name}', 'wb') as dec_file:
                    dec_file.write(decrypted_data)


                print("----------------------------\nDecrypted File is created")

            except FileNotFoundError:
                print("File or key not found || does not exists")


        case '5':   # Getting a specific password from an existing enc_file
            # Reads the data from the password file and key file
            encrypted_file_name = input("Enter Encrypted File name: ")
            key_file_name = input("Enter key name: ")
            try:
                with open(f'{key_file_name}', 'r') as key:
                    key = key.read()

                    # Making the object of the saved encrypted key
                    f_object = Fernet(key)


                with open(f'{encrypted_file_name}', 'r') as file:
                    file = file.read()


            # deccrypts the file data using the key
                decrypted_data = decryption(f_object, file)
                print("Processing complete\n")


            # decoding and cleaning the contents of the byte-data into str
                decode_decryption = decrypted_data.decode().lstrip('b').strip("''")
                decode_decryption = decode_decryption.split('\\r\\n')

            # Check whether the entry is present in the file
                user_input = input("Enter your Website (Q to exit): ")
                checker = 0
                for i in decode_decryption:
                    if user_input in i:
                        print(i)
                        checker +=1
                        sys.exit()

                if checker == 0:
                    print("Entry not found! Try Again")

                if user_input == 'q':
                    sys.exit()


                # Secret code to view all passwords
                if user_input == 'cs50':
                    for _ in decode_decryption:
                        print("All passwords")
                        print(_)

            except FileNotFoundError:
                print("File or key not found || does not exists")


        case '6':   # Adding a new Password

            try:

                # Getting new entry from the user
                new_website = input("Enter your new website: ").lower()
                new_password = input("Enter your new Password: ")
                encrypted_entry = f"\n{new_website} : {new_password}"

                # Encrypting the data with the same key
                # encrypted_entry = encryption(f_object, new_entry)

                # adding the entry to the orginal file
                with open(f'passwords', 'a+') as new_entry_file:
                    new_entry_file.write(encrypted_entry)


            # Then over-writing the encrypted file

            # Reads the data from the password file and key file
                password_file_name = input("Enter File name: ").lower()
                key_file_name = input("Enter key name: ")
                with open(f'{key_file_name}', 'rb') as key:
                    key = key.read()

                    # Making the object of the saved encrypted key
                    f_object = Fernet(key)

                with open(f'{password_file_name}', 'rb') as file:
                    file = file.read()


            # Encrypts the file data using the key
                encrypted_data = encryption(f_object, file)

            # Writes the encrypted data to a file
                encrypted_file_name = input("Encrypted File name: ")
                with open(f'{encrypted_file_name}', 'wb') as enc_file:
                    enc_file.write(encrypted_data)


                print("----------------------------\nNew Entry added to Encrypted file")

            except FileNotFoundError:
                sys.exit("File or key not found || does not exists")

        case '7':   # New password Suggestion
            random_password = password_generator()
            print(f"Your generated Password is: {random_password}")

        case 'q':   # Quit the program
            print("Bye")
            sys.exit()

        case _:     # Miscellaneous Number input
            print("Invalid Choice Input")

if __name__ == '__main__':
    main()
