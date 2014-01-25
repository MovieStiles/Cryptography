###
# Polyalphabetic Ciphers
#  A polyalphabetic cipher one in which the correspondence between plaintext and ciphertext
#  is not 1-1.  Alternatively, it is a substitution cipher using multiple substitution alphabets.
###

###
# Vignere Cipher
#  The problem with monoalphabetic ciphers is that there is a reliable 1-1 relationship
#  between letters in the normal alphabet, and letters in a substitution alphabet.
#  Therefore you can use simple techniques such as letter frequency analysis to crack them.
#  Polyalphabetic ciphers, such as the Vignere Cipher, set out to solve this problem.
#
#  A Vignere cipher uses a keyword to determine the multiple substitution alphabets used in encryption.
#
# Encryption Example: Keyword = "eat"  Message = "blue cheese"
#  Plaintext	B	L	U	E	C	H	E	E	S	E
#  Keyword	    E	A	T	E	A	T	E	A	T	E
#  To encrypt, we shift each letter by distance x-1 where x is the position of the keyword
#  letter in the alphabet.
#
#  Ciphertext	F	L	N	I	C	A	I	E	L	I
#
# Decryption:
#  To decrypt, we first need to ask if this is even a Vignere cipher in the first place.
#  One characteristic is that the letter frequency gets smoothed out.  If we already know,
#  then we don't even need the actual keyword, just what it's length is.
#  From there it's just a monoalphabetic additive cipher.
#
#  As for finding that keyword length...well, that's going to take a lot more work.
#  There are a number of tests you can perform, but none of them are as accurate as
#  one might like, so it's a good idea to conduct multiple tests.
#  These tests are outlined in KeywordLengthTests.py.
###

from LetterFrequency import calcLetterFrequency

##
#vignereCipherEncrypt
#Description: Given a plaintext message and a keyword, use
# the Vignere Cipher to encrypt the message.
#
#Parameters:
#   plainText - The message to encrypt
#   keyword - The keyword used to encrypt the message
#
#Return: The encrypted message
##
def vignereCipherEncrypt(plainText, keyword):
    keyword = keyword.lower().replace(' ', '')
    cipherText = ""

    #Loop through the message and shift each letter based on the keyword
    for i in range(0, len(plainText)):
        #Take the ordinal value of the characters, add them together, then convert the sum
        # back to a character.
        cipherText += chr((ord(plainText[i]) + ord(keyword[i % len(keyword)])) % 26 + 85)

    return cipherText

##
#vignereCipherDecrypt
#Description: Given a ciphertext message and a keyword, use
# the Vignere Cipher to decrypt the message.
#
#Parameters:
#   cipherText - The message to decrypt
#   keyword - The keyword used to decrypt the message
#
#Return: The decrypted message
##
def vignereCipherDecrypt(cipherText, keyword):
    keyword = keyword.lower().replace(' ', '')
    plainText = ""

    #Loop through the message and shift each letter based on the keyword
    for i in range(0, len(cipherText)):
        #Take the ordinal value of the characters, add them together, then convert the sum
        # back to a character.
        plainText += chr((ord(cipherText[i]) - ord(keyword[i % len(keyword)])) % 26 + 97)

    return plainText

##
#messageSplit
#Description: Given a message and a keyword length, split the message
# into a group of submessages equal to the keyword length.
#
#Parameters:
#   message - The message to split
#   keywordLength - The length of the keyword in a Vignere Cipher.
#
#Return: The list of submessages
##
def messageSplit(message, keywordLength):
    subMessages = []
    length = len(message)

    for i in range(0, keywordLength):
        tempString = ""
        for j in range(0, length):
            index = j * keywordLength + i
            if index >= length:
                break

            tempString += message[index]

        if len(tempString) > 0:
            subMessages.append(tempString)

    return subMessages

##
#analyzeSubMessages
#Description: Given a ciphertext message encrypted with the Vignere Cipher
# and a possible keyword length, perform frequency analysis on each section
# of the message that is encoded with the same letter in the keyword.
#
#Parameters:
#   ciphertext - The ciphertext to analyze
#   kwLength - A possible length of the encryption keyword
#
#Return: A list of the top three most likely letters of the keyword for
# each submessage.
##
def analyzeSubMessages(ciphertext, kwLength):
    subs = messageSplit(ciphertext, kwLength)
    possibleLetters = []

    #Loop through the submessages
    for sub in subs:
        freqs = calcLetterFrequency(sub)
        topThree = []
        #Loop through the top 3 most frequent letters
        for i in range(0, 3):
            if freqs[i] is not None:
                key = (26 - (ord(freqs[i]) - 97)) % 26
                topThree.append(chr(key + 97))

        possibleLetters.append(topThree)

    return possibleLetters

def test():
    print vignereCipherEncrypt("bluecheese", "eat")
    print vignereCipherDecrypt(vignereCipherEncrypt("bluecheese", "eat"), "eat")

#Output:
#flnicaieli
#bluecheese