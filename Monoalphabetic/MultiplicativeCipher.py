from MultiplicativeKeys import normAlphabetKeys
from LetterFrequency import calcLetterFrequency
from CryptoMath import modinv
import string

def multiplicativeCipher(message, key, encrypt = True, aIsZero = True):
    """Either encrypt or decrypt a message with a multiplicative cipher
        with a given key.  This function assumes that alphabet indexes start at 0.

    Args:
        message: The message to be encrypted or decrypted.
        key: The key to use with the cipher.  Assumed to be the encryption key.
        encrypt: True if encrypting, False otherwise. (default: True)
        aIsZero: Whether or not the index of A is assumed to be zero. (default: True)

    Returns:
        The resulting message.
    """
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

def findLikelyKeys(message, aIsZero = True):
    """Find up to the top five most likely keys of a message encrypted with a
        multiplicative cipher and return the resulting messages along with the keys.
        Takes heavy advantage of the fact that the letter E is the most common letter in English.

    Args:
        message: The message to try and decrypt.
        aIsZero: Whether or not the index of A is assumed to be zero. (default: True)

    Returns:
        A dictionary of the messages and keys.
    """
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

def test():
    """A small function to test the outputs of the methods in this file.
    """
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