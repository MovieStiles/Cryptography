from MultiplicativeCipher import multiplicativeCipher
from CaesarShift import caesarShiftStringOps

##
#affineEncode
#Description:  Given a key tuple and a message, encode a message with an affine cipher.
#
#Parameters:
#   keys - A tuple of two keys.  It is assumed that the second of the two keys is the first cipher key.
#   message - The message to be encoded.
#   addFirst - Whether the additive cipher is first or not.  True by default.
#   aIsZero - Whether or not the index of A is assumed to be zero.  True by default.
#
#Return: The resulting message.
##
def affineEncode(keys, message, addFirst, aIsZero):
    if addFirst:
        message = caesarShiftStringOps(message, keys[1])
        message = multiplicativeCipher(message, keys[0], True, aIsZero)
    else:
        message = multiplicativeCipher(message, keys[1], True, aIsZero)
        message = caesarShiftStringOps(message, keys[0])

    return message

##
#affineDecode
#Description:  Given a key tuple and a message, decode a message with an affine cipher.
#
#Parameters:
#   keys - A tuple of two keys.  It is assumed that the second of the two keys is the first cipher key.
#          These are assumed to be the encryption keys.
#   message - The message to be decoded.
#   addFirst - Whether the additive cipher is first in the encryption or not.  True by default.
#   aIsZero - Whether or not the index of A is assumed to be zero.  True by default.
#
#Return: The resulting message.
##
def affineDecode(keys, message, addFirst, aIsZero):
    #When additive is done first in encryption, multiplicative needs to be
    # done first in decryption.
    if addFirst:
        #Both of these functions assume that the key is the decryption key,
        # so that's why this function does as well.
        message = multiplicativeCipher(message, keys[1], False, aIsZero)
        message = caesarShiftStringOps(message, keys[0], False)
    else:
        message = caesarShiftStringOps(message, keys[1], False)
        message = multiplicativeCipher(message, keys[0], False, aIsZero)

    return message