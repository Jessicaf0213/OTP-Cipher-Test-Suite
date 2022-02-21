from cipher import *
import os.path
import random

# test genereatPad
def test_generatePad_by_random_size():
    # generate OTP in random size (50-1500)
    generatePad(random.randrange(50,1500,1))
    # pass test if a OTP pad file exists
    assert os.path.exists("OTP.txt")

# Read the decrypted msg in the folder
with open("decrypted-message.txt") as file: 
    plaintxt = file.read()
# read the pad in the folder
with open("pad.txt") as file:
    pad = file.read()
# read the encrpted msg in the foler
with open("encrypted-message.txt") as file: 
    entxt = file.read()

def test_encipher(): 
    # encrypt the plaintext using the given pad file
    # pass test if the encrypted message equals the content in encrypted-message.txt
    assert encipher(pad, plaintxt) == entxt

def test_decipher():
    # decrypt the encrypted msg using the given pad file
    # pass test if the decrypted message equals the content in decrypted-message.txt
    assert decipher(pad, entxt) == plaintxt

def test_encipher_shift_letters_by_0():
    # encrypt "ABCDE" by shifting all letters forward by 0
    # pass test if the result is "ABCDE"
    assert encipher("AAAAA", "ABCDE") == "ABCDE"

def test_decipher_shift_letters_by_0():
    # decrypt "BCDED" by shifting all letters backward by 0
    # pass test if the result is "BCDEF"
    assert decipher("AAAAA", "BCDEF") == "BCDEF"

def test_encipher_shift_letters_by_1():
    # encrypt "ABCDE" by shifting all letters forward by 1
    # pass test if the result is "BCDEF"
    assert encipher("BBBBB", "ABCDE") == "BCDEF"

def test_decipher_shift_letters_by_1():
    # decrypt "BCDED" by shifting all letters backward by 1
    # pass test if the result is "ABCDE"
    assert decipher("BBBBB", "BCDEF") == "ABCDE"

def test_encipher_shift_letters_by_25():
    # encrypt "ABCDE" by shifting all letters forward by 25
    # pass test if the result is "ZABCD"
    assert encipher("ZZZZZ", "ABCDE") == "ZABCD"

def test_decipher_shift_letters_by_25():
    # encrypt "ZABCD" by shifting all letters backward by 25
    # pass test if the result is "ABCDE"
    assert decipher("ZZZZZ", "ZABCD") == "ABCDE"

def test_encipher_shift_letters_by_25_with_punctuation():
    # encrypt "A! BC DE." by shifting all letters forward by 25 
    # pass test if the result is "Z! AB CD."
    assert encipher("ZZZZZ", "A! BC DE.") == "Z! AB CD."

def test_decipher_shift_letters_by_25_with_punctuation():
    # encrypt "Z-A.B C?D?" by shifting all letters backward by 25
    # pass test if the result is "ABCDE"
    assert decipher("ZZZZZ", "Z-A.B C?D?") == "A-B.C D?E?"
