#Cryptography Python Scripts

This repo is to show all of the scripts I developed over the course of the last semester taking Cryptography.
Initially they were very rough and really only meant for my use, but over time I will clean them up (such as organizing them into actual functions), and post everything I used to help me crack the ciphers taught in this class.

The purpose of these is too help others with introducing themselves to cryptography, so I include a lot of documentation on what the different ciphers are and a few other definitions to try and help people who aren't as familiar with the concepts used.  I do not go too deeply into how all of the math works, because this is meant to be friendly to those who don't necessarily know a lot of advanced math.  So, for example, once I finish the RSA code, I will not go into how rings and fields and whatnot make the math possible, only that it works because multiplicative inverses are kickass.
Not all of this code is meant to outright crack the cipher for you (aka finding the decryption key and outputting the resulting plaintext).  For the monoalphabetic ciphers, it can often be trivial enough that the code certainly can do that, but more often than not this code will only help in some of the analysis of the ciphertext.
From there it's up to you.

Some of these include pieces of code that I found elsewhere, which I credit appropriately.

##Included Ciphers

* Monoalphabetic Ciphers (*COMPLETE*)
   * Additive Cipher (Caesar Shift) (*COMPLETE*)
   * Multiplicative Cipher (*COMPLETE*)
   * Affine Cipher (*COMPLETE*)
   * Keyword Cipher (*COMPLETE*)

* Polyalphabetic Ciphers (*COMPLETE*)
   * Vignere Cipher (*COMPLETE*)

* Polygraphic Ciphers
   * Hills System

* Public Key Cryptography
   * Exponentiation Cipher (*COMPLETE*)
   * RSA Algorithm
   * Signature Authentication
   * Diffie - Hellman Key Exchange
   * Massey - Omura System

* Elliptic Curve Cryptography
   * Elliptic Curves
   * Diffie - Hellman using Elliptic Curves

* Knapsack Cryptosystem

##Other Useful Scripts

* Index of Coincidence

The index of coincidence (IC) is defined to be the probability of two letters selected randomly from a text being the same letter.
This varies from language to language, so it offers a very quick and easy way to tell if some ciphertext has a frequency similar to the original language, and therefore used a
monoalphatetic cipher, or far enough away from the expected number to have undergone transformation with a polyalphabetic cipher.

English Language IC = 0.065

26 letter alphabet with all same frequency = 0.038

* Letter Frequency Analysis
* Prime Math