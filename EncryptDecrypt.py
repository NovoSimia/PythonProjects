import random
import string

original_set=list(" "+string.punctuation+string.digits+string.ascii_letters)
key=original_set.copy()
random.shuffle(key)

##Check if the original_set and keys are generated as you envisioned it
# print("\n",original_set,"\n")
# print(key,"\n")

def encrypt(phrase):
    encrypted_phrase=""
    for i in phrase:
        encrypted_phrase+=key[original_set.index(i)]
    
    return encrypted_phrase


def decrypt(phrase):
    decrypted_phrase=""
    for i in phrase:
        decrypted_phrase+=original_set[key.index(i)]
    
    return decrypted_phrase