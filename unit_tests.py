import unittest
from caesar import CaesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic_shift(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.encrypt("abc"), "def")

    def test_decrypt_basic_shift(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.decrypt("def"), "abc")

    def test_wrap_around(self):
        cipher = CaesarCipher(3)
        self.assertEqual(cipher.encrypt("æøå"), "abc")

    def test_wrap_around_big_number(self):
        cipher = CaesarCipher(250)
        self.assertEqual(cipher.encrypt("æøå"), "pqr")

    def test_preserves_case(self):
        cipher = CaesarCipher(1)
        self.assertEqual(cipher.encrypt("AbC"), "BcD")

    def test_non_alphabet_characters(self):
        cipher = CaesarCipher(5)
        self.assertEqual(cipher.encrypt("hello, world!"), "mjqqt, øtwqi!")

    def test_negative_encrypt(self):
        cipher = CaesarCipher(-5)
        self.assertEqual(cipher.encrypt("hello, world!"), "cåggj, rjmgø!")
        self.assertEqual(cipher.decrypt("cåggj, rjmgø!"), "hello, world!")
    
    def test_key_zero(self):
        cipher = CaesarCipher(0)
        self.assertEqual(cipher.encrypt("hello, world!"), "hello, world!")
        self.assertEqual(cipher.decrypt("hello, world!"), "hello, world!")
    
    def test_empty_text(self):
        cipher = CaesarCipher(4)
        self.assertEqual(cipher.encrypt(""), "")
        self.assertEqual(cipher.decrypt(""), "")
        
        
    def test_encrypt_decrypt_roundtrip(self):
        cipher = CaesarCipher(7)
        with open("plaintext.txt", "r") as file:
            file = file.read()
        encrypted = cipher.encrypt(file)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, file)

if __name__=="__main__":
    unittest.main()