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
#  Therefore, only certain integers are ok to use as keys.  Only integers which are coprime with 26
#  make valid keys.  The list of valid keys are: 3 5 7 9 11 15 17 19 21 23 25
#
# Encryption Example: Key = 3 and assuming A = 0
#  craze = 2 17 0 25 4 becomes 6 51 0 75 12 becomes 6 25 0 23 12 = gzaxm
#
# Decryption:
#  To find the decryption key, you must find the multiplicative inverse of the encryption key.
#  The multiplicative inverse of 3 is 9.
#  gzaxm = 6 25 0 23 12 becomes 54 225 0 207 108 becomes 2 17 0 25 4 = craze
###

###
# Coprime
#  Two numbers are coprime when their gcd = 1
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

from MultiplicativeKeys import multiplicativeKeyCount
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
#   encrypt - True if encrypting, False otherwise
#
#Return: The new message
##
def multiplicativeCipherA0(message, key, encrypt = True):
    message = message.lower().replace(' ', '')
    alphabet = string.lowercase
    newMessage = ""

    keyList = multiplicativeKeyCount(26)[1]

    if not encrypt:
        key = modinv(key, 26)

    #If a multiplicative inverse couldn't be found or if it's an invalid key
    if key is None or not (key in keyList):
        return "Bad key"

    #Loop through the message
    for char in message:
        index = alphabet.find(char)
        newMessage += alphabet[(index * key) % 26]

    return newMessage

##
#testA0
#Description: A small method to test the outputs of the methods in this file.
# Specifically the ciphering method that assumes the index of A is 0.
##
def testA0():
    print multiplicativeCipherA0("This is a test message", 5)
    print multiplicativeCipherA0("rjomomarumriummaeu", 5, False)
    print multiplicativeCipherA0("This is a test message", 6)

#Output:
#rjomomarumriummaeu
#thisisatestmessage
#Bad key