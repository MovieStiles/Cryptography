from .ExponentialCipher import exponentialCipherEncode
from .ExponentialCipher import exponentialCipherDecode

##
#RSAEncode
#Description: Given a message, key, and mode, encrypt the message with the RSA algorithm
# and return the resulting message.
#
#Parameters:
#   plaintext - The message to encode
#   key - The key to encode the message with.  Must satisfy the equation: gcd(key, p-1) = 1
#   p - The prime number to mod the message by.
#   mode - The mode to encode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#   q - A second prime number to be multiplied with the first to create a new value, n.
#   aIsZero - Whether the index of A starts at 0 or not in mode 0. (default: True)
#
#Return: The resulting ciphertext.
##
def RSAEncode(plaintext, key, p, mode, q, aIsZero = True):
    return exponentialCipherEncode(plaintext, key, p, mode, q, aIsZero)

##
#RSAEncode
#Description: Given some ciphertext that has been encrypted using the RSA algorithm,
# decrypt the ciphertext and return the resulting plaintext.
#
#Parameters:
#   plaintext - The message to decode
#   key - The key to decode the message with.  Must satisfy the equation: gcd(key, p-1) = 1
#   p - The prime number to mod the message by.
#   mode - The mode to decode the message with.
#       0 - Convert letters to their alphabetic indexes with A = 0.
#       1 - Convert characters to their ASCII numbers.
#   q - A second prime number to be multiplied with the first to create a new value, n.
#   isDecryptionKey - Whether the key given is the decryption key. (default: True)
#   subSize - The size of each submessage, which you may know ahead of time. (default: None)
#   aIsZero - Whether the index of A starts at 0 or not in mode 0. (default: True)
#
#Return: The resulting ciphertext.
##
def RSADecode(ciphertext, key, p, mode, q, isDecryptionKey = True, subSize = None, aIsZero = True):
    return exponentialCipherDecode(ciphertext, key, p, mode, isDecryptionKey, subSize, q, aIsZero)