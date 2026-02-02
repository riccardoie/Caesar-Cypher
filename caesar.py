import argparse
import string

class CaesarCipher:
    '''
    Simple Caesar cipher class that lets you encrypt or decrypt text strings

    Attributes:
        key(int): How much letters are shifted.
        alphabet_type(int): Tells the class which alphabet to use, defaults to norwegian
    '''

    def __init__(self, key, alphabet_type = 0):
        self.key = key

        # For now only norwegian alphabet, expand to support other alphabets too
        if(alphabet_type == 0):
            self.alphabet = list(string.ascii_lowercase)
            self.alphabet.extend("æøå")     
            self.alphabet_size = len(self.alphabet)

            self.index = {char: i for i, char in enumerate(self.alphabet)}
            
    def _caesar_cipher(self, letter, key):
        '''
        Runs the cipher algorithm

        :param letter: Letter shifted or to be shifted.
        :param key: How much letters are shifted.
        '''
        lower = letter.lower()

        if lower not in self.index:
            return letter  # keep spaces, punctuation, etc.

        i = self.index[lower]
        shifted = self.alphabet[(i + key) % self.alphabet_size]

        return shifted.upper() if letter.isupper() else shifted

    def encrypt(self, text):
        '''
        Encrypts text string by using _caesar_cipher.

        :param text: String buffer.
        '''
        encrypted_message = "".join(map (lambda letter: self._caesar_cipher (letter, self.key), text))
        return encrypted_message

    def decrypt(self, text):
        '''
        Decrypts text string by using _caesar_cipher.

        :param text: String buffer.
        '''
        decrypted_message = "".join(map (lambda letter: self._caesar_cipher (letter, -self.key), text))
        return decrypted_message


def open_file(path):
    '''
    Opens file and returns it as a string buffer.
    
    :param path: Path to file to open.
    '''
    with open(path, "r") as file:
        file = file.read()
    return file

def main(key, filename, flag):
    '''
    Main function to run the algorithm.

    :param key(int): How much letters are shifted.
    :param filename(str): Name of file, or path to file to encrypt/decrypt.
    :param flag(bool): Tells if the operation is encryption or decryption, true = encryption.
    '''
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