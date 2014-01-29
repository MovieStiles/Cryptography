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