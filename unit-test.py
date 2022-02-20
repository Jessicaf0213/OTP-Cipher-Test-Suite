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
    assert encipher(pad, plaintxt) == entxt

def test_decipher():
    # decrypt the encrypted msg using the given pad file
    assert decipher(pad, entxt) == plaintxt

def test_encipher_shift_letters_by_1():
    assert encipher("BBBBB", "ABCDE") == "BCDEF"

def test_decipher_shift_letters_by_1():
    assert decipher("BBBBB", "BCDEF") == "ABCDE"

def test_encipher_shift_letters_by_25():
    assert encipher("YYYYY", "A! BCDE") == "Y! ZABC"

def test_decipher_shift_letters_by_25():
    assert decipher("YYYYY", "Y ?ZAB C") == "A ?BCD E"

