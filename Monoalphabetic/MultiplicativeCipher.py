###
# Multiplicative Cipher
#  A multiplicative cipher is similar to the Caesar Shift, except instead of adding
#  to the alphabetic index, the index is multiplied.
#
#  Because all of these numbers are mod 26, that means that one result can be shared by multiple
#  multiplications.  For example:
#  4*1 = 4 and 4*14 = 56 = 4
#  This is bad since we don't want multiple letters mapping to one letter, since this will make
#  decryption a nightmare, if not impossible.
#  Therefore, only certain integers are ok to use as keys.  Only integers which are relatively prime with 26
#  make valid keys.  The list of valid keys are: 3 5 7 9 11 15 17 19 21 23 25
#
# Encryption Example: Key = 3 and assuming A = 0
#  craze = 2 17 0 25 4 becomes 6 51 0 75 12 becomes 6 25 0 23 12 = gzaxm
#  I have seen some ciphers that assume A = 1, so I will include the ability to do both.
#
# Decryption:
#  To find the decryption key, you must find the multiplicative inverse of the encryption key.
#  The multiplicative inverse of 3 is 9.
#  gzaxm = 6 25 0 23 12 becomes 54 225 0 207 108 becomes 2 17 0 25 4 = craze
###

###
# Relatively Prime
#  Two numbers are relatively prime when their gcd = 1
###

###
# gcd
#  GCD stands for Greatest Common Divider.  It is the highest number that can evenly divide multiple numbers.
#  A very common algorithm for finding the gcd of two numbers is the Euclidean Algorithm.
###

###
# Multiplicative Inverse
#  The multiplicative inverse of a number, x, is another number, y, such that x*y = 1
#  In the mod 26 world, for example, 3*9 = 27 = 1
#  Not all integers here have a multiplicative inverse, so not all 25 integers can be keys.
#  For example, no possible number can be used for x such that 4*x mod 26 = 1
###

from MultiplicativeKeys import normAlphabetKeys
from LetterFrequency import calcLetterFrequency
import string

##   Finding the multiplicative inverse   ##

#Straight from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

##
#egcd
#Description: Recursive implementation of the Extended Euclidean Algorithm
# to find the gcd of two numbers.
#
#Parameters:
#   a - The first of two numbers to find the gcd of.
#   b - The second of the two numbers.
#
#Return: (g, x, y) such that ax + by = g = gcd(a, b)
##
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

##
#modinv
#Description: Find the multiplicative inverse of a number under a certain field
#
#Parameters:
#   a - The number to find the multiplicative inverse of
#   m - The modulo of the field
#
#Return: The multiplicative inverse of a if it exists
##
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

##############################################

##
#multiplicativeCipher
#Description: Either encrypt or decrypt a message with a multiplicative cipher
# with a given key.  This function assumes that alphabet indexes start at 0.
#
#Parameters:
#   message - The message to be encrypted or decrypted
#   key - The key to use with the cipher.  Assumed to be the encryption key.
#   encrypt - True if encrypting, False otherwise.  True by default.
#   aIsZero - Whether or not the index of A is assumed to be zero.  True by default.
#
#Return: The new message
##
def multiplicativeCipher(message, key, encrypt = True, aIsZero = True):
    message = message.lower().replace(' ', '')
    alphabet = string.lowercase
    newMessage = ""

    #Switch to the multiplicative inverse if decrypting
    if not encrypt:
        key = modinv(key, 26)

    #If a multiplicative inverse couldn't be found or if it's an invalid key
    if key is None or not (key in normAlphabetKeys):
        return "Bad key"

    #Loop through the message
    for char in message:
        #Adjust where we look depending on if A is assumed to be index 0 or 1
        if aIsZero:
            index = alphabet.find(char)
            newMessage += alphabet[(index * key) % 26]
        else:
            index = alphabet.find(char) + 1
            newMessage += alphabet[(index * key) % 26 - 1]

    return newMessage

##
#findLikelyKeys
#Description: Find up to the top five most likely keys of a message encrypted with a
# multiplicative cipher and return the resulting messages along with the keys.
# Takes heavy advantage of the fact that the letter E is the most common letter in English.
#
#Parameters:
#   message - The message to try and decrypt.
#   aIsZero - Whether or not the index of A is assumed to be zero.  True by default.
#
#Return: A dictionary of the messages and keys.
##
def findLikelyKeys(message, aIsZero = True):
    #The list of letters that E can become is as finite as the list of keys.
    letters = ['o', 'y', 'i', 's', 'c', 'w', 'g', 'q', 'a', 'k', 'u']
    #Get the list of frequencies, sorted by most frequent.
    frequencies = calcLetterFrequency(message)
    possibles = {}

    for charFreq in frequencies:
        #Move on if the letter is not one of the possible mappings of E
        if charFreq[0] not in letters:
            continue

        #Grab the key associated with the letter and get the decoding key.
        index = letters.index(charFreq[0])
        key = modinv(normAlphabetKeys[index], 26)

        #Add the key and the resulting decoded message to dictionary.
        possibles[key] = multiplicativeCipher(message, key, False, aIsZero)

        #Keep it to the top 5 at maximum
        if len(possibles) > 4:
            break

    return possibles

##
#test
#Description: A small method to test the outputs of the methods in this file.
##
def test():
    print multiplicativeCipher("This is a test message", 5)
    print multiplicativeCipher("rjomomarumriummaeu", 5, False)
    print multiplicativeCipher("This is a test message", 6)
    print multiplicativeCipher("This is a test message", 5, True, False)
    print multiplicativeCipher("vnsqsqevyqvmyqqeiy", 5, False, False)

    for keyAndVal in findLikelyKeys("rjomomarumriummaeu").items():
        print "Decode Key: ", keyAndVal[0], "   Resulting message: ", keyAndVal[1]

#Output:
#rjomomarumriummaeu
#thisisatestmessage
#Bad key
#vnsqsqevyqvmyqqeiy
#thisisatestmessage
#Decode Key:  25    Resulting message:  jrmomoajgojsgooawg
#Decode Key:  15    Resulting message:  plugugapkgpekggack
#Decode Key:  5    Resulting message:  thisisatestmessage
#Decode Key:  9    Resulting message:  zbqkqkazikzyikkami