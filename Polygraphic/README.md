#Polygraphic Ciphers

A **polygraphic cipher** is one in which blocks of plaintext are replaced by blocks of ciphertext.  This can easily be compared to a polyalphabetic substitution cipher, but this with splitting the text into blocks, or matrices.  Generally the block size is known, but that's not a big problem.

Since this involves matrices, this section does assume some knowledge of a few basic operations.  Namely: Matrix addition, scalar multiplication, and matrix multiplication.

* Ciphers
   * [Hills System](https://github.com/MovieStiles/Cryptography/tree/master/Polygraphic#hills-system)

* [Other Definitions](https://github.com/MovieStiles/Cryptography/tree/master/Polygraphic#other-definitions)
   * [Matrix Invertibility](https://github.com/MovieStiles/Cryptography/tree/master/Polygraphic#matrix-invertibility)

##Hills System

Also known as the **Hill Cipher**, it uses some linear algebra to encrypt and decrypt a message.  Besides that, it seems better to explain by example.

####Encryption Example: Message = "hello", and assume A = 1

Rather than using an encryption keyword, for this cipher we use an encryption matrix.  One restriction on our matrix is that it must be invertible.  Here's the encryption matrix we'll use:

![equation](http://latex.codecogs.com/gif.latex?\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix})

Because this is a 2x2 matrix, our message needs to split up into chunks of two.  However, there are five letters in our message, so we need to change it:

"hello" becomes "hellox" to fit the requirements of the matrix.  If our encryption matrix was a 3x3, then our message length would need to be divisible by three.

Now let's split our new message into the blocks of two: ![equation](http://latex.codecogs.com/gif.latex?\\begin{bmatrix}%208\\\\%205%20\\end{bmatrix}%20\\begin{bmatrix}%2012\\\\%2012%20\\end{bmatrix}%20\\begin{bmatrix}%2015\\\\%2024%20\\end{bmatrix})

Now to apply our encryption matrix to each block:

![equation](http://latex.codecogs.com/gif.latex?\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix}%20\\begin{bmatrix}%2018\\\\%203%20\\end{bmatrix}%20%3D%20\\begin{bmatrix}%208\\\\%205%20\\end{bmatrix}%20\\hspace{10%20mm}%20\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix}%20\\begin{bmatrix}%2012\\\\%2012%20\\end{bmatrix}%20%3D%20\\begin{bmatrix}%2010\\\\%2022%20\\end{bmatrix}%20\\hspace{10%20mm}%20\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix}%20\\begin{bmatrix}%2015\\\\%2024%20\\end{bmatrix}%20%3D%20\\begin{bmatrix}%2011\\\\%2017%20\\end{bmatrix}%20\\hspace{10%20mm})

Taking these three resulting blocks gives us the ciphertext: RCJVKQ

####Decryption Example: Ciphertext = "HZD UGQ OBK GHZ TGY KOB HZP QNS XV"

Coming Soon

---

##Other Definitions

###Matrix Invertibility

Let's use the following matrix to demonstrate the definition: ![equation](http://latex.codecogs.com/gif.latex?\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix})

A matrix is said to be **invertible** if a second matrix exists of the same size that can be multiplied with it to form the identity matrix.  For our example matrix:

![equation](http://latex.codecogs.com/gif.latex?\\begin{bmatrix}%20a%20%26%20b\\\\%20c%20%26%20d%20\\end{bmatrix}%20\\begin{bmatrix}%201%20%26%202\\\\%203%20%26%201%20\\end{bmatrix}%20%3D%20\\begin{bmatrix}%201%20%26%200\\\\%200%20%26%201%20\\end{bmatrix}) where a, b, c, and d are integers.

For any matrix containing the elements a, b, c, and d, if the inverse exists it is equal to: ![equation](http://latex.codecogs.com/gif.latex?\\frac{1}{ad-bc}%20\\begin{bmatrix}%20d%20%26%20-b\\\\%20-c%20%26%20a%20\\end{bmatrix})

ad-bc is also the [determinant](http://en.wikipedia.org/wiki/Determinant) of the matrix, which provides a way to test if a matrix is invertible.

As [Wikipedia](http://en.wikipedia.org/wiki/Hill_cipher) says:  "The matrix will have an inverse if and only if its determinant is not zero, and does not have any common factors with the modular base. Thus, if we work (in) modulo 26 as above, the determinant must be nonzero, and must not be divisible by 2 or 13."  Another thing that can be said is that the determinant must have a multiplicative inverse in the modulo base.

