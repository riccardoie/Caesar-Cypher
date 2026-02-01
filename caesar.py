import argparse
import string

class CaesarCipher:

    def __init__(self, key, alphabet_type = 0):
        self.key = key

        # For now only norwegian alphabet, expand to support other alphabets too
        if(alphabet_type == 0):
            self.alphabet = list(string.ascii_lowercase)
            self.alphabet.extend("æøå")     
            self.alphabet_size = len(self.alphabet)
    
    # Runs the cipher algorithm.
    # letter:   letter shifted or to be shifted
    # key:      how much letters are shifted
    def __caesar_cipher__(self, letter, key):
        if (letter.lower() in self.alphabet):
            index = (self.alphabet.index(letter.lower()) + key) % self.alphabet_size
  
            # Maintain case.
            return self.alphabet[index] if not letter.isupper() else self.alphabet[index].upper()
        else:
            return letter # We keep special characters and spaces as are
    
    # Encrypts text string by using __caesar_cipher__
    # text:     string buffer
    def encrypt(self, text):
        encrypted_message = "".join(map (lambda letter: self.__caesar_cipher__ (letter, self.key), text))

        return encrypted_message
    
    # Decrypts text string by using __caesar_cipher__
    # text:     string buffer
    def decrypt(self, text):
        decrypted_message = "".join(map (lambda letter: self.__caesar_cipher__ (letter, -self.key), text))

        return decrypted_message


# Opens file and returns it as a string buffer.
# path: path to file to open
def open_file(path):
    with open(path, "r") as file:
        file = file.read()
    return file

# Main function to run the algorithm
# key:      how much letters are shifted
# filename: name of file, or path to file to encrypt/decrypt
# flag:     boolean which tells if the operation is encryption or decryption, true = encryption
def main(key, filename, flag):
    text = open_file(filename)
    caesar = CaesarCipher(key)

    if flag:
        result = caesar.decrypt(text)
    else:
        result = caesar.encrypt(text)

    print(result)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("key", type = int, help = "Number of positions to shift each letter.")
    parser.add_argument("filename", help = "Path to the text file to encrypt or decrypt.")
    parser.add_argument("-d", "--decrypt", action = "store_true",
                        help = "Decrypts the file instead of encrypting")
    
    args = parser.parse_args()
    main(args.key, args.filename, args.decrypt)