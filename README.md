Caesar Cipher
=============
This program is a simple Caesar cipher implementation written in Python. It encrypts or decrypts text files by shifting letters a fixed number of positions in the alphabet. The alphabet is extended with the Norwegian letters æ, ø, and å.

How it works
------------
Each letter is shifted by a numeric key.  
Encryption shifts letters forward.  
Decryption shifts letters backward.  
Wrapping is handled automatically (e.g. shifting past å loops back to a).

Requirements
------------
Python 3

Usage
-----
python3 caesar.py `key` `filename` [-d]

- **key**  
  Number of positions to shift each letter.

- **filename**  
  Path to the text file to encrypt or decrypt.

- **-d, --decrypt** (optional)  
  Decrypts the file instead of encrypting it.
