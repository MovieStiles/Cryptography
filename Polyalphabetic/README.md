#Polyalphabetic Ciphers

The problem with monoalphabetic ciphers is that there is a reliable 1-1 relationship between letters in the normal alphabet, and letters in a substitution alphabet.  Therefore you can use simple techniques such as letter frequency analysis to crack them.  Polyalphabetic ciphers, such as the Vignere Cipher, set out to solve this problem.
A **polyalphabetic cipher** one in which the correspondence between plaintext and ciphertext is not 1-1.  Alternatively, it is a substitution cipher using multiple substitution alphabets on different sections of the plaintext.

Below are explanations for each of the ciphers implemented in this folder.  It assumes that you know and understand any ideas introduced in the monoalphabetic ciphers, and likewise some of the code is built with more leaning towards performance and functionality over hand-holding the reader through the algorithms.

* Ciphers
   * [Vignere Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Polyalphabetic#vignere-cipher)

* Keyword Length Tests
   * [Kasiski Test](https://github.com/MovieStiles/Cryptography/tree/master/Polyalphabetic#kasiski-test)
   * [Friedman Test](https://github.com/MovieStiles/Cryptography/tree/master/Polyalphabetic#friedman-test)

##Vignere Cipher

A Vignere cipher uses a keyword to determine the multiple substitution alphabets used in encryption.

####Encryption Example: Keyword = "eat"  Message = "blue cheese"

To encrypt, we shift each letter by distance x-1 where x is the position of the keyword letter in the alphabet.

|Table       |   |   |   |   |   |   |   |   |   |   |
|:----------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plaintext  | B | L | U | E | C | H | E | E | S | E |
| Keyword    | E | A | T | E | A | T | E | A | T | E |
| Ciphertext | F | L | N | I | C | A | I | E | L | I |

####Decryption
To decrypt, we first need to ask if this is even a Vignere cipher in the first place.
One characteristic is that the letter frequency gets smoothed out compared to the monoalphabetic ciphers.  Check out the entry on the main page for the [index of coincidence](https://github.com/MovieStiles/Cryptography#index-of-coincidence) for more information.  If we already know, then we don't even need the actual keyword, just what it's length is.
From there it's just a monoalphabetic additive cipher on every nth letter in the message since each letter in the keyword shifts the corresponding letter in the plaintext the same way.

As for finding that keyword length...well, that's going to take a lot more work.  There are a few tests you can perform, but none of them are as accurate as one might like, so it's a good idea to conduct multiple tests.  The major ones that I discuss are the Kasiski test and the Friedman test.

---

##Kasiski Test

| Table | | | | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plaintext | c | h | e | e | s | e | c | h | e | e | s | e | c | h | e | e | s | e |
| Keyword | b | l | u | e | b | l | u | e | b | l | u | e | b | l | u | e | b | l |
| Ciphertext | **D** | **S** | **Y** | **I** | **T** | **P** | W | L | F | P | M | I | **D** | **S** | **Y** | **I** | **T** | **P** |

If a string of characters appears repeatedly in a ciphertext message, it is possible (though not certain) that the distance between the occurrences is a multiple of the keyword.  We see repetition in the ciphertext because the keyword synchronizes with the plaintext again.  While this example is rather artificial, given a lengthy enough message it’s reasonable to think that this could happen with repeated trigraphs.
In this case, the distance between the two repitions is 12 (from the start of one to the start of the other), which is indeed a multiple of our key length of 4.

You will hopefully find multiple instances of this happening, so you narrow your possibilities down to some of the common factors between the multiple distances.

##Friedman Test

Given a message of length n, with an index of coincidence of IC, the length of the keyword can be roughly evaluated with:

![equation](http://i.imgur.com/ddsjBkf.png) because math.

However, the accuracy of this test is about suck, so it would be best to try multiple key lengths near the result of the equation and should really be partnered with the results of the Kasiski test.