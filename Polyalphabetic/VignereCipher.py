###
# Polyalphabetic Ciphers
#  A polyalphabetic cipher one in which the correspondence between plaintext and ciphertext
#  is not 1-1.  Alternatively, it is a substitution cipher using multiple substitution alphabets.
###

###
# Vignere Cipher
#  The problem with monoalphabetic ciphers is that there is a reliable 1-1 relationship
#  between letters in the normal alphabet, and letters in a substitution alphabet.
#  Therefore you can use simple techniques such as letter frequency analysis to crack them.
#  Polyalphabetic ciphers, such as the Vignere Cipher, set out to solve this problem.
#
#  A Vignere cipher uses a keyword to determine the multiple substitution alphabets used in encryption.
#
# Encryption Example: Keyword = "eat"  Message = "blue cheese"
#  Plaintext	B	L	U	E	C	H	E	E	S	E
#  Keyword	    E	A	T	E	A	T	E	A	T	E
#  To encrypt, we shift each letter by distance x-1 where x is the position of the keyword
#  letter in the alphabet.
#
#  Ciphertext	F	L	N	E	C	A	I	E	L	I
#
# Decryption:
#  To decrypt, we first need to ask if this is even a Vignere cipher in the first place.
#  One characteristic is that the letter frequency gets smoothed out.  If we already know,
#  then we don't even need the actual keyword, just what it's length is.
#  From there it's just a monoalphabetic additive cipher.
#
#  As for finding that keyword length...well, that's going to take a lot more work.
#  There are a number of tests you can perform, but none of them are as accurate as
#  one might like, so it's a good idea to conduct multiple tests.
#  These tests are outlined in KeywordLengthTests.py.
###

