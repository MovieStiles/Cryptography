###
# Index of Coincidence
#  The index of coincidence (IC) is defined to be the probability of two letters
#  selected randomly from a text being the same letter.  This varies from language
#  to language, so it offers a very quick and easy way to tell if some ciphertext
#  has a frequency similar to the original language, and therefore used a
#  monoalphatetic cipher, or far enough away from the expected number to have
#  undergone transformation with a polyalphabetic cipher.
#  English Language IC = 0.065      26 letter alphabet with all same frequency = 0.038
###

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

    #Limit the IC to five decimal places.  No need for more.
    return "{0:.5f}".format(IC / len(message)**2)

print findIndexOfCoincidence("ZPM XFC XEZ TGE EPU GIP YWF LHH UZG EUZ MEO OQM DSN LFE IQB EIA BDZ VFD BJS ZGX IPA ESO YRU SYG IPY WFH UWB DBE SAW LFO XES NBI FDY EOO NLF MLI BOQ ETQ LIT SZV PXN LFM UOF CS")