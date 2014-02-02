import math

##
#isPrime
#Description: Check if a given number is prime.
#
#Parameters:
#   n - The number to check.  Must be > 1.
#
#Return: True if the number if prime.  False otherwise.
##
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

############################################
##   Finding the Multiplicative Inverse   ##

#Straight from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

##
#egcd
#Description: Recursive implementation of the Extended Euclidean Algorithm
# to find the gcd of two numbers.
#
#Parameters:
#   a - The first of two numbers to find the gcd of.
#   b - The second of the two numbers.
#
#Return: (g, x, y) such that ax + by = g = gcd(a, b)
##
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

##
#modinv
#Description: Find the multiplicative inverse of a number under a certain field
#
#Parameters:
#   a - The number to find the multiplicative inverse of
#   m - The modulo of the field
#
#Return: The multiplicative inverse of a if it exists
##
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

##   Finding the Multiplicative Inverse   ##
############################################