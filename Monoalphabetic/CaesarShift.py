import string


def caesarShift(message, key, encrypt=True):
    """Perform a Caesar Shift on a given message to either encrypt or decrypt the message.

    Args:
        message: The message to be encoded.
        key: The integer amount to shift the message by.  Assumed to be the encryption key.
        encrypt: Whether to encrypt the message or decrypt it. (default: True)

    Returns:
        The resulting message.
    """
    message = message.lower().replace(' ', '')
    alphabet = string.ascii_lowercase
    newMessage = ""

    # Change shift direction depending on encrypting or decrypting
    if not encrypt:
        key = -key

    # Loop through the message
    for char in message:
        index = alphabet.find(char)
        newMessage += alphabet[(index + key) % 26]

    return newMessage


def caesarShiftStringOps(message, key, encrypt=True):
    """Same as other caesarShift function, but uses string operations since those are implemented
        in C and therefore somewhat faster.  Found on Stack Overflow.
    """
    message = message.lower().replace(' ', '')
    alphabet = string.ascii_lowercase

    if not encrypt:
        key = -key

    shiftedAlphabet = alphabet[key:] + alphabet[:key]
    return message.translate(str.maketrans(alphabet, shiftedAlphabet))


def test():
    """A small function to test the outputs of the methods in this file.
    """
    print(caesarShift("Test message", 1))
    print(caesarShift("uftunfttbhf", 1, False))
    print(caesarShiftStringOps("Test message", 1))
    print(caesarShiftStringOps("uftunfttbhf", 1, False))

############################################

# Run the test method
test()

# Output:
# uftunfttbhf
# testmessage
# uftunfttbhf
# testmessage
