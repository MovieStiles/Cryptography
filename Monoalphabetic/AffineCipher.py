###
# Affine Cipher
#  An affine cipher combines both an additive and multiplicative cipher
#  in order to increase the obscurity of the resulting message.
#
#  In order to encrypt a message, you choose two keys, (x, y):
#  One, y, for the additive cipher and one, x, for the multiplicative.
#  First you put the message through the additive cipher, then
#  you put it through the multiplicative cipher.
#  In other words, for each letter with index i:
#  The encrypted letter e is equal to x(i + y)
#
#  There's certainly no reason to not do them in reverse order.
#  Because of that this file includes support for both ways.
#
#  Encryption Example: Key(3, 5)
#  First use the additive cipher with key 5: craze -> hwfej
#  Then use the multiplicative cipher with key 3: hwfej -> jgzut
#
#  Decryption Example: Key(3, 5)
#  Without knowing the encryption keys, frequency analysis would have to be done
#  the same as when solving a multiplicative cipher.
#  It's difficult to do on a short example such as this, but it can be assumed
#  That whatever the most frequent letter is, that's what maps to E.
#  The next step is just to figure out which order the ciphers are done in, and
#  with what keys.
#
#  In this case, we have the encryption keys and the order, so we just need the
#  decryption keys:  26 - 5 = 21 for the additive.  The multiplicative inverse of 3 in mod 26 is 9.
#  So: jgzut transformed by the multiplicative cipher with key 9 becomes hwfej.
#  Then hwfej transformed by the additive cipher with key 21 becomes craze.
###

from MultiplicativeCipher import multiplicativeCipher
from CaesarShift import caesarShift

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
        message = caesarShift(message, keys[1])
        message = multiplicativeCipher(message, keys[0], True, aIsZero)
    else:
        message = multiplicativeCipher(message, keys[1], True, aIsZero)
        message = caesarShift(message, keys[0])

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
def affineEncode(keys, message, addFirst, aIsZero):
    #When additive is done first in encryption, multiplicative needs to be
    # done first in decryption.
    if addFirst:
        #Both of these functions assume that the key is the decryption key,
        # so that's why this function does as well.
        message = multiplicativeCipher(message, keys[1], False, aIsZero)
        message = caesarShift(message, keys[0], False)
    else:
        message = caesarShift(message, keys[1], False)
        message = multiplicativeCipher(message, keys[0], False, aIsZero)

    return message