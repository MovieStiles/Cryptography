#Monoalphabetic Ciphers

A monoalphabetic cipher is a type of substitution cipher where each letter in the message is replaced with another letter based on some fixed pattern.

Below are explanations for each of the ciphers implemented in this folder.  These are meant for people are want to learn how these ciphers work, and likewise the code is meant to be friendly to the methodology of the cipher.

* Ciphers
   * [Additive Cipher (Caesar Shift)](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#caesar-shift)
   * [Multiplicative Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#multiplicative-cipher)
   * [Affine Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#affine-cipher)
   * [Keyword Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#keyword-cipher)
   * [Keyword Cipher Variant (Keyed Caesar Shift)](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#keyword-cipher-variant-keyed-caesar-shift)

* [Other Definitions](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#other-definitions)

##Additive Cipher (Caesar Shift)

A Caesar Shift, otherwise known as an Additive Cipher, takes the letters in a message and shifts the letters through the alphabet by some integer amount.

####Encryption Example: Key = 4

| Table | | | | | |
| --- | --- | --- | --- | --- | --- |
| Plaintext | c | r | a | z | e |
| Numeric form | 2 | 17 | 0 | 25 | 4 |
| Shift 4 | 6 | 21 | 4 | 29 | 8 |
| Mod 26 | 6 | 21 | 4 | 3 | 8 |
| Ciphertext | g | v | e | d | i |

Any number greater than the index of Z loops back around, otherwise known as mod 26.

####Decryption

Decryption is easy.  Simply subtract the encryption key instead of adding. You can also add the [additive inverse](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#additive-inverse) of the key.
From the previous example, -4 or 22 would be the decryption key.

| Table | | | | | |
| --- | --- | --- | --- | --- | --- |
| Ciphertext | g | v | e | d | i |
| Numeric form | 6 | 21 | 4 | 3 | 8 |
| Shift 22 | 28 | 43 | 26 | 25 | 30 |
| Mod 26 | 2 | 17 | 0 | 25 | 4 |
| Plaintext | c | r | a | z | e |

##Multiplicative Cipher

A multiplicative cipher is similar to the Caesar Shift, except instead of adding to the alphabetic index, the index is multiplied.
Because all of these numbers are mod 26, that means that one result can be shared by multiple multiplications.  For example:

4*1 = 4 and 4*14 = 56 = 4

This is bad since we don't want multiple letters mapping to one letter, since this will make decryption a nightmare, if not impossible.
Therefore, only certain integers are ok to use as keys.  Only integers which are [relatively prime](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#relatively-prime) with 26 make valid keys.  The list of valid keys are: 3 5 7 9 11 15 17 19 21 23 25

####Encryption Example: Key = 3 and assuming A = 0

| Table | | | | | |
| --- | --- | --- | --- | --- | --- |
| Plaintext | c | r | a | z | e |
| Numeric form | 2 | 17 | 0 | 25 | 4 |
| Times 3 | 6 | 51 | 0 | 75 | 12 |
| Mod 26 | 6 | 25 | 0 | 23 | 12 |
| Ciphertext | g | z | a | x | m |

I have seen some ciphers that assume A = 1, so I will include the ability to do both.

####Decryption

To find the decryption key, you must find the [multiplicative inverse](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#multiplicative-inverse) of the encryption key. The multiplicative inverse of 3 is 9.

| Table | | | | | |
| --- | --- | --- | --- | --- | --- |
| Ciphertext | g | z | a | x | m |
| Numeric form | 6 | 25 | 0 | 23 | 12 |
| Times 9 | 54 | 225 | 0 | 207 | 108 |
| Mod 26 | 2 | 17 | 0 | 25 | 4 |
| Plaintext | c | r | a | z | e |

##Affine Cipher

An affine cipher combines both an additive and multiplicative cipher in order to increase the obscurity of the resulting message.

In order to encrypt a message, you choose two keys, (x, y):  One, y, for the additive cipher and one, x, for the multiplicative.
First you put the message through the additive cipher, then you put it through the multiplicative cipher.

In other words, for each letter with index i:
The encrypted letter e is equal to x(i + y)

There's certainly no reason to not do them in reverse order. Because of that this file includes support for both ways.

####Encryption Example: Key(3, 5)

First use the additive cipher with key 5: craze -> hwfej
Then use the multiplicative cipher with key 3: hwfej -> jgzut

####Decryption Example: Key(3, 5)

Without knowing the encryption keys, frequency analysis would have to be done the same as when solving a multiplicative cipher.
It's difficult to do on a short example such as this, but it can be assumed that whatever the most frequent letter is, that's what maps to E.
The next step is just to figure out which order the ciphers are done in, and with what keys.

In this case, we have the encryption keys and the order, so we just need the decryption keys:  26 - 5 = 21 for the additive.  The multiplicative inverse of 3 in mod 26 is 9.

So: jgzut transformed by the multiplicative cipher with key 9 becomes hwfej.
Then hwfej transformed by the additive cipher with key 21 becomes craze.

##Keyword Cipher

A keyword cipher is very similar to caesar shift, except instead of shifting the entire alphabet by a number, the alphabet is shifted by a keyword.

Let W be a word in plaintext.
We can define a keyword cipher with key W as follows:

1. Rewrite W without duplicate letters
2. Write the reduced keyword letter for letter beneath the plaintext alphabet.
3. Write remaining letters in alphabetical order.
4. Perform the same letter substitution you should be used to by now.

For example: Key = fox

|Table | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plaintext Letter | A | B | C | D | E | F | G |
| Maps To | f | o | x | a | b | c | d |

And so on.

####Encryption Example: Key = crazytrain

crazytrain -> crazytin

| Table | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plaintext Letter | A | B | C | D | E | F | G | H | I | J |
| Maps To | c | r | a | z | y | t | i | n | b | d |

Now to actually encrypt a word with this:
"Here is a test message for your enjoyment" -> "nymybocpyopgyoociytjmwjqmyhdjwgyhp"

####Decryption

Decryption is the same in reverse, assuming you know the keyword.  If you don't know the keyword, then you once again need to employ frequency analysis to try and deduce what the letter correspondences are and what the keyword might be.

##Keyword Cipher Variant (Keyed Caesar Shift)

Another variant exists which also puts an additive cipher on top of the keyword cipher.
In this case, the cipher is as follows:

Let W be a word in plaintext and let X be a letter in plaintext alphabet.
We can define a keyword cipher with key(W, X) as follows:

1. Rewrite W without duplicate letters
2. Write a reduced keyword letter for letter beneath the plaintext alphabet stating at X.
3. Write remaining letters in alphabetical order.

####Encryption Example: Key = (crazytrain, d)

crazytrain -> crazytin

| Table | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plaintext Letter | D | E | F | G | H | I | J | K | L | M |
| Maps To | c | r | a | z | y | t | i | n | b | d |

---

##Other Definitions

###Relatively Prime

Two numbers are relatively prime when their gcd = 1

###GCD

GCD stands for Greatest Common Divider.  It is the highest number that can evenly divide multiple numbers.  A very common algorithm for finding the gcd of two numbers is the [Euclidean Algorithm](http://simple.wikipedia.org/wiki/Euclidean_algorithm).

###Additive Inverse

The additive inverse of a number, x, is another number, y, where x + y = 0.  In normal numbers, this is just simply the negative version.  In cases like this, we're only dealing with the numbers 0-25, so this changes slightly.
x + y = 0 still holds true, but now all numbers are mod 26, so 4 + 22 = 0

###Multiplicative Inverse

The multiplicative inverse of a number, x, is another number, y, such that x*y = 1.  In the mod 26 world, for example, 3*9 = 27 = 1
Not all integers here have a multiplicative inverse, so not all 25 integers can be keys. For example, no possible number can be used for x such that 4*x mod 26 = 1
