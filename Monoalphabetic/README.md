
##Caesar Shift

A Caesar Shift, otherwise known as an Additive Cipher, takes the letters in a message and shifts them through the alphabet by some integer amount.

###Encryption Example: Key = 4

craze = 2 17 0 25 4 becomes 6 21 4 29 8 becomes 6 21 4 3 8 = gvedi

Any number greater than the index of Z loops back around, otherwise known as mod 26.

###Decryption

Decryption is easy.  Simply subtract the encryption key instead of adding. You can also add the additive inverse of the key.
From the previous example, -4 or 22 would be the decryption key.

##Additive Inverse

The additive inverse of a number, x, is another number, y, where x + y = 0.  In normal numbers, this is just simply the negative version.  In cases like this, we're only dealing with the numbers 0-25, so this changes slightly.
x + y = 0 still holds true, but now all numbers are mod 26, so 4 + 22 = 0

##Multiplicative Cipher

A multiplicative cipher is similar to the Caesar Shift, except instead of adding to the alphabetic index, the index is multiplied.
Because all of these numbers are mod 26, that means that one result can be shared by multiple multiplications.  For example:

4*1 = 4 and 4*14 = 56 = 4

This is bad since we don't want multiple letters mapping to one letter, since this will make decryption a nightmare, if not impossible.
Therefore, only certain integers are ok to use as keys.  Only integers which are relatively prime with 26 make valid keys.  The list of valid keys are: 3 5 7 9 11 15 17 19 21 23 25

###Encryption Example: Key = 3 and assuming A = 0

craze = 2 17 0 25 4 becomes 6 51 0 75 12 becomes 6 25 0 23 12 = gzaxm

I have seen some ciphers that assume A = 1, so I will include the ability to do both.

###Decryption

To find the decryption key, you must find the multiplicative inverse of the encryption key. The multiplicative inverse of 3 is 9.

gzaxm = 6 25 0 23 12 becomes 54 225 0 207 108 becomes 2 17 0 25 4 = craze

##Relatively Prime

Two numbers are relatively prime when their gcd = 1

##GCD

GCD stands for Greatest Common Divider.  It is the highest number that can evenly divide multiple numbers.  A very common algorithm for finding the gcd of two numbers is the Euclidean Algorithm.

##Multiplicative Inverse

The multiplicative inverse of a number, x, is another number, y, such that x*y = 1.  In the mod 26 world, for example, 3*9 = 27 = 1
Not all integers here have a multiplicative inverse, so not all 25 integers can be keys. For example, no possible number can be used for x such that 4*x mod 26 = 1
