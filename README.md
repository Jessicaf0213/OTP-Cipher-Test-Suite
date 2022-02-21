# OTP-Cipher-Test-Suite
Assignment 4 for CSC 151

Author: Jessica Feng

Date: Feb.20, 2022

``cipher.py`` is an app to create one-time pad, encrypy and decrypt messages. 

``decrypted-message.txt`` contains a readable message that will be used for encryption. 

``pad.txt`` contains a given size of random uppercase letters. 

``enctypted-message.txt`` contains the encrypted message, which is encrypted by the readable message using pad. 

``unit-test.py`` contains several tests to check whether functions in ``cipher.py`` works as expected. 

In ``cipher.py``, you can generate a one-time-pad by using function ``generatePad(size)". This function will generate a text file called "OPT.txt" in the directory. In the file, there will be a given number of randomly selected uppercase letters. The number of uppercase letters is decided by the argument size. 
You can also encipher a message using a pad with function ``encipher(pad,plaintxt)``. The argument pad represents a series of random uppercase letter, and the argument plaintxt represents the plainmessage that you want to encrypt. This function will return a encrypted message. 
You can also decipher a message using a pad with function ``decipher(pad,entxt)``. The argument pad represents a series of random uppercase letter, and the argument entxt represents a encrypted message. This function will return a decrypted message.

In ``unit-test.py``, you can check whether the functions in main program run properly. 
The function ``test_generatePad_by_random_size()`` creates a new pad file with random size and passes if a OTP pad does exist in the directory. 
The function ``test_encipher()`` encrypts the plaintext using the given pad file and passes if the resulting string equals to the content in the ``encrypted-message.txt``.
The function ``test_encipher()`` encrypts the plaintext using the given pad file and passes if the resulting string equals to the content in the ``encrypted-message.txt``.
The function ``test_encipher_shift_letters_by_0()`` encrypts "ABCDE" by shifting all letters forward by 0 and passes test if the result is "ABCDE". 
The function ``test_decipher_shift_letters_by_0()`` decrypts "BCDED" by shifting all letters backward by 0 and passes test if the result is "BCDEF".
The function ``test_encipher_shift_letters_by_1()`` encrypts "ABCDE" by shifting all letters forward by 1 and passes test if the result is "BCDEF".
The function ``test_decipher_shift_letters_by_1()`` decrypts "BCDED" by shifting all letters backward by 1 and passes test if the result is "ABCDE".
The function ``test_encipher_shift_letters_by_25()`` encrypts "ABCDE" by shifting all letters forward by 25 and passes test if the result is "ZABCD".
The function ``test_decipher_shift_letters_by_25()`` encrypts "ZABCD" by shifting all letters backward by 25 and passes test if the result is "ABCDE".
The function ``test_encipher_shift_letters_by_25_with_punctuation()`` encrypts "A! BC DE." by shifting all letters forward by 25 and passes test if the result is "Z! AB CD.".
The function ``test_decipher_shift_letters_by_25_with_punctuation()`` encrypts "Z-A.B C?D?" by shifting all letters backward by 25 and passes test if the result is "ABCDE".
