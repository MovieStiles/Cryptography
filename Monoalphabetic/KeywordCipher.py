import string


def keywordCipher(message, keyword, keyShift=0, encrypt=True):
    """Given a message and keyword, encrypt or decrypt a message using a keyword cipher.

    Args:
        message - The message to encrypt or decrypt.
        keyword - The keyword used in the cipher.
        keyShift - The amount to shift the new alphabet created by the keyword by. (default: 0)
        encrypt - True if encrypting, False otherwise. (default: True)

    Return:
        The resulting message.
    """
    message = message.lower().replace(' ', '')
    alphabet = string.ascii_lowercase

    # First, remove repeated characters from the keyword.
    # If anyone reading this can do it faster than O(n^2), let me know.
    keyword = ''.join(sorted(set(keyword), key=keyword.index))

    # Then build the new alphabet.
    newAlpha = keyword + ''.join(sorted(set(alphabet).difference(keyword)))
    # Then shift the new alphabet if there's any shifting to do.
    if not keyShift == 0:
        newAlpha = newAlpha[keyShift:] + newAlpha[:keyShift]

    # Now construct the new message

    # Normally, this would be the way to go:
    # for char in message:
    #    if encrypt:
    #        newMessage += newAlpha[alphabet.find(char)]
    #    else:
    #        newMessage += alphabet[newAlpha.find(char)]
    #
    # But that's just to make what's going on more clear.  I think we can move on
    # for efficiency sake by now.
    if encrypt:
        return message.translate(str.maketrans(alphabet, newAlpha))
    else:
        return message.translate(str.maketrans(newAlpha, alphabet))
