from fractions import gcd
from PrimeMath import isPrime
import string

alphabet = string.lowercase()

##
#exponentialCipherEncode
#Description: Given a message, key, and mode, encrypt the message with an Exponential Cipher
# and return the resulting message.
#
#Parameters:
#   plaintext - The message to encode
#   key - The key to encode the message with.  Must satisfy the equation: gcd(key, modKey) = 1
#   p - The prime number to mod the message by.
#   mode - The mode to encode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#
#Return: The resulting ciphertext.
##
def exponentialCipherEncode(plaintext, key, p, mode):
    if not isPrime(p):
        print "ERROR: exponentialCipherEncode: Third argument must be a prime number."
        return
    if gcd(key, p) != 1:
        print "ERROR: exponentialCipherEncode: Key of ", key, " is not valid."
        return

    plaintext.lower().replace(' ', '')

    #Calculate the size of each submessage
    sub = ""
    while True:
        nextSub = ""
        if mode == 0:
            nextSub = "25"
        elif mode == 1:
            nextSub = "122"

        if int(sub + nextSub) >= p:
            break
        else:
            sub += nextSub

    subSize = len(sub) / 2

    #Break the message up into equal pieces
    messagePieces = []
    messagePiece = ""
    i = 0

    for char in plaintext:
        if i == subSize:
            messagePieces.append(messagePiece)
            messagePiece = ""
            i = 0

        if mode == 0:
            index = alphabet.find(char)
            if index < 10:
                messagePiece += "0"
            messagePiece += str(index)
        elif mode == 1:
            asciiIndex = ord(char)
            if asciiIndex < 100:
                messagePiece += "0"
            messagePiece += asciiIndex

        i += 1

    #Now take each submessage and create the ciphertext.
    cipherText = ""
    for piece in messagePieces:
        intPiece = int(piece)
        c = str(pow(intPiece, key) % p)

        #Add leading zeroes until the string is the same size as before
        while len(c) < len(piece):
            c = "0" + c

        cipherText += c

    return cipherText