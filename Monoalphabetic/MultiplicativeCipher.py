from MultiplicativeKeys import multiplicativeKeyCount
import string

############################################
##   Finding the multiplicative inverse   ##
############################################

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
# with a given key.  The key is assumed to be the encryption key.
# This function assumes that alphabet indexes start at 0.
#
#Parameters:
#   message - The message to be encrypted or decrypted
#   key - The key to use with the cipher
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

def testA0():
    print multiplicativeCipherA0("This is a test message", 5)
    print multiplicativeCipherA0("rjomomarumriummaeu", 5, False)
    print multiplicativeCipherA0("This is a test message", 6)

#Output:
#rjomomarumriummaeu
#thisisatestmessage
#Bad key