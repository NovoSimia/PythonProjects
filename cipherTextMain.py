import CipherText.EncryptDecrypt as EncryptDecrypt
import time
import os

#call the function below whenever you want to clear the terminal outputs
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


original_phrase = []
print("\n\n               WELCOME USER")
for i in range(0,4):
    clear()
    time.sleep(0.7)
    print("Loading....")
    time.sleep(0.7)

while True:
    
    clear()
    choice=input("""1. Key and return 1 to encrypt a phrase
2. Key and return 2 to decrypt a phrase
3. Key and return 3/e/exit to exit
\n""").lower()
    
    if choice in ['3','e','exit']:
        clear()
        break

    match choice:
        case '1':
            original_phrase=input("\n\nEnter the phrase: ")
            encryptedPhrase=EncryptDecrypt.encrypt(original_phrase)
            print(f'Encrypted version of {original_phrase} is {encryptedPhrase}')
            input("\nhit return or type whatever you want and hit return to continue....")
        
        case '2':
            original_phrase=input("\n\nEnter the phrase: ")
            decryptedPhrase=EncryptDecrypt.decrypt(original_phrase)
            print(f'Decrypted version of {original_phrase} is {decryptedPhrase}')
            input("\nhit return or type whatever you want and hit return to continue....")
        
        case _:
            print("\n\n!! No valid option selected.\n\nRestarting")
            time.sleep(1/2)
            print(".")
            time.sleep(1/2)
            print(". ")
            time.sleep(1/2)
            print(".")
            time.sleep(1/2)
            print(".")
            
    
# for i in reversed(original_phrase):
#     print(original_phrase.index(i))

