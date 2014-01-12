import string

##
#caesarShift
#Description: Perform a Caesar Shift on a given message to either encrypt or decrypt the message.
# This is also known as an Additive Cipher
# A Caesar Shift takes the letters in a message and shifts them through the alphabet by some integer amount.
# Encryption shifts to the right, while decryption shifts to the left.
#
#Parameters:
#   message - The text to shift
#   key     - The integer amount to shift the message by
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

print caesarShift("Test message", 1)
print caesarShift("uftunfttbhf", 1, False)
print caesarShiftStringOps("Test message", 1)
print caesarShiftStringOps("uftunfttbhf", 1, False)

#Output:
#uftunfttbhf
#testmessage
#uftunfttbhf
#testmessage