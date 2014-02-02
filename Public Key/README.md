#Public Key Cryptography

Public Key cryptography, otherwise known as asymmetric cryptography, is characterized by the existence of both a private key and a public key for each person using the cryptosystem.

If Alice wants to send a message to Bob, Alice encrypts the message using Bob's public key, then when Bob receives it he decrypts it using his private key.  This ensures that Bob is the only one who can read the message.  The reason why this works is because the keys are generated in such a way that they are easy to create, but it is impossible with today's math and computing power to determine the private key given the public key.

A very large part of why this works is because the math is done with really really large numbers, meaning that the time it would take to crack the encryption is so insanely big that it's not worth trying.

* Ciphers
  * [Exponential Cipher](https://github.com/MovieStiles/Cryptography/tree/master/Public%20Key#exponential-cipher)

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

To calculate the decryption key, all we need to do is find the multiplicative inverse of the encryption key under p - 1.

19 ^ -1 mod 128188 = 26987 = d

Now run the ciphertext through the equation, but this time using d instead of e.

![equation](http://i.imgur.com/n8oILRJ.png)

And there's our original numbers which we can easily translate from ASCII:  Hello world

####Afterthought

If you read the top definition of public key cryptography, you'll no doubt notice on glaring problem with this cipher: It is not actually public key cryptography.

The problem is that the decryption key, or private key, is far too easy to calculate once you know the encryption key, or public key.  I chose to include it here because it provides a good introduction to the type of methodology we can expect in the ciphers to come, including the next one: The RSA Algorithm.

