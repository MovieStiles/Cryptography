###
# Keyword Cipher
#  A keyword cipher is very similar to caesar shift, except instead of shifting the entire alphabet
#  by a number, the alphabet is shifted by a keyword.
#
#  Let W be a word in plaintext.
#  We can define a keyword cipher with key W as follows:
#    1.	Rewrite W without duplicate letters
#    2.	Write the reduced keyword letter for letter beneath the plaintext alphabet.
#    3.	Write remaining letters in alphabetical order.
#    4. Perform the same letter substitution you should be used to by now.
#
#  For example: Key = fox
#  A   B   C   D   E   F   G   H   I   J   K   L
#  f   o   x   a   b   c   d   e   g   h   i   j...
#
# Encryption Example: Key = crazytrain
#  1. crazytrain -> crazytin
#  2. A -> c   B -> r   C -> a.... you get the idea.
#
#  Now to actually encrypt a word with this:
#  "Here is a test message for your enjoyment" -> "nymybocpyopgyoociytjmwjqmyhdjwgyhp"
#
# Decryption is the same in reverse, assuming you know the keyword.
# If you don't know the keyword, then you once again need to employ frequency analysis
# to try and deduce what the letter correspondences are and what the keyword might be.
###

import string

##
#keywordCipher
#Description: Given a message and keyword, encrypt or decrypt a message
# using a keyword cipher.
#
#Paramters:
#   message - The message to encrypt or decrypt.
#   keyword - The keyword used in the cipher.
#   encrypt - True if encrypting, False otherwise.  True by default.
#
#Return: The resulting message.
##
def keywordCipher(message, keyword, encrypt = True):
    message = message.lower().replace(' ', '')
    alphabet = string.lowercase

    #First, remove repeated characters from the keyword.
    #If anyone reading this can do it faster than O(n^2), let me know.
    keyword = ''.join(sorted(set(keyword), key = keyword.index))

    #Then build the new alphabet.
    newAlpha = keyword + ''.join(sorted(set(alphabet).difference(keyword)))

    #Now construct the new message

    #Normally, this would be the way to go:
    #for char in message:
    #    if encrypt:
    #        newMessage += newAlpha[alphabet.find(char)]
    #    else:
    #        newMessage += alphabet[newAlpha.find(char)]
    #
    #But that's just to make what's going on more clear.  I think we can move on
    # for effeciency's sake by now.
    if encrypt:
        return message.translate(string.maketrans(alphabet, newAlpha))
    else:
        return message.translate(string.maketrans(newAlpha, alphabet))

###
# Another variant exists which also puts an additive cipher on top of the keyword cipher.
# In this case, the cipher is as follows:
#
#  Let W be a word in plaintext and let X be a letter in plaintext alphabet.
#  We can define a keyword cipher with key(W, X) as follows:
#   1.	Rewrite W without duplicate letters
#   2.	Write a reduced keyword letter for letter beneath the plaintext alphabet stating at X.
#   3.	Write remaining letters in alphabetical order.
#
#  Key: (fox, d)
#
# Encryption Example: Key = crazytrain
#  1. crazytrain -> crazytin
#  2. D -> c   E -> r   F -> a.... and so on.
###