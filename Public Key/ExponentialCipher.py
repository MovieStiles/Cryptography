from fractions import gcd
from CryptoMath import isPrime
from CryptoMath import modinv
import string
import re

##
#calcMultInverse
#Description: Calculate the multiplicative inverse of a number given the
# prime number(s) that you are using in your Exponential Cipher
#
#Parameters:
#   n - The number you want the multiplicative inverse of.
#   p - The prime number you are using in your cipher.
#   q - The optional second prime number you are using. (default: None)
#
#Return: The multiplicative inverse of n.
##
def calcMultInverse(n, p, q = None):
    if q is None:
        return modinv(n, p-1)
    else:
        return modinv(n, (p-1)*(q-1))

##
#calcSubMessageSize
#Description: Calculate the maximum size a submessage can be, given the mod p
# used in the encryption or decryption and what mode is being used.
#
#Parameters:
#   p - The prime number to mod the message by.
#   mode - The mode to encode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#
#Return: The maximum size of each submessage.
##
def calcSubMessageSize(p, mode):
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
    if mode == 0:
        return len(sub) / 2
    elif mode == 1:
        return len(sub) / 3

##
#splitMessageAndConvert
#Description, given a message and submessage size, split the message into the
# appropriate number of submessages and do the necessary conversions to numbers.
#
#Parameters:
#   message - The message to split
#   subSize - The size of the submessages
#   mode - The mode to encode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#   aIsZero - Whether the index of A starts at 0 or not. (default: True)
#
#Return: The list of submessages.
##
def splitMessageAndConvert(message, subSize, mode, aIsZero = True):
    alphabet = string.ascii_lowercase
    messagePieces = []
    messagePiece = ""
    i = 0

    for char in message:
        if i == subSize:
            messagePieces.append(messagePiece)
            messagePiece = ""
            i = 0

        #If the message is being converted to their alphabetic indexes
        if mode == 0:
            index = alphabet.find(char)

            if not aIsZero:
                index += 1

            if index < 10:
                messagePiece += "0"
            messagePiece += str(index)
        #If the message is being converted to ASCII
        elif mode == 1:
            asciiIndex = ord(char)
            if asciiIndex < 100:
                messagePiece += "0"
            messagePiece += asciiIndex

        i += 1

    #Pad the last piece with zeroes if need be.
    if len(messagePieces[-1]) != subSize:
        messagePieces[-1] = messagePieces[-1].ljust(subSize, '0')

    return messagePieces

##
#exponentialCipherEncode
#Description: Given a message, key, and mode, encrypt the message with an Exponential Cipher
# and return the resulting message.
#
#Parameters:
#   plaintext - The message to encode
#   key - The key to encode the message with.  Must satisfy the equation: gcd(key, p-1) = 1
#   p - The prime number to mod the message by.
#   mode - The mode to encode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#   q - An optional second prime number which can be multiplied with the first to create a new n. (default: None)
#   aIsZero - Whether the index of A starts at 0 or not in mode 0. (default: True)
#
#Return: The resulting ciphertext.
##
def exponentialCipherEncode(plaintext, key, p, mode, q = None, aIsZero = True):
    if not isPrime(p):
        print("ERROR: exponentialCipherEncode: Third argument must be a prime number.")
        return

    if q is None:
        n = p
        phi = p - 1
        if gcd(key, phi) != 1:
            print("ERROR: exponentialCipherEncode: Key of ", key, " is not valid.")
            return
    else:
        if not isPrime(q):
            print("ERROR: exponentialCipherEncode: Fifth argument must be a prime number.")
            return
        n = p*q
        phi = (p - 1)*(q - 1)
        if gcd(key, phi) != 1:
            print("ERROR: exponentialCipherEncode: Key of ", key, " is not valid.")
            return

    #If we're using the alphabetic indices, we need to clean the message
    if mode == 0:
        plaintext.lower()
        plaintext = "".join(c for c in plaintext if c.isalpha())

    #Calculate the size of each submessage
    subSize = calcSubMessageSize(n, mode)

    #Break the message up into equal pieces
    messagePieces = splitMessageAndConvert(plaintext, subSize, mode, aIsZero)

    #Now take each submessage and create the ciphertext.
    ciphertext = ""
    for piece in messagePieces:
        intPiece = int(piece)
        c = str(pow(intPiece, key) % n)

        #Add leading zeroes until the string is the same size as before
        if len(c) < len(piece):
            c = c.zfill(len(piece))

        ciphertext += c

    return ciphertext

##
#exponentialCipherDecode
#Description: Given some ciphertext that has been encrypted using an Exponential Cipher,
# decrypt the ciphertext and return the resulting plaintext.
#
#Parameters:
#   plaintext - The message to decode
#   key - The key to decode the message with.  Must satisfy the equation: gcd(key, p-1) = 1
#   p - The prime number to mod the message by.
#   mode - The mode to decode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#   isDecryptionKey - Whether the key given is the decryption key. (default: True)
#   subSize - The size of each submessage, which you may know ahead of time. (default: None)
#   q - An optional second prime number which can be multiplied with the first to create a new n. (default: None)
#   aIsZero - Whether the index of A starts at 0 or not in mode 0. (default: True)
#
#Return: The resulting plaintext.
##
def exponentialCipherDecode(ciphertext, key, p, mode, isDecryptionKey = True, subSize = None, q = None, aIsZero = True):
    if not isPrime(p):
        print("ERROR: exponentialCipherEncode: Third argument must be a prime number.")
        return

    if q is None:
        n = p
        phi = p - 1
        if gcd(key, phi) != 1:
            print("ERROR: exponentialCipherDecode: Key of ", key, " is not valid.")
            return
    else:
        if not isPrime(q):
            print("ERROR: exponentialCipherDecode: Fifth argument must be a prime number.")
            return
        n = p*q
        phi = (p - 1)*(q - 1)
        if gcd(key, phi) != 1 and not isDecryptionKey:
            print("ERROR: exponentialCipherDecode: Key of ", key, " is not valid.")
            return

    ciphertext.lower().replace(' ', '')
    alphabet = string.ascii_lowercase

    #Calculate the decryption key if needed
    if not isDecryptionKey:
        key = modinv(key, phi)

    #Calculate the size of each submessage
    if subSize is None:
        subSize = calcSubMessageSize(n, mode)

    #Break the message up into equal pieces
    #No need for any conversion since the ciphertext is already numbers.
    pattern = '.{' + str(subSize) + '}'
    messagePieces = re.findall(pattern, ciphertext)

    #Now take each submessage and create the ciphertext.
    plaintext = ""
    for piece in messagePieces:
        intPiece = int(piece)
        plainNums = str(pow(intPiece, key) % n)

        #Add leading zeroes until the string is the same size as before
        while len(plainNums) < len(piece):
            plainNums = "0" + plainNums

        #Now convert each submessage from their numeric to their alphabetic form
        subPieces = None
        if mode == 0:
            subPieces = re.findall('..', plainNums)
        elif mode == 1:
            subPieces = re.findall('...', plainNums)

        for subPiece in subPieces:
            if mode == 0:
                if aIsZero:
                    plaintext += alphabet[int(subPiece)]
                else:
                    plaintext += alphabet[int(subPiece) - 1]
            elif mode == 1:
                plaintext += chr(int(subPiece))

    return plaintext

def test():
    print(exponentialCipherDecode("125246", 33, 71, 0, False, 2, None, False))

#Output:
#sun