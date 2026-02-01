import argparse
import string

alphabet = list(string.ascii_lowercase)
alphabet.extend("æøå")
alphabet_size = len(alphabet)

# Opens file and returns it as a string buffer.
# path: path to file to open
def open_file(path):
    file = open(path, "r")
    return file.read()

# Finds index of the to be encrypted/decrypted letter.
# key:      how much letters are shifted
# letter:   letter shifted or to be shifted
# decrypt:  boolean which tells if the operation is encryption or decryption 
def get_index(key, letter, decrypt):
    if decrypt:
        index = alphabet.index(letter) - key
    else: 
        index = alphabet.index(letter) + key

    return index % alphabet_size

# Runs the main algorithm 
# key:      how much letters are shifted
# filename: name of file, or path to file to encrypt/decrypt
# flag:     boolean which tells if the operation is encryption or decryption, true = encryption
def main(key, filename, flag):
    encrypted_message = ""

    # Cast key to int from str
    key = int(key)
    text = open_file(filename)

    for letter in text:
        if (letter in alphabet):
            index = get_index(key, letter.lower(), flag)
            # Maintain case.
            encrypted_message += alphabet[index] if not letter.isupper() else alphabet[index].upper()
        else:
            encrypted_message += letter # We keep special characters and spaces as are
    
    print(encrypted_message)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help = "Number of positions to shift each letter.")
    parser.add_argument("filename", help = "Path to the text file to encrypt or decrypt.")
    parser.add_argument("-d", "--decrypt", action = "store_true",
                        help = "Decrypts the file instead of encrypting")
    
    args = parser.parse_args()
    main(args.key, args.filename, args.decrypt)