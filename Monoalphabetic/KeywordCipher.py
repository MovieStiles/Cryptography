###
# Keyword Cipher
#  A keyword cipher is very similar to caesar shift, except for
#  the brief involvement of a keyword to try and make the cipher a
#  little less obvious.
#
#  Let W be a word in plaintext and let X be a letter in plaintext alphabet.
#  We can define a keyword cipher with key(W, X) as follows:
#    1.	Rewrite W without duplicate letters
#    2.	Write the reduced keyword letter for letter beneath the plaintext alphabet stating at X.
#    3.	Write remaining letters in alphabetical order.
#    4. Perform the same letter substitution you should be used to by now.
#
#  For example: Key = (fox, k)
#  K   L   M   N   O   P   Q   R   S   T   U   V...
#  f   o   x   a   b   c   d   e   g   h   i   j...
#
# Encryption Example: Key = (crazytrain, d)
#  1. crazytrain -> crazytin
#  2. D -> c   E -> r   F -> a.... you get the idea.
#
#  Now to actually encrypt a word with this:

