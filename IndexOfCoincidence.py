from LetterFrequency import calcLetterFrequency

##
#findIndexOfCoincidence
#Description: Given a message, find the possible IC.  Works better the longer the message.
#
#Parameters:
#   message - The message to evaluate.  Assumed to have no punctuation.
#
#Return: The IC of the text.
##
def findIndexOfCoincidence(message):
    message = message.lower().replace(' ', '')

    IC = 0.0
    frequencies = calcLetterFrequency(message)

    #Sum the square of each letter frequency, then divide that by the total^2.
    for charFreq in frequencies:
        IC += charFreq[1]**2

    #Limit the IC to four decimal places.  No need for more.
    return round(IC / len(message)**2, 4)