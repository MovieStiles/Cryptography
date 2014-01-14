###
# Caesar Shift
#  A Caesar Shift, otherwise known as an Additive Cipher,
#  takes the letters in a message and shifts them through the alphabet by some integer amount.
#
# Encryption Example: Key = 4
#  craze = 2 17 0 25 4 becomes 6 21 4 29 8 becomes 6 21 4 3 8 = gvedi
#  Any number greater than the index of Z loops back around, otherwise known as mod 26.
#
# Decryption is easy.  Simply subtract the encryption key instead of adding.
# You can also add the additive inverse of the key.
# From the previous example, -4 or 22 would be the decryption key.
###

###
# Additive Inverse
#  The additive inverse of a number, x, is another number, y, where x + y = 0.
#  In normal numbers, this is just simply the negative version.
#  In cases like this, we're only dealing with the numbers 0-25, so this changes slightly.
#  x + y = 0 still holds true, but now all numbers are mod 26, so 4 + 22 = 0
###

import string

##
#caesarShift
#Description: Perform a Caesar Shift on a given message to either encrypt or decrypt the message.
#
#Parameters:
#   message - The text to shift
#   key     - The integer amount to shift the message by.  Assumed to be the encryption key.
#   encrypt - Whether to encrypt the message or decrypt it
#
#Return: The new text after shifting
##
def caesarShift(message, key, encrypt = True):
    message = message.lower().replace(' ', '')
    alphabet = string.lowercase
    newMessage = ""

    #Change shift direction depending on encrypting or decrypting
    if not encrypt:
        key = -key

    #Loop through the message
    for char in message:
        index = alphabet.find(char)
        newMessage += alphabet[(index + key) % 26]

    return newMessage

##
#caesarShiftStringOps
#Description: Same as other caesarShift function, but uses string operations
# since those are implemented in C and therefore somewhat faster.
# Found on Stack Overflow
##
def caesarShiftStringOps(message, key, encrypt = True):
    message = message.lower().replace(' ', '')
    alphabet = string.lowercase

    if not encrypt:
        key = -key

    shiftedAlphabet = alphabet[key:] + alphabet[:key]
    return message.translate(string.maketrans(alphabet, shiftedAlphabet))

##
#test
#Description: A small method to test the outputs of the methods in this file.
##
def test():
    print caesarShift("Test message", 1)
    print caesarShift("uftunfttbhf", 1, False)
    print caesarShiftStringOps("Test message", 1)
    print caesarShiftStringOps("uftunfttbhf", 1, False)

#Output:
#uftunfttbhf
#testmessage
#uftunfttbhf
#testmessage