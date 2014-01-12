from fractions import gcd

##
#multiplcativeKeyCount
#Description: Given a length of some alphabet, calculate how many valid multiplicative cipher keys that alphabet can have.
# A key is valid if it is an integer less than the alphabet length and coprime with the alphabet length.
# Two numbers are coprime if the gcd of the two numbers is 1.
#
#Parameters:
#   alphabetLength - The length of the alphabet
#   showList - Whether or not to actually keep track of the list of keys
#
#Return: A tuple of the key count and the array of key values. The second value is None if showList is False.
##
def multiplicativeKeyCount(alphabetLength, showList = True):
    keyCount = 0
    keyList = []
    #Start at 2 because 1 and 0 are never valid keys
    for i in range(2, alphabetLength):
        #Inrease the key count if the gcd of the two numbers is one.
        if gcd(i, alphabetLength) == 1:
            keyCount += 1
            #Add to the list of keys if we're keeping track of that
            if showList:
                keyList.append(i)

    if showList:
        return keyCount, keyList
    else:
        return keyCount, None

def test():
    keys = multiplicativeKeyCount(26)
    print "Number of keys: ", keys[0]
    print "List of keys: ", keys[1]

    keys = multiplicativeKeyCount(26, False)
    print "Number of keys: ", keys[0]
    print "List of keys: ", keys[1]

    keys = multiplicativeKeyCount(42)
    print "Number of keys: ", keys[0]
    print "List of keys: ", keys[1]

#Output:
#Number of keys:  11
#List of keys:  [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
#Number of keys:  11
#List of keys:  None
#Number of keys:  11
#List of keys:  [5, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41]