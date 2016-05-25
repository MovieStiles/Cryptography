###
# Keyword Length Tests
#  Below are various methods of analyzing a message encrypted with a polyalphabetic
#  substitution cipher, and attempting to discover the length of the keyword used.
###

import re
from IndexOfCoincidence import findIndexOfCoincidence

#############################################################################
#                      Kasiski Test Code Section                            #
#   Code in this section from: http://inventwithpython.com/hacking/source/  #

NONLETTERS_PATTERN = re.compile('[^A-Z]')
SILENT_MODE = False  # if set to True, program doesn't print attempts
NUM_MOST_FREQ_LETTERS = 4  # attempts this many letters per subkey
MAX_KEY_LENGTH = 16  # will not attempt keys longer than this


def findRepeatSequencesSpacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).

    # Use a regular expression to remove non-letters from the message.
    message = NONLETTERS_PATTERN.sub('', message.upper())

    # Compile a list of seqLen-letter sequences found in the message.
    seqSpacings = {}  # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = message[seqStart:seqStart + seqLen]

            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []  # initialize blank list

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings


def getUsefulFactors(num):
    # Returns a list of useful factors of num. By "useful" we mean factors
    # less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
    # returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]

    if num < 2:
        return []  # numbers less than 2 have no useful factors

    factors = []  # the list of factors found

    # When finding factors, you only need to check the integers up to
    # MAX_KEY_LENGTH.
    for i in range(2, MAX_KEY_LENGTH + 1):  # don't test 1
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))


def getItemAtIndexOne(x):
    return x[1]


def getMostCommonFactors(seqFactors):
    # First, get a count of how many times a factor occurs in seqFactors.
    factorCounts = {}  # key is a factor, value is how often if occurs

    # seqFactors keys are sequences, values are lists of factors of the
    # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

    # Second, put the factor and its count into a tuple, and make a list
    # of these tuples so we can sort them.
    factorsByCount = []
    for factor in factorCounts:
        # exclude factors larger than MAX_KEY_LENGTH
        if factor <= MAX_KEY_LENGTH:
            # factorsByCount is a list of tuples: (factor, factorCount)
            # factorsByCount has a value like: [(3, 497), (2, 487), ...]
            factorsByCount.append((factor, factorCounts[factor]))

    # Sort the list by the factor count.
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount


def kasiskiExamination(ciphertext):
    # Find out the sequences of 3 to 5 letters that occur multiple times
    # in the ciphertext. repeatedSeqSpacings has a value like:
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    # See getMostCommonFactors() for a description of seqFactors.
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    # See getMostCommonFactors() for a description of factorsByCount.
    factorsByCount = getMostCommonFactors(seqFactors)

    # Now we extract the factor counts from factorsByCount and
    # put them in allLikelyKeyLengths so that they are easier to
    # use later.
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths


#                    End Kasiski Test Code Section                          #
#############################################################################

##
# friedmanTest
# Description: Given the length of a message and its index of coincidence,
# estimate the length of the keyword used to encrypt it using the Friedman test.
#
# Parameters:
#   mLength - The length of the encrypted message
#   ic - The index of the coincidence of the message
#
# Return:  The result of the equation rounded to 3 decimal places.
##
def friedmanTest(mLength, ic):
    denominator = (mLength - 1) * ic - 0.038 * mLength + 0.065
    return round((0.027 * mLength) / denominator, 3)


def friedmanTestOnMessage(cipherText):
    """Given a message, estimate the length of the keyword used to encrypt it using the Friedman test.

    Args:
        cipherText - The encrypted message

    Returns:
        The result of the equation rounded to 3 decimal places."""
    mLength = len(cipherText.replace(' ', ''))
    ic = findIndexOfCoincidence(cipherText)

    denominator = (mLength - 1) * ic - 0.038 * mLength + 0.065
    return round((0.027 * mLength) / denominator, 3)
