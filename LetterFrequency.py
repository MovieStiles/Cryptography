from collections import Counter


def calcLetterFrequency(message):
    """Given some text, calculate the frequency of all the letters in the text.

    Args:
        message - The text to calculate the letter frequency of

    Returns:
        An ordered list of all the letters and their corresponding frequencies from highest to lowest."""
    message = message.lower().replace(' ', '')
    frequencies = {}

    for char in message:
        # If the letter has already been seen, simply increment how many have been found
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return Counter(frequencies).most_common()


def test():
    """A small method to test the outputs of the methods in this file."""
    print(calcLetterFrequency("Here is a test message"))

    # Output:
    # [('e', 5), ('s', 4), ('a', 2), ('t', 2), ('g', 1), ('i', 1), ('h', 1), ('m', 1), ('r', 1)]
