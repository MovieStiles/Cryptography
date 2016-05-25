#Public Key Cryptography

Public Key cryptography, otherwise known as asymmetric cryptography, is characterized by the existence of both a private key and a public key for each person using the cryptosystem.

If Alice wants to send a message to Bob, Alice encrypts the message using Bob's public key, then when Bob receives it he decrypts it using his private key.  This ensures that Bob is the only one who can read the message.  The reason why this works is because the keys are generated in such a way that they are easy to create, but it is impossible with today's math and computing power to determine the private key given the public key.

A very large part of why this works is because the math is done with really really large numbers, meaning that the time it would take to crack the encryption is so insanely big that it's not worth trying.

* Ciphers
  * [Exponential Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#exponential-cipher)
  * [RSA Algorithm](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#rsa-algorithm)
  * [Signature Authentication](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#signature-authentication)
  * [Diffie-Hellman Key Exchange](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#diffie-hellman-key-exchange)
  * [Massey-Omura System](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#massey-omura-system)

* [Other Definitions](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#other-definitions)
  * [Euler's Totient Function](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function)

##Exponential Cipher

Given a numeric representation of a message, m, an encryption key, e, and a prime, n, where the equation gcd(e, n-1) = 1 holds true, the following equation is used to generate the ciphertext, c:

![equation](http://latex.codecogs.com/gif.latex?c%3Dm%5E%7Be%7D%20mod%28n%29)

Our key, e, must be relatively prime to n-1 as I said before, but the reason why we use n-1 is because of [Euler's Totient Function](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function).

This equation is not just done on the entire message at once.  Instead the message is broken up into small chunks roughly less than n.  Once the math is done on each chunk, then the group is concatenated together to form a single ciphertext message.

So the equation ends up looking more like: ![equation](http://latex.codecogs.com/gif.latex?c%3D%5C%7Bm_%7B1%7D%2C%20m_%7B2%7D%2C%20m_%7B3%7D%2C%20...%5C%7D%5E%7Be%7D%20mod%28n%29)

If you have the the encryption key, e, then the decryption key, d, can be calculated with:

![equation](http://latex.codecogs.com/gif.latex?d%3De%5E%7B-1%7D%20mod%28n%29)

This is otherwise known as finding the [multiplicative inverse](https://github.com/MovieStiles/Cryptography/tree/master/Monoalphabetic#multiplicative-inverse) of e.

The same equation you used to encrypt the text can now be used to decrypt it, simply replacing e with d and running the equation on each chunk of the ciphertext.

####Encryption Example: p = 2707, e = 17, m = "Hello"

For this example, we will be using the alphabetic index of each letter, assuming A = 0.  This code also supports assuming A = 1 and using the ASCII representation of a character.

So "Hello" becomes 08 05 12 12 15, and yes we do **need** to include the leading zeroes to make sure that they're all the same length (2 in this case).

Since we are using the alphabetic index starting at 0, the maximum value any letter can be is 25.  We calculate the size that we need to divide the message into with:

2525 < 2707 < 252525.  Therefore size = 2.

| Size = 2 | | | |
| --- | --- | --- | --- |
| Chunks | 0805 | 1212 | 1500 |

Notice that zeroes were added at the end of the last chunk in order to equal out the size. This just means that our message will have an extra "a" at the end, which should be easy for a human to spot.  Now run those numbers through the equation:

![equation](http://i.imgur.com/MYzegim.png)

Add in the necessary leading zeroes to each chunk of the message and our ciphertext is:

102525530490

####Decryption Example: p = 2707, e = 17

We already know the chunk size is 2, and honestly for educational purposes the ciphertext you look at will likely already be clearly spaced out enough that you can figure out the size anyway.

c = 1025 2553 0490

To calculate the decryption key, all we need to do is find the multiplicative inverse of the encryption key under p - 1, or ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cphi%28p%29).  This is known as [Euler's Totient function](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function), or the phi function.

![equation](http://latex.codecogs.com/gif.latex?17%5E%7B-1%7Dmod%282706%29%3D1751%3Dd)

Now run the ciphertext through the equation, but this time using d instead of e.

![equation](http://i.imgur.com/XHqHS9V.png)

And there's our original numbers which we can easily translate:  hello

####Encryption Example: p = 128189, e = 19, m = "Hello world"

For this example, we will be using ASCII as the numeric representation of our message.

So "Hello world" becomes 072 101 108 108 111 032 119 111 114 108 100.

Since we are using ASCII, the maximum value of any letter is 127.  We calculate the chunk size based on how many of those can fit under our p:

127127 < 128189 < 127127127.  Therefore size = 2.

| Size = 2 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Chunks | 072101 | 108108 | 111032 | 119111 | 114108 | 100000 |

Notice that zeroes were added at the end of the last chunk in order to equal out the size. 000 is null in ASCII anyway so this is fine.  Now run those numbers through the equation:

![equation](http://i.imgur.com/yiBpfAF.png)

Add in the necessary leading zeroes to each chunk and our ciphertext is:

104337081587003961057972096525027140

####Decryption Example: p = 128189, e = 19

We already know the chunk size is 2, and honestly for educational purposes the ciphertext you look at will likely already be clearly spaced out enough that you can figure out the size anyway.

c = 104337 081587 003961 057972 096525 027140

To calculate the decryption key, all we need to do is find the multiplicative inverse of the encryption key under p - 1, or ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cphi%28p%29).

![equation](http://latex.codecogs.com/gif.latex?19%5E%7B-1%7Dmod%28128188%29%3D26987%3Dd)

Now run the ciphertext through the equation, but this time using d instead of e.

![equation](http://i.imgur.com/n8oILRJ.png)

And there's our original numbers which we can easily translate from ASCII:  Hello world

####Afterthought

On the surface, this algorithm may seem to violate one of the basic rules of public key cryptography, and that is that we calculated the decryption key, or private key, fairly easily.  Here's the thing: When using this algorithm the way that it truly should be (with p being much MUCH larger, on the order of hundreds of digits), that is when it becomes nigh impossible with today's computing power to calculate the private key, because multiplicative inverses are kickass.

##RSA Algorithm

The RSA Algorithm is very close to the Exponential Cipher.  One key difference is in the initial setup.

If you've looked at the actual code for the Exponential Cipher, you'll notice that I have an optional parameter called q.  This is because in the Exponential Cipher, the modulus value, n, can either be a single large prime, or the product of two larger primes (someone feel free to correct me if I'm wrong on that, but that's how I understand it).  In the RSA algorithm; however, the modules is always the product of two large primes, p and q (that I know I'm right on).  That extra layer of obscurity, and the fact that you've made your already large modulus even larger, is what makes the private key that much harder for someone else to discover.

So as far as the code goes, nothing changes except that you must have a q, and some of the totient function calculations as described in the [definition below](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function).  The code handles that change, but it's good for you to know that that's what's happening.

The only reason why I even include an RSA file is to make the name of the function you're calling make more sense and to enforce the existence of q.

![image](http://i.imgur.com/8IouvzK.jpg)

No, not you.  Go away.

##Signature Authentication

So now we have made a huge step forward in assuring that any message sent can only be decrypted and read by its intended recipient.  There's just one problem:  We still haven't seen a way to ensure that the message is coming from who we think it is.  That is where signature authentication comes in.

The basic (and very simplified) premise is as follows if Alice wants to send a signature authenticated message to Bob:

1. Alice calculates d1(S) where d1 is her private key and S is her signature.
2. Next she encrypts it with Bob's public key, forming e2(d1(S)) and appends it to her encrypted message to Bob: e2(M).
3. Bob receives it and verifies that it's Alice's signature by first applying his private key, resulting in d1(S), then applying Alice's public key, decrypting the signature completely.  He can then verify that it matches her known signature.

##Diffie-Hellman Key Exchange

Suppose Alice and Bob want to share a key.  The Diffie-Helman system allows them to do this as follows:

1. Choose a (possibly public) large prime, p, and an arbitrary integer, q, such that q < p.

  1. We call q the base of the system.

2. Alice and Bob choose integers a and b such that 0 < a, b < p.  There are private keys.

  1. Alice chooses a while Bob chooses b.

3. Alice and Bob compute ![equation](http://latex.codecogs.com/gif.latex?A=q^amod%28p%29) and ![equation](http://latex.codecogs.com/gif.latex?B=q^bmod%28p%29) respectively, and exchange these values.  These are their public keys.

4. Alice calculates ![equation](http://latex.codecogs.com/gif.latex?K%3D%28q^b%29^amod%28p%29) and Bob calculates ![equation](http://latex.codecogs.com/gif.latex?K%3D%28q^a%29^bmod%28p%29).  Both of these come out to the same number, which is the key they share.

Any outside attacker has no knowledge of a, b, or the shared key.  They do know that the final shared key is the same, so the problem they have to solve is: ![equation](http://latex.codecogs.com/gif.latex?A^amod%28p%29%3DB^bmod%28p%29), where they know A, B, and p.  This turns out to be a very difficult problem to solve with large numbers.

##Massey-Omura System

1. Alice and Bob choose a very large prime number, p.

  1. p is a public number

2. Alice and Bob choose integers ![equation](http://latex.codecogs.com/gif.latex?e_1) and ![equation](http://latex.codecogs.com/gif.latex?e_2) that are both smaller than p.

3. Alice and Bob then calculate the multiplicative inverses of ![equation](http://latex.codecogs.com/gif.latex?e_1) and ![equation](http://latex.codecogs.com/gif.latex?e_2).

  1. ![equation](http://latex.codecogs.com/gif.latex?d_1%3D%20e_1%20mod%28%5Cphi%28p%29%29%2C%20d_2%3D%20e_2%20mod%28%5Cphi%28p%29%29)

4. To send a message M to Bob, Alice computes ![equation](http://latex.codecogs.com/gif.latex?M%5E%7Be_1%7Dmod%28p%29)

5. Bob receives that, calculates ![equation](http://latex.codecogs.com/gif.latex?%28M%5E%7Be_1%7D%29%5E%7Be_2%7Dmod%28p%29), and sends it back to Alice.

6. Alice then computes ![equation](http://latex.codecogs.com/gif.latex?%28%28M%5E%7Be_1%7D%29%5E%7Be_2%7D%29%5E%7Bd_1%7D%29mod%28p%29) and sends it back to Bob.

7. Finally, Bob computes ![equation](http://latex.codecogs.com/gif.latex?%28%28%28M%5E%7Be_1%7D%29%5E%7Be_2%7D%29%5E%7Bd_1%7D%29%5E%7Bd_2%7D%29mod%28p%29%20%3D%20M), and there's the original message.
---

##Other Definitions

###Euler's Totient Function

Euler's Totient function (denoted with the Greek letter, phi) is a function that describes how many numbers less than a given n are relatively prime to n.  For our purposes, we'll only be using this function on prime numbers, and that's an easy calculation.  If n is a prime number, then by definition of it being prime, all numbers less than n are relatively prime to it.  Therefore an easy shortcut is:

![equation](http://latex.codecogs.com/gif.latex?%5Cphi%28n%29%3Dn-1) where n is prime.

This function has the property that it is a multiplicative function.  What that means is that ![equation](http://latex.codecogs.com/gif.latex?%5Cphi%28pq%29%3D%5Cphi%28p%29%5Cphi%28q%29%3D%28p-1%29%28q-1%29).