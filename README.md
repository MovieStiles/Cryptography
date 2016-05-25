#Cryptography Python Scripts

This repo is to show all of the scripts I developed over the course of taking University of Portland's Cryptography course in the fall of 2013.
Initially they were very rough and really only meant for my use, but over time I will clean them up (such as organizing them into actual functions), and post everything I used to help me crack the ciphers taught in this class.

The purpose of these is too help others with introducing themselves to cryptography, so I include a lot of documentation on what the different ciphers are and a few other definitions to try and help people who aren't as familiar with the concepts used.  I do not go too deeply into how all of the math works, because this is meant to be friendly to those who don't necessarily know a lot of advanced math.  So, for example, once I finish the RSA code, I will not go into how rings and fields and whatnot make the math possible, only that it works because multiplicative inverses are kickass.

Not all of this code is meant to outright crack the cipher for you (aka finding the decryption key and outputting the resulting plaintext).  For the monoalphabetic ciphers, it can often be trivial enough that the code certainly can do that, but more often than not this code will only help in some of the analysis of the ciphertext.
From there it's up to you.

Some of these include pieces of code that I found elsewhere, which I credit appropriately.

##Included Ciphers

* [Monoalphabetic Ciphers](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#monoalphabetic-ciphers)
   * [Additive Cipher (Caesar Shift)](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#caesar-shift)
   * [Multiplicative Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#multiplicative-cipher)
   * [Affine Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#affine-cipher)
   * [Keyword Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#keyword-cipher)
   * [Keyword Cipher Variant (Keyed Caesar Shift)](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#keyword-cipher-variant-keyed-caesar-shift)

* [Polyalphabetic Ciphers](https://github.com/MovieStiles/Cryptography/tree/master/Polyalphabetic#polyalphabetic-ciphers)
   * [Vignere Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Polyalphabetic#vignere-cipher)

* [Polygraphic Ciphers](https://github.com/MovieStiles/Cryptography/tree/master/Polygraphic#polygraphic-ciphers)
   * [Hills System](https://github.com/MovieStiles/Cryptography/tree/master/Polygraphic#hills-system)

* [Public Key Cryptography](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#public-key-cryptography)
   * [Exponential Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#exponential-cipher)
   * [RSA Algorithm](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#rsa-algorithm)
   * [Signature Authentication](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#signature-authentication)
   * [Diffie-Hellman Key Exchange](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#diffie-hellman-key-exchange)
   * [Massey-Omura System](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#massey-omura-system)

* [Elliptic Curve Cryptography](https://github.com/MovieStiles/Cryptography/tree/master/Elliptic%20Curves#elliptic-curve-cryptography)
   * [Elliptic Curves](https://github.com/MovieStiles/Cryptography/tree/master/Elliptic%20Curves#elliptic-curves)
   * Diffie - Hellman using Elliptic Curves

* Knapsack Cryptosystem

---

##Other Useful Scripts

### Index of Coincidence

The index of coincidence (IC) is defined to be the probability of two letters selected randomly from a text being the same letter.
This varies from language to language, so it offers a very quick and easy way to tell if some ciphertext has a frequency similar to the original language, and therefore used a
monoalphatetic cipher, or far enough away from the expected number to have undergone transformation with a polyalphabetic cipher.

English Language IC = 0.065

26 letter alphabet with all same frequency = 0.038

### Letter Frequency Analysis

Given a message, analysis the frequency of the various letters and return an ordered list of the letters along with their associated frequencies from most frequent to least.

### Crypto Math

An assortment of small misc functions that can be useful for many cryptosystems.

* isPrime: Check if a given number is a prime number.
* modInv: Find the multiplicative inverse of a number, a, modulus a number, m.