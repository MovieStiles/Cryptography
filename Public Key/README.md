#Public Key Cryptography

Public Key cryptography, otherwise known as asymmetric cryptography, is characterized by the existence of both a private key and a public key for each person using the cryptosystem.

If Alice wants to send a message to Bob, Alice encrypts the message using Bob's public key, then when Bob receives it he decrypts it using his private key.  This ensures that Bob is the only one who can read the message.  The reason why this works is because the keys are generated in such a way that they are easy to create, but it is impossible with today's math and computing power to determine the private key given the public key.

A very large part of why this works is because the math is done with really really large numbers, meaning that the time it would take to crack the encryption is so insanely big that it's not worth trying.

* Ciphers
  * [Exponential Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#exponential-cipher)
  * [RSA Algorithm](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#rsa-algorithm)

* [Other Definitions](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#other-definitions)
  * [Euler's Totient Function](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function)

##Exponential Cipher

Given a numeric representation of a message, m, an encryption key, e, and a prime, p, where the equation gcd(e, p-1) = 1 holds true, the following equation is used to generate the ciphertext, c:

c = m^e mod p

This equation is not just done on the entire message at once.  Instead the message is broken up into small chunks roughly less than p.  Once the math is done on each chunk, then the group is concatenated together to form a single ciphertext message.

####Encryption Example: p = 128189, e = 19, m = "Hello world"

For this example, we will be using ASCII as the numeric representation of our message.  This code also supports simply using the alphabetic index of a letter where A is either 0 or 1.

So "Hello world" becomes 072 101 108 108 111 032 119 111 114 108 100, and yes we do **need** to include the leading zeroes to make sure that they're all the same length (3 in this case).

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

To calculate the decryption key, all we need to do is find the multiplicative inverse of the encryption key under p - 1, or ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cphi%28p%29).  This is known as [Euler's Totient function](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#eulers-totient-function), or the phi function.

19 ^ -1 mod 128188 = 26987 = d

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

---

##Other Definitions

###Euler's Totient Function

Euler's Totient function (denoted with the Greek letter, phi) is a function that describes how many numbers less than a given n are relatively prime to n.  For our purposes, we'll only be using this function on prime numbers, and that's an easy calculation.  If n is a prime number, then by definition of it being prime, all numbers less than n are relatively prime to it.  Therefore an easy shortcut is:

![equation](http://latex.codecogs.com/gif.latex?%5Cphi%28n%29%3Dn-1)

That's how we get "p - 1" as our value in the Exponential Cipher decryption example.

This function has the property that it is a multiplicative function.  What that means is that ![equation](http://latex.codecogs.com/gif.latex?%5Cphi%28pq%29%3D%5Cphi%28p%29%5Cphi%28q%29%3D%28p-1%29%28q-1%29).